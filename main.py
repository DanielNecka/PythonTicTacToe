from easyBot import EasyBot
from hardBot import HardBot
from playerVsPlayer import PlayerVsPlayer
from easyBotVsEasyBot import EasyBotVsEasyBot

def menu():
    print("=====Gra w Kółko i Krzyzyk=====\n\n1. Gra z botem (poziom łatwy)\n2. Gra z botem (poziom trudny)\n3. Gra z innym graczem (local)\n4. Bot vs Bot (poziom łatwe)\n5. Wyjscie\n")

    while True:
        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("Podaj poprawną opcję\n")
            continue

        if choice in [1, 2, 3, 4, 5]:
            if choice == 1:
                easyBotGame = EasyBot()
                easyBotGame.startGame()
                input("Naciśnij Enter, aby kontynuować...")
                menu()
            elif choice == 2:
                hardBot = HardBot()
                hardBot.startGame()
                input("Naciśnij Enter, aby kontynuować...")
                menu()
            elif choice == 3:
                playerVsPlayer = PlayerVsPlayer()
                playerVsPlayer.startGame()
                input("Naciśnij Enter, aby kontynuować...")
                menu()
            elif choice == 4:
                easyBotVsEasyBot = EasyBotVsEasyBot()
                easyBotVsEasyBot.startGame()
                input("Naciśnij Enter, aby kontynuować...")
                menu()
            elif choice == 5:
                return 0;
            return choice
        else:
            print("Podaj poprawną opcję 1–5!\n")

menu()