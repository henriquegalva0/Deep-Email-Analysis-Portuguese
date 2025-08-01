from deep_translator import GoogleTranslator
import pandas as pd
from tqdm import tqdm

# Carregar dataset completo
df = pd.read_csv("dataset/emails.csv")

# Selecionar 500 exemplos aleatórios de cada classe
df_0 = df[df["label"] == 0].sample(n=5000, random_state=42)
df_1 = df[df["label"] == 1].sample(n=5000, random_state=42)

# Concatenar os dois subconjuntos
df_amostra = pd.concat([df_0, df_1]).reset_index(drop=True)

# Limite de caracteres por tradução
limite = 4999

# Progresso com tqdm
tqdm.pandas()

# Função de tradução com tratamento de exceções e limite de tamanho
def traduzir_texto(texto):
    try:
        if pd.isna(texto) or texto.strip() == "":
            return ""
        if len(texto) > limite:
            texto = texto[:limite]  # cortar até o limite
        return GoogleTranslator(source='en', target='pt').translate(texto)
    except Exception as e:
        return f"[ERRO] {str(e)}"

# Aplicar tradução
df_amostra["body-pt"] = df_amostra["body"].progress_apply(traduzir_texto)

# Selecionar apenas as colunas desejadas
df_resultado = df_amostra[["body-pt", "label"]]

# Salvar como CSV
df_resultado.to_csv("ptbr-emails.csv", index=False)
