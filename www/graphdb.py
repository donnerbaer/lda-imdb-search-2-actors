from SPARQLWrapper import SPARQLWrapper, JSON

class GraphDB:
    def __init__(self, endpoint_url, username, password):
        self.endpoint_url = endpoint_url
        self.username = username
        self.password = password

    def execute_query(self, sparql_query:str) -> list[dict]:
        sparql = SPARQLWrapper(self.endpoint_url)
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        sparql.setCredentials(self.username, self.password)

        try:
            results = sparql.query().convert()
            return results
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


    def find_movies(self, person_1:str, person_2:str) -> list[dict]:
        """_summary_

        Args:
            person_1 (_type_): _description_
            person_2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        """
        tconst  titleType       primaryTitle    originalTitle   isAdult startYear       endYear runtimeMinutes  genres
        tt0000001       short   Carmencita      Carmencita      0       1894    N      1       Documentary,Short
        tt0000002       short   Le clown et ses chiens  Le clown et ses chiens  0       1892    N      5       Animation,Short
        tt0000003       short   Pauvre Pierrot  Pauvre Pierrot  0       1892    N      4       Animation,Comedy,Romance
        tt0000004       short   Un bon bock     Un bon bock     0       1892    N      12      Animation,Short
        """
        sparql_query = '''
            PREFIX imdb: <http://www.example.com/sis/lda/imdb/>
            SELECT 
            ?movie
            ?movieLabel
            ?startYear
            ?endYear
            ?runtimeMinutes
            ?genres
            (group_concat(?genres) as ?genres)
            WHERE{
                ?person_1 imdb:primaryName "''' + person_1 + '''" .
                ?person_1 imdb:primaryName ?person_1Label .
                ?movie imdb:hasInvolved ?person_1 .
                ?movie imdb:originalTitle ?movieLabel .
                ?person_2 imdb:primaryName "''' + person_2 + '''" .
                ?person_2 imdb:primaryName ?person_2Label .
                ?movie imdb:hasInvolved ?person_2 .
                OPTIONAL { ?movie imdb:startYear ?startYear . }
                OPTIONAL { ?movie imdb:endYear ?endYear . }
                OPTIONAL { ?movie imdb:runtimeMinutes ?runtimeMinutes . }
                OPTIONAL { ?movie imdb:genres ?genres . }
            } GROUP BY (?movie) (?movieLabel) (?startYear) (?endYear) (?runtimeMinutes)
            ORDER BY ?movie
            '''        
        return self.execute_query(sparql_query)

        
    def getPersonData(self, person:str) -> list[dict]:
        """
        imdb:nm0000001 imdb:primaryName "Fred Astaire";
        imdb:birthYear "1899"^^xsd:date;
        imdb:deathYear "1987"^^xsd:date;
        imdb:primaryProfession imdb:soundtrack,
        imdb:actor,
        imdb:miscellaneous;
        imdb:knownForTitles imdb:tt0072308,
        imdb:tt0053137,
        imdb:tt0050419,
        imdb:tt0031983.
        """	
        sparql_query = '''
            PREFIX imdb: <http://www.example.com/sis/lda/imdb/>
            SELECT 
            *
            WHERE{
                ?person imdb:primaryName "''' + person + '''" .
                ?person imdb:primaryName ?personLabel .
                OPTIONAL { ?person imdb:birthYear ?birthYear .}
                OPTIONAL { ?person imdb:deathYear ?deathYear . }
            }
            '''
        return self.execute_query(sparql_query)
    
    
    def getAllPersons(self) -> list[dict]:
        """ select all person in graphDB

        Returns:
            list[dict]: all persons
        """
        
        sparql_query = '''
            PREFIX imdb: <http://www.example.com/sis/lda/imdb/>
            SELECT 
            ?personLabel
            WHERE{
                ?person imdb:primaryName ?personLabel .
            } ORDER BY ?personLabel
        '''
        return self.execute_query(sparql_query)
    
    