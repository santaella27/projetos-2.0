# conversor de unidades simples.py

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32
def main():
    celsius = float(input('digite a temperatura em celsius: '))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f'a temperatura em fahrenheit é {fahrenheit:.2f} fahrenheit.')

    if __name__ == '__main__':
        main()