from math import pi
import math

print("Forneça um valor em graus e o programa irá aprensentar\no seu valor em radianos, o seno, o cosseno e a tangente do ângulo.")
grau=float(input("Digite o valor de um ângulo em graus: "))

print(f'O Ângulo {grau} em radianos é: ', math.radians(grau))
seno = math.sin(math.radians(grau))
print("O Ângulo {} tem seu seno como: {:.2f}" .format(grau, seno))
cosseno = math.cos(math.radians(grau))
print("O Ângulo {} tem seu cosseno como: {:.2f}" .format(grau, cosseno))
tangente = math.tan(math.radians(grau))
print("O Ângulo {} tem sua tangente como: {:.2f}" .format(grau, tangente))
