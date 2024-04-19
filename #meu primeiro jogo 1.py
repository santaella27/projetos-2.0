import random

while True:
    numero_secreto = random.randint(1, 100)

    while True:
        tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))

        if tentativa == numero_secreto:
            print("Você acertou!")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior!")
        else:
            print("Tente um número menor!")

    jogar_novamente = input("Quer jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        break

