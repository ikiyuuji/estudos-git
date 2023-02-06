# fornecendo apenas o diametro de um circulo, ele calcula e mostra a sua área
from math import pi

diametro=float(input("Digite o diametro do circulo (cm): "))

raio = diametro / 2
area_do_circulo = pi * raio**2

print(f'A area do circulo é {area_do_circulo} cm²')
