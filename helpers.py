# -*- coding: utf-8 -*-

def cyr_to_latin(str):


    symbols = (u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
               u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")

    tr = {ord(a):ord(b) for a, b in zip(*symbols)}

    # result = unicode(str.strip(), "utf-8").lower().translate(tr)
    result = str.strip().lower().translate(tr)

    return result