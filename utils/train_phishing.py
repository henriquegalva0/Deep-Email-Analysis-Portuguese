import pandas as pd
from datasets import Dataset
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Alteração 1: Trocar o tokenizador para "neuralmind/bert-base-portuguese-cased" (BERTimbau)
tokenizer = BertTokenizerFast.from_pretrained("neuralmind/bert-base-portuguese-cased")

# 1. Carregar o dataset
# Alteração 2: Trocar o nome do arquivo para "ptbr-emails.csv"
df = pd.read_csv("dataset/ptbr-emails.csv")
le = LabelEncoder()
# Alteração 3: Trocar o nome da coluna de texto para "body-pt"
df['label'] = le.fit_transform(df['label'])  # phishing = 1, legitimo = 0

# Corrigir tipo de texto
# Alteração 4: Trocar o nome da coluna de texto para "body-pt"
df['body-pt'] = df['body-pt'].astype(str)

# Separar
# Alteração 5: Trocar o nome da coluna de texto para "body-pt"
train_df, test_df = train_test_split(df, test_size=0.2)
train_ds = Dataset.from_pandas(train_df[["body-pt", "label"]])
test_ds = Dataset.from_pandas(test_df[["body-pt", "label"]])

# Tokenização segura
def tokenize(batch):
    # Alteração 6: Trocar o nome da coluna de texto para "body-pt"
    textos = [str(x) for x in batch["body-pt"]]
    return tokenizer(textos, padding="max_length", truncation=True, max_length=512)

train_ds = train_ds.map(tokenize, batched=True)
test_ds = test_ds.map(tokenize, batched=True)

# 5. Modelo
# Alteração 7: Trocar o modelo para "neuralmind/bert-base-portuguese-cased" (BERTimbau)
model = BertForSequenceClassification.from_pretrained("neuralmind/bert-base-portuguese-cased", num_labels=2)

# 6. Argumentos de treinamento
training_args = TrainingArguments(
    output_dir="model/",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_steps=10,
    save_total_limit=2,
)

# 7. Treinamento
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=test_ds,
)

trainer.train()

# 8. Salvar modelo
model.save_pretrained("model/")
tokenizer.save_pretrained("model/")
