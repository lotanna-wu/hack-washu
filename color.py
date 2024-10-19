import colorsys

def rgb_to_hsv(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h = h * 360
    s = s * 100
    v = v * 100

    return h, s, v

def hsv_to_rgb(h, s, v):
    h /= 360.0
    s /= 100.0
    v /= 100.0

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    return r, g, b