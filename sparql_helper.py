# -*- coding: utf-8 -*-

import rdflib



def get_header():

    result = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    PREFIX my: <http://www.semanticweb.org/naz/ontologies/2016/4/untitled-ontology-27#>
    """

    return result




def get_clean(url):
    return url.split('#')[-1]






def by_lex_form_exact(value):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
        SELECT ?x     ?y    ?z
        WHERE {
            ?x    my:lexical-form    ?z    FILTER regex( ?z, '^""" + value + """$', 'i')  .
        }

     """)

    arr = []

    for row in qres:
        arr.append(row.x.encode('utf-8'))



    if len(arr) > 0:
        result = get_clean(arr[0])
    else:
        result = None



    return result









def get_giperonims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_giperonim    ?z     .

            }

     """)

    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result





def get_giponims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_giponim    ?z     .

            }

     """)

    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result














def get_meronims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_meronim    ?z     .

            }

     """)


    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result














def get_sinonims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_sinonim    ?z     .

            }

     """)


    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result




















def get_omonims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_omonim    ?z     .

            }

     """)


    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result



















def get_ontonims(inst_name):

    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z   ?rel
            WHERE {
            my:""" + inst_name + """    my:has_ontonim    ?z     .

            }

     """)


    arr = []

    for row in qres:
        arr.append(get_clean(row.z))


    result = arr

    return result











def get_lex_form(inst_name):
    g = rdflib.Graph()

    # ... add some triples to g somehow ...
    g.parse("/home/naz/Desktop/101.owl")

    qres = g.query(
        get_header() +
        """
             SELECT ?x     ?y    ?z
            WHERE {
            my:""" + inst_name + """    my:lexical-form    ?z     .

            }

     """)



    arr = []


    for row in qres:
        arr.append(row.z.encode('utf-8'))



    if len(arr) > 0:
        result = arr[0]
    else:
        result = None



    return get_clean(result)