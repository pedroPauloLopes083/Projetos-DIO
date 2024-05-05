def recomendar_plano(consumo):
    essencial_fibra = consumo <= 10
    prata_fibra = 10 <= consumo <= 20
    premium_fibra = consumo >= 20

    if essencial_fibra:
        return "Plano Essencial Fibra - 50Mbps"
    elif prata_fibra:
        return "Plano Prata Fibra - 100Mbps"
    elif premium_fibra:
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira o valor do consumo médio mensal: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
