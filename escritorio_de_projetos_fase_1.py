# Disciplina: Lógica e Programação de Computadores
# Aluno: Claudia Rayara Alves da Silva
# Escritório de Projetos - Fase 01

def obterNomeMes(numeroMes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[numeroMes - 1]

def main():
    totalMeses = 12
    somaTemperaturasMaximas = 0
    mesesQuentes = 0
    nomeMesMaisQuente = ""
    nomeMesMenosQuente = ""
    temperaturaMaisQuente = -float("inf")
    temperaturaMenosQuente = float("inf")

    for mes in range(1, totalMeses + 1):
        print("Mês:", end=" ")
        print(obterNomeMes(mes))

        while True:
            temperaturaMaxima = float(input("Digite a temperatura: "))
            
            if -60 <= temperaturaMaxima <= 50:
                break
            else:
                print("Temperatura inválida! Por favor, digite um valor que esteja entre -60 a 50 graus Celsius.")

        somaTemperaturasMaximas += temperaturaMaxima

        if temperaturaMaxima > temperaturaMaisQuente:
            temperaturaMaisQuente = temperaturaMaxima
            nomeMesMaisQuente = obterNomeMes(mes)

        if temperaturaMaxima < temperaturaMenosQuente:
            temperaturaMenosQuente = temperaturaMaxima
            nomeMesMenosQuente = obterNomeMes(mes)

        if temperaturaMaxima > 38:
            mesesQuentes += 1

    media_temperaturaMaxima = somaTemperaturasMaximas / totalMeses

    print("\nEstatísticas:")
    print(f"Temperatura média máxima anual: {media_temperaturaMaxima:.2f} graus Celsius")
    print(f"Quantidade de meses escaldantes: {mesesQuentes}")
    print(f"Mês mais escaldante do ano: {nomeMesMaisQuente}")
    print(f"Mês menos quente do ano: {nomeMesMenosQuente}")

if __name__ == "__main__":
    main()
