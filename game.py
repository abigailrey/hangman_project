import random
from utils import get_random_word

HANGMAN_ART = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


class HangmanGame:
    def __init__(self, filename: str = "wordlist.txt", max_attempts: int = 6):
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.incorrect_attempts = 0
        self.guessed_letters = set()
        self.secret_word = get_random_word(filename)

    def get_display_word(self) -> str:
        """Retorna la palabra revelando las letras adivinadas y caracteres no alfabéticos."""
        displayed = []
        for char in self.secret_word:
            if not char.isalpha() or char.lower() in self.guessed_letters:
                displayed.append(char)
            else:
                displayed.append("_")
        return " ".join(displayed)

    def process_guess(self, letter: str) -> bool:
        """Procesa el intento del jugador: añade la letra y actualiza errores si falla."""
        letter = letter.lower()
        self.guessed_letters.add(letter)

        if letter in self.secret_word.lower():
            return True
        else:
            self.incorrect_attempts += 1
            return False

    def is_won(self) -> bool:
        """Verifica si el jugador ha adivinado todas las letras de la palabra."""
        for char in self.secret_word:
            if char.isalpha() and char.lower() not in self.guessed_letters:
                return False
        return True

    def is_game_over(self) -> bool:
        """Verifica si el juego terminó (ganó o se agotaron los intentos)."""
        return self.is_won() or self.incorrect_attempts >= self.max_attempts

    def display_status(self):
        """Muestra el dibujo actual del ahorcado, la palabra oculta e intentos."""
        print(HANGMAN_ART[self.incorrect_attempts])
        print(f"Palabra: {self.get_display_word()}")
        print(f"Letras usadas: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'Ninguna'}")
        print(f"Intentos fallidos: {self.incorrect_attempts}/{self.max_attempts}")
