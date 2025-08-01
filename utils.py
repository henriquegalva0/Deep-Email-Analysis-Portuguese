import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import pandas as pd # Necessário para recriar o LabelEncoder com as classes originais

# Carregar o tokenizador e o modelo salvos
# Certifique-se de que o caminho para o seu diretório 'model/' está correto
model_path = "model/" 
tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

# Mapear os rótulos de volta para suas classes originais (legitimo, phishing)
# Isso é importante para que a saída do modelo seja compreensível.
# Você precisa garantir que a ordem das classes seja a mesma de como
# o LabelEncoder foi treinado inicialmente.
# No seu script de treinamento: df['label'] = le.fit_transform(df['label'])
# Onde 'phishing' era 1 e 'legitimo' era 0.

# Se você tem o dataset original, pode carregá-lo para recriar o LabelEncoder.
# Caso contrário, defina as classes manualmente se souber a ordem exata.
try:
    df_original = pd.read_csv("data/ptbr-emails.csv")
    le = LabelEncoder()
    le.fit(df_original['label']) # Ajustar o LabelEncoder com as classes originais
    class_names = le.inverse_transform([0, 1]) # 0 e 1 são os rótulos numéricos
except FileNotFoundError:
    print("Aviso: 'data/ptbr-emails.csv' não encontrado. Assumindo classes [0: 'legitimo', 1: 'phishing'].")
    # Se você não tiver o arquivo original, e souber que 0 é "legitimo" e 1 é "phishing"
    class_names = ['legitimo', 'phishing']
    # Se o LabelEncoder mapeou 'phishing' para 1 e 'legitimo' para 0, então:
    # class_names = ['legitimo', 'phishing']
    # Caso contrário, ajuste para a ordem correta baseada no seu LabelEncoder
    
# Definir o dispositivo (CPU ou GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval() # Colocar o modelo em modo de avaliação

def classify_email(email_text):
    # Tokenizar o e-mail de teste
    inputs = tokenizer(email_text, return_tensors="pt", padding="max_length", truncation=True, max_length=256)
    
    # Mover os inputs para o mesmo dispositivo do modelo
    inputs = {key: value.to(device) for key, value in inputs.items()}
    
    # Fazer a previsão
    with torch.no_grad(): # Desativar o cálculo de gradientes para inferência
        outputs = model(**inputs)
    
    # Obter as probabilidades (softmax) e a classe prevista
    probabilities = torch.softmax(outputs.logits, dim=1)
    predicted_class_id = torch.argmax(probabilities, dim=1).item()
    
    # Mapear o ID da classe de volta para o nome da classe
    predicted_class_name = class_names[predicted_class_id]
    
    return predicted_class_name, probabilities.cpu().numpy()[0]

if __name__ == "__main__":
    print(f"Modelo e tokenizador carregados do diretório: {model_path}")
    print(f"Dispositivo de inferência: {device}")
    print(f"Classes de saída: {class_names}")

    while True:
        email_teste = input("\nDigite o texto do e-mail para classificação (ou 'sair' para encerrar): \n")
        if email_teste.lower() == 'sair':
            break
        
        predicted_label, probs = classify_email(email_teste)
        
        print(f"\nResultado da Classificação:")
        print(f"  Classe Prevista: {predicted_label}")
        print(f"  Probabilidades: Legitimo={probs[0]:.4f}, Phishing={probs[1]:.4f}")