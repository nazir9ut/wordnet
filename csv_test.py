# -*- coding: utf-8 -*-
import csv




symbols = (u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя ",
           u"aabvggdeejziikqlmnnooprstuuufhhccwwiiiieyy_")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}


# text = u'Добрый День'
# print text.translate(tr)  # looks good




with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:


        print unicode(row[0].strip(), "utf-8").lower().translate(tr)
        print unicode(row[1].strip(), "utf-8").lower().translate(tr)
        print unicode(row[2].strip(), "utf-8").lower().translate(tr)



        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'