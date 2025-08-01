import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import pandas as pd

model_path = "model/" 
tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

try:
    df_original = pd.read_csv("data/ptbr-emails.csv")
    le = LabelEncoder()
    le.fit(df_original['label'])
    class_names = le.inverse_transform([0, 1])
except FileNotFoundError:
    print("Aviso: 'data/ptbr-emails.csv' não encontrado. Assumindo classes [0: 'legitimo', 1: 'phishing'].")
    class_names = ['legitimo', 'phishing']
    
# Definir o dispositivo (CPU ou GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def detectar_email_suspeito(email_text):
    inputs = tokenizer(email_text, return_tensors="pt", padding="max_length", truncation=True, max_length=256)

    inputs = {key: value.to(device) for key, value in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)
    predicted_class_id = torch.argmax(probabilities, dim=1).item()

    predicted_class_name = class_names[predicted_class_id]
    
    return predicted_class_name, probabilities.cpu().numpy()[0]

if __name__ == "__main__":
    print(f"Modelo e tokenizador carregados do diretório: {model_path}")
    print(f"Dispositivo de inferência: {device}")
    print(f"Classes de saída: {class_names}")