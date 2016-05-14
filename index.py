import rdflib

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



     SELECT ?x     ?y    ?z   ?rel
        WHERE {
my:akparat-noun-1    my:has_giperonim    ?z     .

?z  my:lexical-form  ?rel .

?x     ?y    ?z  .

}

       """)

for row in qres:
    # print(row.mer)
    # print(row.gip)
    # print row
    print row.x
    print row.y
    print row.z
    print row.rel