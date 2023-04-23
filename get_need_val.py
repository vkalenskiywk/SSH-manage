import ctypes

def get_value(val_in):
    val_out = [v for v in val_in if v.isnumeric()]
    val_out = ''.join(val_out)
    return val_out

def get_str(val_in):
    val_out = [v for v in val_in if not(v.isnumeric())]
    val_out = ''.join(val_out)
    return val_out


def GetTextDimensions(text, points, font):
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)

    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))

    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)

    return size.cx, size.cy