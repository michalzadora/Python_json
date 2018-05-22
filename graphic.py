import shapes
import re
from PIL import Image, ImageColor, ImageDraw


class Graphic:
    def __init__(self, contents, screen, palette):
        self.contents = contents
        self.screen = dict(screen)
        self.palette = dict(palette)
        self.graphic = None

    def make_graphic(self):
        self.graphic = Image.new('RGB', (self.screen['width'], self.screen.get('height')),
                                 self.convert_to_RGB(self.screen.get('bg_color')))
        self.graphic.show()
        for content in self.contents:
            self.draw_content(content)

    def convert_to_RGB(self, colour):
        # start with word representation and match it with palette:
        if colour in self.palette.keys():
            colour = self.palette.get(colour)
        # now HTML notatation
        if str(colour).startswith('#'):
            return ImageColor.getrgb(colour)
        # and last we have change string RGB to tuple
        elif str(colour).startswith('('):
            return tuple(map(int, re.findall('[0-9]{1,3}', colour)))

    def draw_content(self, content):
        # TODO pick good def
        drawer = ImageDraw.Draw(self.graphic)
        pass
