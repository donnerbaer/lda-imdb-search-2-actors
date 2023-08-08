from bottle import route, run
from bottle import get, static_file, template, request
import graphdb


endpoint_url = "http://example.com:7200/repositories/LDApps" 
username = ""
password = ""
GDB = graphdb.GraphDB(endpoint_url, username, password)





@route('/')
def index():
    return template('index')


@route('/results', method="get")
def results():
    query = request.query_string 
    query_params = query.split('&')
    params_dict = {}

    for param in query_params:
        key, value = param.split('=')
        value = value.replace('+', ' ')
        params_dict[key] = value
        
    data = GDB.find_movies(person_1=params_dict['person_1'], person_2=params_dict['person_2'])
    person_1 = GDB.getPersonData(params_dict['person_1'])
    person_2 = GDB.getPersonData(params_dict['person_2'])
    return template('results', data=data, person_1 = person_1, person_2 = person_2)



@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")



if __name__ == '__main__':
    run(host="localhost", port="80", reloader=True, debug=True)