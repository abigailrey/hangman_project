from game import HangmanGame
from utils import clear_screen, get_valid_letter


def main():
    while True:
        clear_screen()
        game = HangmanGame()

        print("¡Bienvenido al Juego del Ahorcado!\n")

        # Bucle principal de la partida
        while not game.is_game_over():
            game.display_status()
            
            # Pide y valida la letra usando utils.py
            letter = get_valid_letter(game.guessed_letters)
            
            # Procesa la letra ingresada con el nuevo método
            game.process_guess(letter)
            clear_screen()

        # Muestra el estado final al terminar
        game.display_status()

        if game.is_won():
            print("\n ¡Felicidades! ¡Has adivinado la palabra correcta!\n")
        else:
            print(f"\n ¡Te has quedado sin intentos! La palabra era: '{game.secret_word}'\n")

        # Preguntar si quiere jugar de nuevo
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if play_again != 's':
            print("\n¡Gracias por jugar! Hasta la próxima.")
            break


if __name__ == "__main__":
    main()
