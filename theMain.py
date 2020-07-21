import window
import gameEngine
from audioEngine import AudioEngine


def main():
    gameEngine.mainMenu(window.startScreen(), AudioEngine())

if __name__ == '__main__':
    main()

