# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 22. Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono,
# onde N é o número de lados do polígono. Sabe-se que ND=N(N-3)/2.
#
angle1= int(input("Digite o angulo 1"))
angle2 = int(input("Digite o angulo2"))

angle_sum = angle1 + angle2

angle3 = 180 - angle_sum

print(angle3)
