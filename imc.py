# Código para cálculo de IMC
def calcular_imc():
    try:
        altura = float(input("Digite sua altura em metros (exemplo: 1.75): "))
        peso = float(input("Digite seu peso em kg (exemplo: 70): "))
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Baixo peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso adequado"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau I"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

# Chamar a função
if __name__ == "__main__":
    calcular_imc()
