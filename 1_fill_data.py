# -*- coding: utf-8 -*-
import csv
from db import *

import helpers





with open('/home/naz/Desktop/wordnet/xls2/НОВЫЙ Тезаурус (1).csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in spamreader:


        Word.create(
            lex_form = helpers.trim_all(row[0]),

            description = helpers.trim_all(row[1]),

            giperonim = helpers.trim_all(row[2]),

            giponim = helpers.trim_all(row[3]),

            holonim = helpers.trim_all(row[4]),

            sinonim = helpers.trim_all(row[5]),

            ontonim = helpers.trim_all(row[6]),

            omonim = helpers.trim_all(row[7]),

            meronim = helpers.trim_all(row[8]),

            is_zatesim = True
        )


        # print ' '.join(row)
        print '--------------------------------------------------------------------------------------------------------------'