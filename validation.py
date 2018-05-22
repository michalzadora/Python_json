import shapes as sh
import re


def shape_validate(shape):
    shape = dict(shape)
    if 'type' in shape.keys():
        type = shape.get('type')
        if type == 'point' and all(fild in shape for fild in ('x', 'y')):
            return True
        elif type == 'polygon' and 'points' in shape:
            return True
        elif type == 'rectangle' and all(fild in shape for fild in ('x', 'y', 'width', 'height')):
            return True
        elif type == 'circle' and all(fild in shape for fild in ('x', 'y', 'radius')):
            return True
        elif type == 'square' and all(fild in shape for fild in ('x', 'y', 'size')):
            return True
        else:
            print("Wrong filds in: " + str(shape))
            return False
    else:
        print("No type in: " + str(shape))
        return False


def screen_palette_validate(screen, palette):
    if all(fild in screen for fild in ('width', 'height', 'bg_color', 'fg_color')) and \
            int(screen.get('width')) > 0 and int(screen.get('height')) > 0 and \
            colour_validate(screen.get('bg_color'), palette) and \
            colour_validate(screen.get('fg_color'), palette) and \
            all (colour_validate(colour, palette) for colour in palette.values()):
        return True
    else:
        print("No validation for screen or palette")
        return False


def colour_validate(colour, palette):
    if colour.startswith("#") and len(colour) == 7:
        return all(re.match('[0-9a-f]', number) for number in colour[1:])
    elif colour.startswith("(") and colour.endswith(")"):
        colour = tuple(map(int, re.findall('[0-9]{1,3}', colour)))
        if len(colour) == 3 and all(0 <= x <= 255 for x in colour):
            return True
        else:
            return False
    elif re.search('^[a-z]+$', colour) and colour in palette:
        return True
    else:
        return False
