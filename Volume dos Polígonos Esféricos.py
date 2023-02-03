from math import pi
print('Valor de pi: ', pi)
raio=int(input("Digite o valor do raio (cm):"))
altura=int(input("Digite o valor do altura (cm):"))

volume_cone = 1/3 * pi * (raio**2) * altura
print('Volume Cone: ', volume_cone, "cm³")
volume_cilindro = pi * (raio**2) * altura
print('Volume Cilindro: ', volume_cilindro, "cm³")
volume_esfera = 4/3 * pi * (raio**3)
print('Volume Esfera: ', volume_esfera, "cm³")

if volume_cone > volume_cilindro and volume_cone > volume_esfera:
    print('O Cone possui o maior volume')
elif volume_cilindro > volume_cone and volume_cilindro > volume_esfera:
    print('O Cilindro possui o maior volume')
else:
    print('A Esfera possui o maior')
if volume_cone < volume_cilindro and volume_cone < volume_esfera:
    print('E o Cone possui o menor volume')
elif volume_cilindro < volume_cone and volume_cilindro < volume_esfera:
    print('E o Cilindro possui o menor volume')
else:
    print('E a Esfera possui o menor volume')
