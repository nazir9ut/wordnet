# -*- coding: utf-8 -*-
import csv
from db import *



symbols = (u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
           u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}










with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:


        print unicode(row[0].strip(), "utf-8").lower().translate(tr)
        print unicode(row[1].strip(), "utf-8").lower().translate(tr)
        print unicode(row[2].strip(), "utf-8").lower().translate(tr)


        Word.create(lex_form = row[0].strip(),
                    giperonim = row[1].strip(),
                    giponim = row[2].strip(),
                    meronim = row[3].strip(),
                    sinonim = row[4].strip(),
                    ontonim = row[5].strip(),
                    omonim = row[6].strip())


        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'