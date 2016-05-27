# -*- coding: utf-8 -*-

from db import *

import helpers


items = Word.select()

for item in items:


    base_url = 'http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-39'



    xml =  '<owl:NamedIndividual rdf:about="' + base_url + '#' + item.lex_form_latin + '">\n'




    xml += '<rdf:type rdf:resource="' + base_url + '#zat_esim"/>\n'




    if item.giperonim_latin:
        arr = item.giperonim_latin.split('@')

        for word in arr:
            xml += '<has_giperonim rdf:resource="' + base_url + '#' +  word + '"/>\n'






    if item.giponim_latin:
        arr = item.giponim_latin.split('@')

        for word in arr:
            xml += '<has_giponim rdf:resource="' + base_url + '#' +  word + '"/>\n'






    if item.meronim_latin:
        arr = item.meronim_latin.split('@')

        for word in arr:
            xml += '<has_meronim rdf:resource="' + base_url + '#' +  word + '"/>\n'





    if item.holonim_latin:
        arr = item.holonim_latin.split('@')

        for word in arr:
            xml += '<has_holonim rdf:resource="' + base_url + '#' +  word + '"/>\n'





    if item.sinonim_latin:
        arr = item.sinonim_latin.split('@')

        for word in arr:
            xml += '<has_sinonim rdf:resource="' + base_url + '#' +  word + '"/>\n'





    if item.ontonim_latin:
        arr = item.ontonim_latin.split('@')

        for word in arr:
            xml += '<has_ontonim rdf:resource="' + base_url + '#' +  word + '"/>\n'






    if item.omonim_latin:
        arr = item.omonim_latin.split('@')

        for word in arr:
            xml += '<has_omonim rdf:resource="' + base_url + '#' +  word + '"/>\n'






    if item.lex_form:
        xml += '<lexical-form>' + unicode(item.lex_form.encode('utf-8'), "utf-8") + '</lexical-form>'




    if item.description:
        xml += '<description>' + unicode(item.description.encode('utf-8'), "utf-8") + '</description>'





    xml += '</owl:NamedIndividual>'




    item.xml = xml
    item.save()




    print item.lex_form_latin
