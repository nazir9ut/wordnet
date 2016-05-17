# -*- coding: utf-8 -*-

from db import *

import helpers


items = Word.select()

for item in items:

    if item.giperonim_latin:

        arr_latin = item.giperonim_latin.split('@')
        arr = item.giperonim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass



    if item.giponim_latin:

        arr_latin = item.giponim_latin.split('@')
        arr = item.giponim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass




    if item.meronim_latin:

        arr_latin = item.meronim_latin.split('@')
        arr = item.meronim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass




    if item.sinonim_latin:

        arr_latin = item.sinonim_latin.split('@')
        arr = item.sinonim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass



    if item.ontonim_latin:

        arr_latin = item.ontonim_latin.split('@')
        arr = item.ontonim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass




    if item.omonim_latin:

        arr_latin = item.omonim_latin.split('@')
        arr = item.omonim.split('@')

        for idx, word in enumerate(arr_latin):

            exist = Word.select().where(Word.lex_form_latin == word).count() > 0


            if not exist:
                Word.create(lex_form = arr[idx],
                            lex_form_latin = word)
                # pass
            else:
                print word
                # pass


