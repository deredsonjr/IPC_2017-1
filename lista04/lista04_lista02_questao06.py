#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053
# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
a = float(input())
b = float(input())
c = float(input())

MEDIA = (a*2+b*3+c*5)/10

print("MEDIA = %0.1f" % MEDIA)
