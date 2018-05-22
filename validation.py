import shapes as sh
import re


def shape_validate(shape, screen):
    shape = dict(shape)
    if 'type' in shape.keys():
        type = shape.get('type')
        if type == 'point' and all(fild in shape for fild in ('x', 'y')) and \
                0 <= shape.get('x') <= screen.get('width') and \
                0 <= shape.get('y') <= screen.get('height'):
            return True
        elif type == 'polygon' and 'points' in shape:
            return True
        elif type == 'rectangle' and all(fild in shape for fild in ('x', 'y', 'width', 'height')) and \
                0 <= shape.get('x') <= screen.get('width') and \
                0 <= shape.get('y') <= screen.get('height') and \
                0 <= shape.get('width') and 0 <= shape.get('height'):
            return True
        elif type == 'circle' and all(fild in shape for fild in ('x', 'y', 'radius')) and \
                0 <= shape.get('x') <= screen.get('width') and \
                0 <= shape.get('y') <= screen.get('height') and \
                0 <= shape.get('radius'):
            return True
        elif type == 'square' and all(fild in shape for fild in ('x', 'y', 'size')) and \
                0 <= shape.get('x') <= screen.get('width') and \
                0 <= shape.get('y') <= screen.get('height') and \
                0 <= shape.get('size'):
            return True
        else:
            raise Exception("Wrong filds or wrong value in one of them in: " + str(shape))
    else:
        raise Exception("No type in: " + str(shape))


def screen_palette_validate(screen, palette):
    if all(fild in screen for fild in ('width', 'height', 'bg_color', 'fg_color')) and \
            int(screen.get('width')) > 0 and int(screen.get('height')) > 0 and \
            colour_validate(screen.get('bg_color'), palette) and \
            colour_validate(screen.get('fg_color'), palette) and \
            all(colour_validate(colour, palette) for colour in palette.values()):
        return True
    else:
        raise Exception("No validation for screen or palette")


def colour_validate(colour, palette):
    if colour.startswith("#") and len(colour) == 7:
        if all(re.match('[0-9a-f]', number) for number in colour[1:]):
            return True
        raise Exception("Problem with colour in HTML notification.")
    elif colour.startswith("(") and colour.endswith(")"):
        colour = tuple(map(int, re.findall('[0-9]{1,3}', colour)))
        if len(colour) == 3 and all(0 <= x <= 255 for x in colour):
            return True
        else:
            raise Exception("Problem with colour in RGB notification.")
    elif re.search('^[a-z]+$', colour) and colour in palette:
        return True
    else:
        raise Exception("Wrong colour in json, check it!")
