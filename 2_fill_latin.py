from db import *

import helpers




items = Word.select()

for item in items:
    print helpers.cyr_to_latin(item.lex_form)

    item.lex_form_latin = helpers.cyr_to_latin(item.lex_form)
    item.giperonim_latin = helpers.cyr_to_latin(item.giperonim)
    item.giponim_latin = helpers.cyr_to_latin(item.giponim)
    item.meronim_latin = helpers.cyr_to_latin(item.meronim)
    item.holonim_latin = helpers.cyr_to_latin(item.holonim)
    item.sinonim_latin = helpers.cyr_to_latin(item.sinonim)
    item.ontonim_latin = helpers.cyr_to_latin(item.ontonim)
    item.omonim_latin = helpers.cyr_to_latin(item.omonim)
    item.save()






