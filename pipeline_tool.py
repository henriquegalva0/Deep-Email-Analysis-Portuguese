from predict_characters import detectar_caracteres_conteudo, detectar_caracteres_assunto
from predict_grammar import detectar_erro_gramatical
from predict_phishing import detectar_email_suspeito
from predict_words import detectar_palavras_suspeitas
import sys
from io import StringIO

def suprimir_prints(func, *args, **kwargs):
    """Suprime declarações print para limpar a saída"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        resultado = func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout
    return resultado

def analisar_email_unico(assunto_email, conteudo_email):
    """Analisa um único email e retorna resultados com saída detalhada"""
    
    resultado_texto = []
    
    print("=" * 80)
    print("📧 ANÁLISE DE EMAIL")
    print("=" * 80)
    resultado_texto.append("=" * 80)
    resultado_texto.append("📧 ANÁLISE DE EMAIL")
    resultado_texto.append("=" * 80)
    
    # Exibir conteúdo do email
    print(f"📋 Assunto do Email: {assunto_email}")
    print(f"📄 Conteúdo do Email: {conteudo_email}")
    print()
    resultado_texto.append(f"📋 Assunto do Email: {assunto_email}")
    resultado_texto.append(f"📄 Conteúdo do Email: {conteudo_email}")
    resultado_texto.append("")
    
    print("🔍 RESULTADOS DO PIPELINE:")
    print("-" * 50)
    resultado_texto.append("🔍 RESULTADOS DO PIPELINE:")
    resultado_texto.append("-" * 50)
    
    # Etapa 1: Análise de Palavras
    print("1️⃣ DETECÇÃO DE PALAVRAS SUSPEITAS:")
    resultado_texto.append("1️⃣ DETECÇÃO DE PALAVRAS SUSPEITAS:")
    palavras_assunto = suprimir_prints(detectar_palavras_suspeitas, assunto_email, 1)
    palavras_conteudo = suprimir_prints(detectar_palavras_suspeitas, conteudo_email, 0)
    total_palavras = palavras_assunto + palavras_conteudo
    print(f"   • Palavras no assunto: {palavras_assunto}")
    print(f"   • Palavras no conteúdo: {palavras_conteudo}")
    print(f"   • Total de palavras suspeitas: {total_palavras}")
    print()
    resultado_texto.append(f"   • Palavras no assunto: {palavras_assunto}")
    resultado_texto.append(f"   • Palavras no conteúdo: {palavras_conteudo}")
    resultado_texto.append(f"   • Total de palavras suspeitas: {total_palavras}")
    resultado_texto.append("")
    
    # Etapa 2: Análise de Caracteres  
    print("2️⃣ DETECÇÃO DE CARACTERES SUSPEITOS:")
    resultado_texto.append("2️⃣ DETECÇÃO DE CARACTERES SUSPEITOS:")
    caracteres_assunto = suprimir_prints(detectar_caracteres_assunto, assunto_email)
    caracteres_conteudo = suprimir_prints(detectar_caracteres_conteudo, conteudo_email)
    total_caracteres = caracteres_assunto + caracteres_conteudo
    print(f"   • Caracteres no assunto: {caracteres_assunto}")
    print(f"   • Caracteres no conteúdo: {caracteres_conteudo}")
    print(f"   • Total de caracteres suspeitos: {total_caracteres}")
    print()
    resultado_texto.append(f"   • Caracteres no assunto: {caracteres_assunto}")
    resultado_texto.append(f"   • Caracteres no conteúdo: {caracteres_conteudo}")
    resultado_texto.append(f"   • Total de caracteres suspeitos: {total_caracteres}")
    resultado_texto.append("")
    
    # Etapa 3: Análise Gramatical
    print("3️⃣ DETECÇÃO DE ERROS GRAMATICAIS:")
    resultado_texto.append("3️⃣ DETECÇÃO DE ERROS GRAMATICAIS:")
    gramatica_assunto = suprimir_prints(detectar_erro_gramatical, assunto_email)
    gramatica_conteudo = suprimir_prints(detectar_erro_gramatical, conteudo_email)
    total_gramatica = gramatica_assunto + gramatica_conteudo
    print(f"   • Erros gramaticais no assunto: {gramatica_assunto}")
    print(f"   • Erros gramaticais no conteúdo: {gramatica_conteudo}")
    print(f"   • Total de erros gramaticais: {total_gramatica}")
    print()
    resultado_texto.append(f"   • Erros gramaticais no assunto: {gramatica_assunto}")
    resultado_texto.append(f"   • Erros gramaticais no conteúdo: {gramatica_conteudo}")
    resultado_texto.append(f"   • Total de erros gramaticais: {total_gramatica}")
    resultado_texto.append("")
    
    # Etapa 4: Classificação por IA
    print("4️⃣ PREDIÇÃO DE PHISHING POR IA:")
    resultado_texto.append("4️⃣ PREDIÇÃO DE PHISHING POR IA:")
    texto_completo = f"{assunto_email}\n\n{conteudo_email}"
    rotulo_previsto, probabilidades = suprimir_prints(detectar_email_suspeito, texto_completo)
    print(f"   • Classificação da IA: {rotulo_previsto}")
    print(f"   • Confiança - Legítimo: {probabilidades[0]:.4f}")
    print(f"   • Confiança - Phishing: {probabilidades[1]:.4f}")
    print()
    resultado_texto.append(f"   • Classificação da IA: {rotulo_previsto}")
    resultado_texto.append(f"   • Confiança - Legítimo: {probabilidades[0]:.4f}")
    resultado_texto.append(f"   • Confiança - Phishing: {probabilidades[1]:.4f}")
    resultado_texto.append("")
    
    # Resumo
    print("📊 RESUMO FINAL:")
    print("-" * 30)
    print(f"Palavras suspeitas: {total_palavras}")
    print(f"Caracteres suspeitos: {total_caracteres}")
    print(f"Erros gramaticais: {total_gramatica}")
    print(f"Predição da IA: {rotulo_previsto}")
    resultado_texto.append("📊 RESUMO FINAL:")
    resultado_texto.append("-" * 30)
    resultado_texto.append(f"Palavras suspeitas: {total_palavras}")
    resultado_texto.append(f"Caracteres suspeitos: {total_caracteres}")
    resultado_texto.append(f"Erros gramaticais: {total_gramatica}")
    resultado_texto.append(f"Predição da IA: {rotulo_previsto}")
    
    # Avaliação de risco
    pontuacao_risco = (total_palavras * 2 + total_caracteres * 1.5 + total_gramatica * 1 + 
                      (10 if rotulo_previsto == 'phishing' else 0))
    
    if pontuacao_risco >= 15:
        nivel_risco = "🔴 ALTO RISCO"
    elif pontuacao_risco >= 8:
        nivel_risco = "🟡 MÉDIO RISCO"
    else:
        nivel_risco = "🟢 BAIXO RISCO"
        
    print(f"Pontuação de Risco: {pontuacao_risco:.1f} - {nivel_risco}")
    print("=" * 80)
    print()
    resultado_texto.append(f"Pontuação de Risco: {pontuacao_risco:.1f} - {nivel_risco}")
    resultado_texto.append("=" * 80)
    resultado_texto.append("")
    
    return {
        'email_body': conteudo_email.strip(),
        'email_topic': assunto_email.strip(), 
        'word_counter': total_palavras,
        'characters_counter': total_caracteres,
        'grammar_mistakes': total_gramatica,
        'predict_phishing': rotulo_previsto
    }, resultado_texto

def salvar_resultados_txt(resultado_texto, nome_arquivo="resultados_analise_phishing.txt"):
    """Salva os resultados em arquivo de texto"""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in resultado_texto:
            arquivo.write(linha + '\n')
    print(f"\n💾 Resultados salvos em: {nome_arquivo}")

# Exemplo de uso com seus dados de email existentes
if __name__ == "__main__":
    # Seu email de teste
    email_teste_assunto = "Serviço locaweb - Cobrança Limite"
    email_teste_conteudo = """Olá!
Notamos qeu ua caixa de entrada estar Bem proxim oao limite de 11GB.
Para garantir o recebimento e  envio de mensagens, Libere mais 20 GB de espaço para o seu E-mail,
Efetuando o loguin em sua conta.
Efetuar Loguin
Atenção: Caso seu serviço seja suspenso, pode demorar até 48h para que ele seja reativado após
contratacao do locaweb"""
    
    # Analisar o email
    resultado, texto_resultado = analisar_email_unico(email_teste_assunto, email_teste_conteudo)
    
    # Salvar resultados em arquivo de texto
    salvar_resultados_txt(texto_resultado)
