DEFAULT_CHARSET = list("1iohajhduakshd@#$%?*+=-:.")

def pixel_to_char(r, g, b):
    brightness = (r + g + b) / 3
    charset = DEFAULT_CHARSET
    index = int((brightness / 255) * (len(charset) - 1))
    return charset[index]