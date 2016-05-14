# -*- coding: utf-8 -*-

import csv
import re

with open('/home/naz/Desktop/Untitled Folder/xls/Улдана2-новый Тезаурус.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:

        # valid = re.match('^[\w-]+$', ' '.join(row)) is not None

        # if not valid:
        print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'