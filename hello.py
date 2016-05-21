# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import rdflib
from flask import render_template

import helpers
import sparql_helper

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'




# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id







@app.route('/_add_numbers', methods=['GET', 'POST'])
def add_numbers():
    a = request.form['a']
    b = request.form['b']
    return jsonify(result=a + b)







@app.route('/_get_collection', methods=['GET', 'POST'])
def get_collection():


    value = request.args.get('value')


    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-27#>



    SELECT ?x     ?y    ?z
            WHERE {
    ?x    my:lexical-form    ?z    FILTER regex( ?z, '^""" + value + """', 'i')  .

    }

     """)
    result = []

    for row in qres:
        print row.x
        print row.y
        print row.z
        result.append(row.z .encode('utf-8'))
        print '----------------------------------------------------------'



    return jsonify(result=result)











@app.route('/_get_item', methods=['GET', 'POST'])
def get_item():


    value = request.args.get('value')



    name = sparql_helper.by_lex_form_exact(value)




    arr =  sparql_helper.get_giperonims(name)



    giperonims_coll = []

    for word in arr:
        giperonims_coll.append(
            {
                'name': word,
                'lex_form': sparql_helper.get_lex_form(word)
            }
        )



    print '++++++++++++++++++++++++++++++='
    print  giperonims_coll



    return jsonify(result=giperonims_coll)











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

    PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-27#>



#      SELECT ?x     ?y    ?z   ?rel
#         WHERE {
# my:akparat-noun-1    my:has_giperonim    ?z     .
#
# ?z  my:lexical-form  ?rel .
#
# ?x     ?y    ?z  .
#
# }



SELECT ?x     ?y    ?z
        WHERE {
?x    ?y    ?z    FILTER regex( ?z, '^Ақп', 'i')  .

}



     """)
    data = ''

    for row in qres:
        print row.x
        print row.y
        print row.z
        data = row.z


    print 'xxxx'



    return render_template('hello2.html', name=name)



if __name__ == "__main__":
    app.debug = True
    app.run()