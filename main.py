import argparse
import json
import re
import shapes as sh
import graphic
import validation


def reader(path):
    # Using with open to better  automatical close file
    with open(path) as file:
        data = json.load(file)
    return data


def divine(text, file):
    if text in file:
        return file[text]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="path to json file")
    # If we have option -o or --output we have to check if next arg is path to output
    parser.add_argument("-o", "--output", type=str, help="option to save graphic to file")
    args = parser.parse_args()

    # Read from json file and divine it for major parts (Figures, Screen, Palette)
    file = reader(args.input)
    screen = dict(divine('Screen', file))
    palette = dict(divine('Palette', file))
    if not validation.screen_palette_validate(screen, palette):
        return
    # making list of figures and making each figure to be a dict and if color is None
    contents = list(divine('Figures', file))
    i = 0
    while (i < len(contents)):
        contents[i] = dict(contents[i])
        # VALIDATION OF FIGURES
        validation.shape_validate(contents[i])
        if not contents[i].__contains__('color'):
            contents[i]['color'] = screen.get('fg_color')
        else:
            if not validation.colour_validate(contents[i]['color'], palette):
                return
        i += 1

    # Making instance of shapes to easily draw
    shapes_to_draw = []
    for c in contents:
        if c.get('type') == 'point':
            shapes_to_draw.append(sh.Point(c.get('x'), c.get('y'),
                                           c.get('color')))

        elif c.get('type') == 'rectangle':
            shapes_to_draw.append(sh.Rectangle(c.get('x'), c.get('y'),
                                               c.get('width'), c.get('height'),
                                               c.get('color')))

        elif c.get('type') == 'square':
            shapes_to_draw.append(sh.Square(c.get('x'), c.get('y'), c.get('size'),
                                            c.get('color')))

        elif c.get('type') == 'circle':
            shapes_to_draw.append(sh.Circle(c.get('x'), c.get('y'), c.get('radius'),
                                            c.get('color')))

        elif c.get('type') == 'polygon':
            shapes_to_draw.append(sh.Polygon(c.get('points'),
                                             c.get('color')))

    # if screen.keys().__contains__('bg_color' and 'fg_color'):
    # if (screen['bg_color'] and screen['fg_color']) in palette.keys():

    a = graphic.Graphic(shapes_to_draw, screen, palette)
    a.make_graphic()


if __name__ == "__main__":
    main()
