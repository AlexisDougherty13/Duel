from threading import Thread
import pygame
import os

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
        pygame.mixer.music.set_volume(0.8)
        while self.Active:
            if self.songChange:
                if self.currentSong == "Main Menu":
                    path = "RedForestMap.wav"
                    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                    music_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), canonicalized_path)
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play(-1)
                elif self.currentSong == "Red Forest":
                    path = "RedForestMap.wav"
                    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                    music_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), canonicalized_path)
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play(-1)
                self.songChange = False


    def changeVolume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def getVolume(self):
        return pygame.mixer.music.get_volume()

    def changeSong(self, song):
        print("Wow?")
        self.currentSong = song
        self.songChange = True

    def getSong(self):
        return self.currentSong

    def closeAudioEngine(self):
        self.Active = False

    song = property(getSong, changeSong)
    volume = property(getVolume, changeVolume)