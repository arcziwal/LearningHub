import re
import sys

def text_normalizer(text_to_normalize):
    text_to_normalize = text_to_normalize.lower()
    normalized_text = re.sub(r'[^\w\s]', "", text_to_normalize)
    return normalized_text

def load_text_from_file():
    while True:
        filename = input("Podaj ścieżkę do pliku: \n")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("Błąd! Nie odnaleziono pliku.")
            decision = input("Czy chcesz spróbować ponownie? (t/n)")
            if decision == "n":
                return None
            else:
                continue

def main_menu():
    border = "*" * 50
    welcome_text = "Witaj w Analizatorze tekstu. Wybierz odpowiednią opcję:"
    menu = """
    1. Wpisz tekst do analizy
    2. Wczytaj tekst do analizy z pliku txt
    3. Wyjście z programu
    """
    full_message = f"{border}\n{welcome_text}\n{border}\n{menu}\n"
    decision = input(full_message)
    return decision




if __name__ == "__main__":
    while True:
        decision = main_menu()
        if decision == "1":
            text = input("Wpisz poniżej swój tekst do przeanalizowania:\n")
            normalized_text = text_normalizer(text)
            print(f"Twój znormalizowany tekst to:\n{normalized_text}")
        elif decision == "2":
            text = load_text_from_file()
            if text:
                normalized_text = text_normalizer(text)
                print(f"Twój znormalizowany tekst to:\n{normalized_text}")
            else:
                continue
        elif decision == "3":
            sys.exit("Dziękuję za użycie Analizatora Tekstu. Miłego dnia!")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie")
            continue

