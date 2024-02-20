print("\nExercício 3 -------------------------------------------------------------------------------------------------")
aluno = {'nome': input('Digite o nome do aluno: ')}

aluno['media'] = input(f'Digita a media do aluno {aluno["nome"]}: ')

if int(aluno['media']) >= 60:
    aluno['status'] = 'AP'
else:
    aluno['status'] = 'RP'

print(aluno)
