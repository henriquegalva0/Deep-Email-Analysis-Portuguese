def detectar_palavras_suspeitas(email_texto, typedef):
    # typedef=0 - conteúdo do e-mail
    # typedef=1 - assunto do e-mail
    phishing_elements = [
        [  # Conteúdo
            "ação necessária", "atenção imediata", "urgente", "aja agora", "sua conta será suspensa",
            "sua conta será encerrada", "falha ao cumprir", "alerta de segurança", "aviso", "tempo limitado",
            "expira em breve", "última chance", "atualização crítica", "conta comprometida", "atividade não autorizada detectada",
            "seu acesso será encerrado", "verifique sua conta imediatamente", "notificação oficial", "departamento de segurança",
            "suporte ao cliente", "departamento de cobrança", "suporte técnico", "administração", "mesa de serviços",
            "conformidade", "departamento jurídico", "fatura", "pagamento", "reembolso", "entrega", "imposto",
            "governo", "banco", "cartão de crédito", "paypal", "amazon", "netflix", "microsoft", "apple",
            "transação falhou", "pagamento pendente", "atividade incomum", "login suspeito", "conta bloqueada",
            "redefinir senha", "atualizar informações de pagamento", "verificar dados de pagamento", "débito/crédito",
            "saldo", "vencido", "fatura em anexo", "transferência bancária", "fundos", "acesso limitado", "conta congelada",
            "clique aqui", "verifique sua conta", "atualize suas informações", "faça login na sua conta",
            "confirme seus dados", "baixar anexo", "revisar o documento", "desbloquear sua conta",
            "acesse sua mensagem segura", "siga este link", "responda este e-mail", "preencha o formulário",
            "número do CPF", "data de nascimento", "nome da mãe", "número do cartão de crédito",
            "detalhes da conta bancária", "senha", "respostas de segurança", "nome completo", "endereço", "telefone",
            "nome de usuário", "caro cliente", "prezado usuário", "prezado cliente", "atenciosamente", "obrigado",
            "a equipe", "suporte ao cliente", "serviço de contas", "departamento de segurança", "certificado SSL",
            "criptografia", "endereço IP", "erro no servidor", "vazamento de dados", "firewall", "ataque phishing",
            "autenticação em duas etapas", "protocolo", "domínio", "proxy"
        ],
        [  # Assunto
            "urgente", "ação imediata", "responda agora", "última chance", "clique aqui", "confidencial",
            "verifique sua conta", "problema na conta", "conta bloqueada", "recuperar senha", "ganhe dinheiro",
            "você ganhou", "prêmio", "oferta exclusiva", "tempo limitado", "não perca", "grátis",
            "desconto especial", "parabéns", "saldo pendente", "transferência bancária", "pagamento pendente",
            "fatura", "reembolso", "conta vencida", "aviso importante", "alerta de segurança",
            "confirme suas informações", "atualização de conta", "login suspeito", "conta bloqueada",
            "dados bancários", "ação necessária", "veja o anexo", "mensagem importante", "nova mensagem",
            "resposta obrigatória"
        ]
    ]

    x = 0
    texto_normalizado = email_texto.lower()
    encontradas = []
    for palavra in phishing_elements[typedef]:
        if palavra.lower() in texto_normalizado:
            encontradas.append(palavra)
            x += 1
    return x