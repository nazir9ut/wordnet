# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import rdflib
from flask import render_template
import json

import helpers
import sparql_helper

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')








# @app.route('/_add_numbers', methods=['GET', 'POST'])
# def add_numbers():
#     a = request.form['a']
#     b = request.form['b']
#     return jsonify(result=a + b)









@app.route('/_get_collection', methods=['GET', 'POST'])
def get_collection():


    term = request.args.get('term')


    g = rdflib.Graph()

    g.parse(sparql_helper.owl_file())

    qres = g.query(
        """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-39#>


        SELECT ?x     ?y    ?z
                WHERE {
                    ?x    my:lexical-form    ?z    FILTER regex( ?z, '^""" + term + """', 'i')  .
                }

     """)


    result = []


    for row in qres:
        instance_name = sparql_helper.get_clean(row.x.encode('utf-8'))

        is_zatesim = sparql_helper.is_zatesim(instance_name, g)






        obj = {
            'id': row.x.encode('utf-8'),
            'label': row.z.encode('utf-8'),
            'is_zatesim': is_zatesim
        }

        result.append(obj)
        print '----------------------------------------------------------'





    # return jsonify(result=result)
    return json.dumps(result)











@app.route('/_get_item', methods=['GET', 'POST'])
def get_item():


    g = rdflib.Graph()

    g.parse(sparql_helper.owl_file())



    value = request.args.get('value')






    name = sparql_helper.by_lex_form_exact(value, g)





    giperonims_coll = []
    giponims_coll = []
    holonims_coll = []
    meronims_coll = []
    sinonims_coll = []
    omonims_coll = []
    ontonims_coll = []
    aniktama = ''





    if name:



        arr =  sparql_helper.get_giperonims(name, g)

        for word in arr:
            if word:
                giperonims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )








        arr =  sparql_helper.get_giponims(name, g)

        for word in arr:
            if word:
                giponims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )








        arr =  sparql_helper.get_holonims(name, g)

        for word in arr:
            if word:
                holonims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )





        arr =  sparql_helper.get_meronims(name, g)

        for word in arr:
            if word:
                meronims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )





        arr =  sparql_helper.get_sinonims(name, g)

        for word in arr:
            if word:
                sinonims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )





        arr =  sparql_helper.get_omonims(name, g)

        for word in arr:
            if word:
                omonims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )





        arr =  sparql_helper.get_ontonims(name, g)

        for word in arr:
            if word:
                ontonims_coll.append(
                    {
                        'name': word,
                        'lex_form': sparql_helper.get_lex_form(word, g),
                        'is_zatesim': sparql_helper.is_zatesim(word, g)
                    }
                )








        aniktama = sparql_helper.get_descr(name, g)




        is_zatesim = sparql_helper.is_zatesim(name, g)







    return jsonify(
        giperonims_coll = giperonims_coll,
        giponims_coll = giponims_coll,
        holonims_coll = holonims_coll,
        meronims_coll = meronims_coll,
        sinonims_coll = sinonims_coll,
        omonims_coll = omonims_coll,
        ontonims_coll = ontonims_coll,
        aniktama = aniktama,
        is_zatesim = is_zatesim
    )




















# @app.route('/hello2')
# def hello2():

    # g = rdflib.Graph()
    #
    # # ... add some triples to g somehow ...
    # g.parse("/home/naz/Desktop/101.owl")
    #
    # qres = g.query(
    #     """
    #     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    #     PREFIX owl: <http://www.w3.org/2002/07/owl#>
    #     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    #     PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    #
    #     PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-39#>
    #
    #
    #
    #     SELECT ?x     ?y    ?z
    #             WHERE {
    #                 ?x    ?y    ?z    FILTER regex( ?z, '^Ақп', 'i')  .
    #
    #             }
    #
    #  """)
    #
    # for row in qres:
    #     print row.x
    #     print row.y
    #     print row.z


    # return render_template('hello2.html')



if __name__ == "__main__":
    app.debug = True
    app.run()