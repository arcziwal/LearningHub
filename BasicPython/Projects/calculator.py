def adding(num1, num2):
    return num1 + num2

def subtracting(num1, num2):
    return num1 - num2

def multiplying(num1, num2):
    return num1 * num2

def dividing(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return None

def main():

    while True:
        print("Witaj w kalkulatorze!")

        num1 = float(input("Podaj pierwsza liczbe: "))
        num2 = float(input("Podaj druga liczbe: "))

        print("Wybierz działanie: ")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print()

        choice = input("Twoj wybor: ")

        if choice == "1":
            print(f"Suma liczb: {num1} oraz {num2} wynosi: {adding(num1, num2)}")
        elif choice == "2":
            print(f"Różnica liczb: {num1} oraz {num2} wynosi: {subtracting(num1, num2)}")
        elif choice == "3":
            print(f"Iloczyn liczb: {num1} oraz {num2} wynosi: {multiplying(num1, num2)}")
        elif choice == "4":
            if num2 == 0:
                print("Niestety nie mogę tego obliczyć. Nie da się podzielić przez zero")
            else:
                print(f"Iloraz liczb: {num1} oraz {num2} wynosi: {dividing(num1, num2)}")


        repeat = input("Czy chcesz wykonać kolejne działanie? (t/n): ".lower())
        if repeat == 't':
            continue
        else:
            print("Dziękuję za użycie kalkulatora. Do zobaczenia")
            break

if __name__ == "__main__":
    main()