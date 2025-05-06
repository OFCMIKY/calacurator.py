def calculator():
    print("Jednoduchá kalkulačka")
    print("Vyber operaci:")
    print("1. Sčítání")
    print("2. Odčítání")
    print("3. Násobení")
    print("4. Dělení")

    try:
        choice = int(input("Zadej číslo operace (1/2/3/4): "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Zadej první číslo: "))
            num2 = float(input("Zadej druhé číslo: "))

            if choice == 1:
                print(f"Výsledek: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Výsledek: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Výsledek: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"Výsledek: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Chyba: Dělení nulou není povoleno.")
        else:
            print("Neplatná volba operace.")
    except ValueError:
        print("Chyba: Zadejte platné číslo.")

# Spuštění kalkulačky
if __name__ == "__main__":
    calculator()