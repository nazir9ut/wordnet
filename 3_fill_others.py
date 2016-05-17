# -*- coding: utf-8 -*-

from db import *

import helpers


items = Word.select()

for item in items:
    # print item.id


    if item.giperonim_latin:

        arr_giperonim_latin = item.giperonim_latin.split('@')
        arr_giperonim = item.giperonim.split('@')

        for idx, word in enumerate(arr_giperonim_latin):
            # print word
            # print arr_giperonim[idx]


            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr_giperonim[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass


