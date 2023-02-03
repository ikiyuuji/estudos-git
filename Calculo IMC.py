peso=float(input("Digite o Peso(k
g):"))
altura=float(input("Digite o Altura(m):"))

IMC = peso / (altura**2)


if IMC < 20:
    print('Abaixo do peso ideal')
elif IMC > 25:
    print('Sobre peso')
else:
    print('Peso ideal')
