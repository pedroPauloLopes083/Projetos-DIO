# Criação da lista para armazenar os equipamentos
itens = []

# Loop para solicitar ao usuário inserir até três equipamentos
for item in range(3):
    equipamento = {}  # Dicionário para armazenar as informações de cada equipamento
    
    # Solicita ao usuário inserir as informações do equipamento
    equipamento["nome"] = input("Insira o nome do equipamento: ")
    
    # Adiciona o equipamento à lista
    itens.append(equipamento)

# Exibe a lista de equipamentos
print("\nLista de Equipamentos:")
for i, equipamento in enumerate(itens, 1):
    print(f" - {equipamento['nome']}")
