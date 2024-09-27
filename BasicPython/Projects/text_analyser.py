import re
import sys
from os.path import split


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

def text_input():
    text_input_options = """Wybierz odpowiednią opcję wprowadzenia tekstu:
    1. Wpisz tekst do analizy
    2. Wczytaj tekst do analizy z pliku txt
    3. Wyjście z programu"""
    decision = input(text_decorator(text_input_options))
    return decision

def text_loader():
    while True:
        decision = text_input()
        if decision == "1":
            text = input("Wpisz poniżej tekst do analizy:\n")
            normalized_text = text_normalizer(text)
            return normalized_text
        elif decision == "2":
            text = load_text_from_file()
            if text:
                normalized_text = text_normalizer(text)
                return normalized_text
            else:
                continue
        elif decision == "3":
            sys.exit("Dziękuję za użycie Analizatora Tekstu. Miłego dnia!")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie")
            continue

def text_decorator(text):
    text = text.capitalize()
    border = "*" * 50
    return f"{border}\n{text}\n{border}\n"


def text_analyse_menu():
    text_analyse_options = """Aby przeanalizować tekst wybierz dostępne opcje:
    1. Zlicz słowa
    2. Załaduj nowy tekst
    3. Wyjście z programu"""
    decision = input(text_decorator(text_analyse_options))
    return decision

def count_words(text):
    text = text.split()
    words_count = len(text)
    return words_count



if __name__ == "__main__":
    text_to_analyse = text_loader()
    while True:
        user_decision = text_analyse_menu()
        if user_decision == "1":
            words_number = count_words(text_to_analyse)
            print(f"\nTwój tekst zawiera {words_number} słów.")
            continue
        elif user_decision == "2":
            text_to_analyse = text_loader()
            continue
        elif user_decision == "3":
            sys.exit("Dziękuję za użycie Analizatora Tekstu. Miłego dnia!")


