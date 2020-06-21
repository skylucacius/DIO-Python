def le_arquivo(nome):
    arquivo = open(nome, 'r')
    nota = arquivo.read().split('\n')
    for x in nota:
        aluno_nota = x.split(',')
        aluno_nota.pop(0)
        # print(aluno_nota)
        media_aluno = lambda lista_notas: sum([int(i) for i in lista_notas])/4
        print(media_aluno(aluno_nota))
    

if __name__ == "__main__":
    le_arquivo('file.txt')
