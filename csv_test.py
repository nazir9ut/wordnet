# -*- coding: utf-8 -*-

import csv
import re



# аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя



symbols = (u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
           u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}


# text = u'Добрый День'
# print text.translate(tr)  # looks good




with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:

        # if not valid:
        str =  row[0].strip()


        print unicode(str, "utf-8").lower().translate(tr)



        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'