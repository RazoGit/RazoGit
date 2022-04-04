import random

def run():
    IMAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

    DB =[
        "C#",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP",
        "REACT",
        "C",
        "C++",
        "R",
        "SWIFT",
        "COBOL"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        print("Adivina el lenguaje de programacion\n")
        for character in spaces:
            print(character, end=" ")
        print (IMAGES[attemps])
        letter = input("Ingresa una letra\n").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            print(word)
            print (IMAGES[attemps])
            print(" \"Ganaste\" uwu")
            break
            input()
            
        if attemps == 0:
            print(word)
            print (IMAGES[attemps])
            print("Perdiste ;(")
            break
            input()

if __name__ == '__main__':
    run()

while (True):
    print(' 1) Jugar de nuevo? \n 2) salir')
    opcion = input()
    if opcion == "1":
        print(run())
    elif opcion =="2":
        break