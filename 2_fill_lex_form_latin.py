from db import *

import helpers




items = Word.select()

for item in items:
    print helpers.cyr_to_latin(item.lex_form)

    item.lex_form_latin = helpers.cyr_to_latin(item.lex_form)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item. = helpers.cyr_to_latin(item.)
    item.save()


