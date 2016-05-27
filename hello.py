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
    return 'Index Page'








@app.route('/_add_numbers', methods=['GET', 'POST'])
def add_numbers():
    a = request.form['a']
    b = request.form['b']
    return jsonify(result=a + b)







@app.route('/_get_collection', methods=['GET', 'POST'])
def get_collection():


    term = request.args.get('term')


    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

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
        print row.x
        print row.y
        print row.z

        obj = {
            'id': row.x.encode('utf-8'),
            'label': row.z.encode('utf-8'),
            'value': row.z.encode('utf-8')
        }

        result.append(obj)
        print '----------------------------------------------------------'





    # return jsonify(result=result)
    return json.dumps(result)











@app.route('/_get_item', methods=['GET', 'POST'])
def get_item():


    value = request.args.get('value')



    name = sparql_helper.by_lex_form_exact(value)

    giperonims_coll = []
    giponims_coll = []
    holonims_coll = []
    meronims_coll = []
    sinonims_coll = []
    omonims_coll = []
    ontonims_coll = []





    if name:

        arr =  sparql_helper.get_giperonims(name)

        for word in arr:
            giperonims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )





        arr =  sparql_helper.get_giponims(name)

        for word in arr:
            giponims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )








        arr =  sparql_helper.get_holonims(name)

        for word in arr:
            holonims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )





        arr =  sparql_helper.get_meronims(name)

        for word in arr:
            meronims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )





        arr =  sparql_helper.get_sinonims(name)

        for word in arr:
            sinonims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )





        arr =  sparql_helper.get_omonims(name)

        for word in arr:
            omonims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )





        arr =  sparql_helper.get_ontonims(name)

        for word in arr:
            ontonims_coll.append(
                {
                    'name': word,
                    'lex_form': sparql_helper.get_lex_form(word)
                }
            )










    return jsonify(
        giperonims_coll = giperonims_coll,
        giponims_coll = giponims_coll,
        meronims_coll = meronims_coll,
        sinonims_coll = sinonims_coll,
        omonims_coll = omonims_coll,
        ontonims_coll = ontonims_coll
    )




















@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-39#>



    SELECT ?x     ?y    ?z
            WHERE {
    ?x    ?y    ?z    FILTER regex( ?z, '^Ақп', 'i')  .

    }

     """)

    for row in qres:
        print row.x
        print row.y
        print row.z






    return render_template('hello2.html', name=name)



if __name__ == "__main__":
    app.debug = True
    app.run()