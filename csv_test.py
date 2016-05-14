# -*- coding: utf-8 -*-

import csv
import re




symbols = (u"",
           u"")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}


text = u'Добрый Ден'
print text.translate(tr)  # looks good




with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:

        # valid = re.match('^[\w-]+$', ' '.join(row)) is not None

        # if not valid:
        str =  row[0].strip()

        str = unicode(str, "utf-8")

        print str.lower()

        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'