# -*- coding: utf-8 -*-
import csv
from db import *

import helpers



# symbols = (u"аəбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
#            u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")
#
# tr = {ord(a):ord(b) for a, b in zip(*symbols)}










with open('/home/naz/Desktop/wordnet/xls2/НОВЫЙ Тезаурус (1).csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:

        # print unicode(row[0], "utf-8").lower().translate(tr)
        # print unicode(row[1], "utf-8").lower().translate(tr)
        # print unicode(row[2], "utf-8").lower().translate(tr)

        # print row[1]

        Word.create(
            lex_form = helpers.trim_all(row[0]),

            description = helpers.trim_all(row[1]),

            giperonim = helpers.trim_all(row[2]),

            giponim = helpers.trim_all(row[3]),

            holonim = helpers.trim_all(row[4]),

            sinonim = helpers.trim_all(row[5]),

            ontonim = helpers.trim_all(row[6]),

            omonim = helpers.trim_all(row[7]),

            meronim = helpers.trim_all(row[8])
        )


        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'