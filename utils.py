import os
import random


def clear_screen():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_letter(guessed_letters: set) -> str:
    """Solicita y valida que la entrada del usuario sea una sola letra no repetida."""
    while True:
        user_input = input("\nIngresa una letra: ").strip().lower()

        if len(user_input) != 1 or not user_input.isalpha():
            print("❌ Entrada no válida. Por favor, ingresa solo UNA letra.")
        elif user_input in guessed_letters:
            print(f"⚠️ Ya habías intentado la letra '{user_input}'. Intenta con otra.")
        else:
            return user_input


def get_random_word(filename: str = "wordlist.txt") -> str:
    """Lee todas las palabras de wordlist.txt y devuelve una aleatoriamente."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Lee las líneas y elimina espacios en blanco alrededor
            words = [line.strip() for line in file if line.strip()]
        
        if not words:
            raise ValueError("El archivo de palabras está vacío.")
        
        return random.choice(words)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'.")
        exit(1)
