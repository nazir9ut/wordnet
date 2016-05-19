# -*- coding: utf-8 -*-

def cyr_to_latin(str):


    symbols = (u"аəбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ә",
               u"aobvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_o")

    tr = {ord(a):ord(b) for a, b in zip(*symbols)}

    # result = unicode(str.strip(), "utf-8").lower().translate(tr)
    result = str.strip().lower().translate(tr)

    return result








def trim_all(str):

    result = str.strip()\
        .replace("@ ", "@")\
        .replace("@ ", "@")\
        .replace("@ ", "@")\
        .replace(" @", "@")\
        .replace(" @", "@")\
        .replace(" @", "@")

    return result





def to_unicode(str):
    result = unicode(str.encode('utf-8'), "utf-8")

    return result

