# -*- coding: utf-8 -*-
import csv
from db import *

import helpers



symbols = (u"аəбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
           u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}










with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:


        # print unicode(row[0], "utf-8").lower().translate(tr)
        # print unicode(row[1], "utf-8").lower().translate(tr)
        # print unicode(row[2], "utf-8").lower().translate(tr)


        Word.create(lex_form = helpers.trim_all(row[0]),
                    giperonim = helpers.trim_all(row[1]),
                    giponim = helpers.trim_all(row[2]),
                    meronim = helpers.trim_all(row[3]),
                    sinonim = helpers.trim_all(row[4]),
                    ontonim = helpers.trim_all(row[5]),
                    omonim = helpers.trim_all(row[6])
                    )


        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'