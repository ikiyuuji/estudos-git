import random
import os

def gerar_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]
    cpf = cpf + calcula_digitos_verificadores(cpf)
    return ''.join(map(str, cpf))

def calcula_digitos_verificadores(cpf):
    v1 = sum([x * (10 - i) for i, x in enumerate(cpf[:9])])
    d1 = 11 - (v1 % 11)
    if d1 >= 10:
        d1 = 0
    v2 = sum([x * (11 - i) for i, x in enumerate(cpf[:9] + [d1])])
    d2 = 11 - (v2 % 11)
    if d2 >= 10:
        d2 = 0
    return [d1, d2]

def pedir_cpf():
    cpf = input("Digite o CPF: ")
    if validar_cpf(cpf):
        print("CPF válido!")
        return cpf
    else:
        print("CPF inválido!")
        return None

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():
        return False
    cpf = [int(x) for x in cpf]
    dv = calcula_digitos_verificadores(cpf[:9])
    return dv == cpf[9:]

def salvar_cpf(cpf, gerado=True):
    if gerado:
        with open('cpfs_gerados.bin', 'ab') as f:
            f.write(bytes(cpf + '\n', 'utf-8'))
    else:
        with open('cpfs_adicionados.bin', 'ab') as f:
            f.write(bytes(cpf + '\n', 'utf-8'))

def ler_cpfs():
    cpfs_validos_gerados = []
    cpfs_invalidos_gerados = []
    cpfs_validos_adicionados = []
    cpfs_invalidos_adicionados = []
    
    with open('cpfs_gerados.bin', 'rb') as f:
        for line in f:
            cpf = line.decode('utf-8').strip()
            if validar_cpf(cpf):
                cpfs_validos_gerados.append(cpf)
    
    with open('cpfs_adicionados.bin', 'rb') as f:
        for line in f:
            cpf = line.decode('utf-8').strip()
            if validar_cpf(cpf):
                cpfs_validos_adicionados.append(cpf)
            else:
                cpfs_invalidos_adicionados.append(cpf)
    
    print("CPFs gerados válidos:")
    print(cpfs_validos_gerados)
     
    print("CPFs adicionados válidos:")
    print(cpfs_validos_adicionados)
    
    print("CPFs adicionados inválidos:")
    print(cpfs_invalidos_adicionados)

while True:
    opcao = input("Digite 1 para gerar um CPF ou 2 para digitar um CPF: ")
    
    if opcao == '1':
        cpf = gerar_cpf()
        print(f"CPF gerado: {cpf}")
        salvar_cpf(cpf)
        
    elif opcao == '2':
        cpf = pedir_cpf()
        
        if cpf is not None:
            salvar_cpf(cpf, False)
            
    else:
        break

ler_cpfs()
