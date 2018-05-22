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

        for content in self.contents:
            self.draw_content(content)
        self.graphic.show()

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
        drawer = ImageDraw.Draw(self.graphic)
        type_content = type(content)
        if type_content is shapes.Point:
            drawer.point([content.x, content.y], self.convert_to_RGB(content.colour))
        elif type_content is shapes.Rectangle:
            p1 = (content.x - (content.width / 2), content.y - (content.height / 2))
            p2 = (content.x + (content.width / 2), content.y + (content.height / 2))
            drawer.rectangle(list(p1 + p2), self.convert_to_RGB(content.colour))
        elif type_content is shapes.Square:
            p1 = (content.x - (content.side / 2), content.y - (content.side / 2))
            p2 = (content.x + (content.side / 2), content.y + (content.side / 2))
            drawer.rectangle(list(p1 + p2), self.convert_to_RGB(content.colour))
        elif type_content is shapes.Circle:
            p1 = (content.x - content.r, content.y - content.r)
            p2 = (content.x + content.r, content.y + content.r)
            drawer.ellipse(list(p1 + p2), self.convert_to_RGB(content.colour))
        elif type_content is shapes.Polygon:
            var = []
            [var.append((arg.x, arg.y)) for arg in content.points]
            drawer.polygon(var, self.convert_to_RGB(content.colour))
        else:
            print("Drawer cant recognize type to draw.")

    def save_as_png(self, output):
        self.graphic.save(output)