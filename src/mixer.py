import random
import pygame
from constants import Constants

class Mixer:
    def __init__(self, pygame_mixer):
        self.pygame_mixer = pygame_mixer
        self.pygame_mixer.music.load(Constants.MUSIC_BACKGROUND_INTRO)
        self.myevent = pygame.USEREVENT+100
        self.pygame_mixer.music.set_endevent(self.myevent)

    def play_music(self):
        self.pygame_mixer.music.play()

    def stop_music(self):
        self.pygame_mixer.music.load(Constants.MUSIC_BACKGROUND)

    def play_sound(self, soundname):
        soundfile = Constants.SOUNDS[soundname]

        # This logic adds more variety to sfx like explosions
        if isinstance(soundfile, list):
            soundfile = soundfile[random.randint(0, len(soundfile)-1)]

        sound = self.pygame_mixer.Sound(soundfile)
        sound.play()

    def handle_event(self, event):
        if event.type == self.myevent:
            self.stop_music()
            self.play_music()
