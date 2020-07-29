from pygame.rect import Rect


class Tile:
    def __init__(self, x_pos, y_pos, x_length, y_length, image_path, effects):
        self._x_length = x_length
        self._y_length = y_length
        self.rect = Rect(x_pos, y_pos, x_length, y_length)
        self.image_path = image_path
        self.effects = effects

    def getImagePath(self):
        return self.image_path

    def getRect(self):
        return self.rect

    def getEffects(self):
        return self.effects
