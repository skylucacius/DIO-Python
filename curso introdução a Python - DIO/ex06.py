class MinhaException(Exception):
    pass

try:
    erro = False
    IError = True

    if erro:
        raise MinhaException('Deu erro aqui viu.')
except MinhaException as mensagem:
    print(mensagem)
