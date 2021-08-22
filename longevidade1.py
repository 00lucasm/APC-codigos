'''
Longevidade na UnB I
'''
def quantosSemestres(matricula, ano_atual, semestre_atual):
    ano_de_ingresso = matricula//10000000
    sem_ingresso = (((matricula//100000)%1000)%100)
    ano_atual = (ano_atual%100)
    total_anos = ano_atual - ano_de_ingresso

    print((total_anos*2)+(semestre_atual-sem_ingresso))

#quantosSemestres(200012345,2020,0)
#quantosSemestres(200054321,2020,1)
#quantosSemestres(180134242,2020,0)
