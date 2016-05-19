from db import *

import helpers


items = Word.select()

for item in items:


    base_url = 'http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-27'



    xml =  '<owl:NamedIndividual rdf:about="' + base_url + '#' + item.lex_form_latin + '">\n'




    xml += '<rdf:type rdf:resource="' + base_url + '#zatesim"/>\n'




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




    xml += '</owl:NamedIndividual>'




    item.xml = xml
    item.save()




    print item.lex_form_latin
