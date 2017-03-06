# Para cada aluno matriculado na disciplina PD I deste semestre, será informado:
# o nome do aluno; o número de matrícula; e a nota final.
# Assuma um número arbitrário para o total de alunos da turma.
# O programa deve ler essas informações e imprimir, para cada turma, a sua identificação,
# o número de alunos aprovados (nota final >= 7), a média geral e a melhor nota na disciplina, neste semestre.

alunos = [['Antonio', 'Maria', 'Pedro', 'José', 'Tiago', 'Flávia'], [2001, 3102, 6473, 4675, 8492, 7594], [6.5, 4.9, 8.7, 9.0, 3.4, 8.5]]
# print(alunos[0][3])  # José
numero_aprovados = 0
total_medias = 0
index_melhor_nota = 0
for i in range(len(alunos[2])):
    if alunos[2][i] >= 7:
        numero_aprovados += 1
    total_medias += alunos[2][i]
    if alunos[2][index_melhor_nota] < alunos[2][i]:
        index_melhor_nota = i
print('Número de alunos aprovados:', numero_aprovados)
print('Média geral:', total_medias/len(alunos[2]))
print('Melhor nota:', alunos[1][index_melhor_nota], "-", alunos[0][index_melhor_nota], 'Nota:', alunos[2][index_melhor_nota])
