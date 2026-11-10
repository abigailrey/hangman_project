# Juego del Ahorcado (Cabrera Juan, Gilarde Romina, Rey Abigail)

Implementación interactiva en consola del clásico juego del ahorcado desarrollada en Python. El juego selecciona palabras o frases de forma aleatoria a partir de un archivo de texto y permite al usuario adivinar letra por letra dentro de un límite de 6 intentos fallidos.

##  Características
- **Carga dinámica de palabras:** Lee frases y palabras desde un archivo externo (`wordlist.txt`).
- **Revelado automático:** Espacios, signos de puntuación y caracteres especiales no alfabéticos se muestran descubiertos automáticamente desde el inicio.
- **Validación de entradas:** Filtrado de caracteres válidos y control de letras ya intentadas.
- **Visualización en ASCII:** Gráfico progresivo del ahorcado según los intentos fallidos acumulados.
- **Diseño modular y POO:** Lógica desacoplada mediante clases, clases auxiliares y módulos independientes.


##  Estructura del Proyecto

```text
hangman_project/
│
├── main.py          # Punto de entrada y bucle principal de la aplicación
├── game.py          # Clase HangmanGame (gestión del estado y reglas del juego)
├── utils.py         # Funciones auxiliares (lectura de archivos y validaciones)
├── wordlist.txt     # Lista de palabras/frases a adivinar (una por línea)
└── README.md        # Documentación del proyecto
