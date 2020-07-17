from threading import Thread
import pygame

class AudioEngine:

    def __init__(self):
        self.currentSong = "Main Menu"
        self.songChange = True
        self.Active = True
        try:
            self.thread = Thread(target=self.driver, args=())
            self.thread.start()
        except:
            print("Error: unable to start thread")

    def driver(self):
        pygame.mixer.init()
        while self.Active:
            if self.songChange:
                if self.currentSong == "Main Menu":
                    pygame.mixer.music.load("RedForestMap.wav")
                    pygame.mixer.music.play(-1)
                elif self.currentSong == "Red Forest":
                    pygame.mixer.music.load("RedForestMap.wav")
                    pygame.mixer.music.play(-1)
                self.songChange = False


    def changeVolume(self, volume):
        pygame.mixer.set_volume(volume)

    def getVolume(self):
        return pygame.mixer.get_volume()

    def changeSong(self, song):
        print("Wow?")
        self.currentSong = song
        self.songChange = True

    def getSong(self):
        return self.currentSong

    def closeAudioEngine(self):
        self.Active = False

    song = property(getSong, changeSong)