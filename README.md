# Deep-Email-Analysis-Portuguese
Using the bert-base-portuguese-cased model to analyze emails' contents

# Dataset
For security means, I did not uploaded the dataset used here.

# Utils
translate.py translates a dataset using "deep_translator".
train_phishing.py should be used for training the model if you got a dataset.

# Main Files
predict_words.py -> detects phishing related words in the topic/content of emails.
predict_grammar.py -> detects grammar mistakes in the topic/content of emails.
predict_characters.py -> detects unusual characters in the topic/content of emails.
predict_phishing.py -> calls the trained model to detect phishing in the content of emails.

pipeline_tool.py -> starts the verification with all 4 steps and creates one report.txt file.
