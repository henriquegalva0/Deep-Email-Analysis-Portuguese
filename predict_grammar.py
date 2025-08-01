import language_tool_python

tool = language_tool_python.LanguageTool('pt-BR')

def detectar_erro_gramatical(texto):
    a=0
    erros = tool.check(texto)
    for erro in erros:
        a+=1
        print(f"Erro: {erro.message},Texto incorreto: {erro.context}")
    return a