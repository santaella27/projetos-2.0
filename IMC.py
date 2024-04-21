def calcular_imc():
    print('Bem-vindo ao calculador de IMC')
    peso = float(input('Digite seu peso em KG:'))
    altura = float(input('Digite sua altura em Metros:'))
    imc = peso / (altura ** 2)
    print(f'Seu IMC é: {imc:.2f}')
    if imc < 18.5:
        print('Voce está abaixo do peso, Vamos cuidar da alimentação!')
    elif 18.5 <= imc < 25:
        print('Voce está no peso normal, Parabéns!')
    elif 25 <= imc < 30:
        print('Voce esta com sobrepeso, Vamos cuidar da alimentação!')
    else:
        print('Voce esta obeso. Procure um médico!')

if __name__ == '__main__':
    calcular_imc()

                   

                   