import pygame
import os
import json


# Motion controller
class MotionController:

    def __init__(self) -> None:
        # Get joystick mapping
        with open(os.path.join("joysticks", "ps4_keys.json"), 'r+') as file:
            self.button_keys = json.load(file)

        self.fish_direction = {"X": 0, "Y": 0}

    def update(self, event):
       
        # Get all the keys currently pressed
        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_RIGHT] else -1 if pressed_keys[K_LEFT] else fish_direction["X"]
        # if pressed_keys[K_DOWN] else -1 if pressed_keys[K_DOWN] else fish_direction["Y"]

        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == self.button_keys['left_arrow']:
                self.fish_direction["LEFT"] = 1
            if event.button == self.button_keys['right_arrow']:
                self.fish_direction["RIGHT"] = 1
            if event.button == self.button_keys['down_arrow']:
                self.fish_direction["DOWN"] = 1
            if event.button == self.button_keys['up_arrow']:
                self.fish_direction["UP"] = 1

        if event.type == pygame.JOYBUTTONUP:
            print(event.button)
            if event.button == self.button_keys['left_arrow']:
                self.fish_direction["LEFT"] = 0
            if event.button == self.button_keys['right_arrow']:
                self.fish_direction["RIGHT"] = 0
            if event.button == self.button_keys['down_arrow']:
                self.fish_direction["DOWN"] = 0
            if event.button == self.button_keys['up_arrow']:
                self.fish_direction["UP"] = 0

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0 and (event.value > 0.2 or event.value < -0.2):
                self.fish_direction["X"] = event.value * 10
            if event.axis == 1 and (event.value > 0.2 or event.value < -0.2):
                self.fish_direction["Y"] = event.value * 10

            if event.axis == 0 and event.value > -0.2 and event.value < 0.2:
                self.fish_direction["X"] = 0
            if event.axis == 1 and event.value > -0.2 and event.value < 0.2:
                self.fish_direction["Y"] = 0

    def get_fish_direction(self):
        return self.fish_direction
