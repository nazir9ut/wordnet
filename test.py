# -*- coding: utf-8 -*-

from db import *

import helpers


str = 'Тəуекелді өңдеу'



items = Word.select()

# print

print helpers.cyr_to_latin(items[88].lex_form)