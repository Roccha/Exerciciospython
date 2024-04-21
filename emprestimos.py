print('programa de empréstimos ##. responda: (0-não e 1 - sim')
nomeNegativado = int(input('Possui nome negativado?'))
if nomeNegativado == 1:
    print('Não pode realizar emprestimo!😩')
else:
    carteiraAsssinada = int(input('Possui carteira assinada?'))
    if carteiraAsssinada == 0:
        print('Não pode realizar emprestimo!😩 ')
    else:
        possuiCasaPropria = int(input('Possui casa propria?'))
        if possuiCasaPropria == 0:
            print('Não pode realizar emprestimo!😩 ')
        else:
            print('Conceder emprestimo!🤑')