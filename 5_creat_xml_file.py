# -*- coding: utf-8 -*-

from db import *

import helpers


items = Word.select()






f = open('ontology.owl', 'r+')
f.truncate()

for item in items:

    print item.lex_form_latin

    with open('ontology.owl', 'a') as the_file:
        the_file.write(item.xml + '\n\n\n\n')
