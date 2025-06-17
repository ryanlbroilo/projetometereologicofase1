
# Programa para análise de dados meteorológicos de 2021 (jan a dez)
# Recebe temperatura máxima de cada mês e calcula estatísticas conforme enunciado.

# Dicionário para converter número do mês em nome por extenso
meses_nome = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

def ler_mes():
    """Lê e valida o número do mês (1 a 12)."""
    while True:
        try:
            mes = int(input("Informe o mês (1 a 12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Erro: o mês deve estar entre 1 e 12.")
        except ValueError:
            print("Erro: valor inválido. Digite um número inteiro para o mês.")

def ler_temperatura(mes):
    """Lê e valida a temperatura máxima do mês (-60 a 50)."""
    while True:
        try:
            temp = float(input(f"Informe a temperatura máxima para {meses_nome[mes]} (em °C, entre -60 e 50): "))
            if -60 <= temp <= 50:
                return temp
            else:
                print("Erro: temperatura fora do intervalo válido (-60 a 50 °C).")
        except ValueError:
            print("Erro: valor inválido. Digite um número válido para a temperatura.")

def main():
    temperaturas = []
    meses_informados = set()  # para garantir que cada mês seja informado uma vez

    print("=== Cadastro de temperaturas máximas de 2021 ===")

    while len(temperaturas) < 12:
        mes = ler_mes()
        if mes in meses_informados:
            print(f"Erro: o mês {meses_nome[mes]} já foi informado. Digite outro mês.")
            continue
        temp = ler_temperatura(mes)
        temperaturas.append((mes, temp))
        meses_informados.add(mes)
    
    # Ordena os dados pela ordem dos meses
    temperaturas.sort(key=lambda x: x[0])
    
    # Cálculos
    soma_temps = sum(t[1] for t in temperaturas)
    media_maxima = soma_temps / 12

    # Quantidade de meses escaldantes (>33)
    qtd_escaldantes = sum(1 for t in temperaturas if t[1] > 33)

    # Mês mais escaldante
    mes_mais_escaldante = max(temperaturas, key=lambda x: x[1])[0]

    # Mês menos quente
    mes_menos_quente = min(temperaturas, key=lambda x: x[1])[0]

    # Resultados
    print("\n=== Resultados da análise ===")
    print(f"Temperatura média máxima anual: {media_maxima:.2f} °C")
    print(f"Quantidade de meses escaldantes (>33 °C): {qtd_escaldantes}")
    print(f"Mês mais escaldante do ano: {meses_nome[mes_mais_escaldante]}")
    print(f"Mês menos quente do ano: {meses_nome[mes_menos_quente]}")

if __name__ == "__main__":
    main()
