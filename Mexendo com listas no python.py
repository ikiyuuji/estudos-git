nomesenumeros = ["Paulo", "Leiticia", "9198278384", "Carlos", "912312321", "916612311", "Alex", "Pascal", "918223122"]
nomesenumeros.sort()
print(f'Lista de nomes e numeros de contato', nomesenumeros)

altlist=input("Deseja alterar ou adicionar itens da lista? ")
while altlist == "sim":
    altouadd=input("Alterar ou adicionar? ")
    if altouadd == "alterar" or altouadd == "Alterar":
        print(nomesenumeros)
        pos=int(input("Qual posição deseja alterar? "))
        elemento=input("Novo elemento = ")
        nomesenumeros.pop(pos), nomesenumeros.insert(pos, elemento)
        altlist=input("Deseja alterar ou adicionar itens da lista? ")
    elif altouadd == "adicionar" or altouadd == "Adicionar": 
        print(nomesenumeros)
        elemento=input("Novo elemento = ")
        nomesenumeros.append(elemento) 
        altlist=input("Deseja alterar ou adicionar itens da lista? ")

nomesenumeros.sort()
print(nomesenumeros)
Qnomes=int(input("Quantos nomes há na lista? "))
Qnumeros=int(input("Quantos números há na lista? "))

for i in range(Qnumeros):
    print(f'Numeros na lista', nomesenumeros[i])


nomesenumeros.reverse()

for i in range(Qnomes):
    print(f'Nomes na lista', nomesenumeros[i])
