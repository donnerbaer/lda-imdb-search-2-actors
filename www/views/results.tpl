% rebase('base.tpl')
% devMode = False


<a href="/" class="btn btn-primary rounded-0">Zurück</a> 



<%

if len(person_1['results']['bindings']) > 0 and len(person_2['results']['bindings']) > 0:
    person_1 = person_1['results']['bindings'][0]
    person_2 = person_2['results']['bindings'][0]

%>



<div class="position-sticky">
    <div class="position-absolute top-0 start-50 translate-middle-x">
        <div class="row">
            <div class="card m-3" style="width: 18rem;">
                %# <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{person_1['personLabel']['value']}}</h5>

                    <% 
                    if 'birthYear' in person_1.keys():
                        birthYear = person_1['birthYear']['value']
                    else:
                        birthYear = ""
                    end

                    if 'deathYear' in person_1.keys():
                        deathYear = person_1['deathYear']['value']
                    else:
                        deathYear = ""
                    end
                    %>            

                    <p>Year of birth: {{ birthYear }}<br>
                    Year of death: {{ deathYear }}</p>
                    <a href="https://www.imdb.com/name/{{person_1['person']['value'][32:]}}" target="_blank" class="btn btn-primary rounded-0">IMDB</a>
                </div>
            </div>


            <div class="card m-3" style="width: 18rem;">
                %# <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{person_2['personLabel']['value']}}</h5>

                    <% 
                    if 'birthYear' in person_2.keys():
                        birthYear = person_2['birthYear']['value']
                    else:
                        birthYear = ""
                    end

                    if 'deathYear' in person_2.keys():
                        deathYear = person_2['deathYear']['value']
                    else:
                        deathYear = ""
                    end
                    %>

                    <p>Year of birth: {{ birthYear }}<br>
                    Year of death: {{ deathYear }}</p>
                    <a href="https://www.imdb.com/name/{{person_2['person']['value'][32:]}}" target="_blank" class="btn btn-primary rounded-0">IMDB</a>
                </div>
            </div>
        </div>
    </div>
</div>



<div class="" style="padding-top:220px;">

    % if devMode == True:

    <pre>
        {{data}}
    </pre>
    <pre>
        {{person_1}}
    </pre>
    <pre>
        {{person_2}}
    </pre>

    % end

    <table class="table table-light table-striped">
        <thead>
            <tr>
                % if devMode == True: 
                <th>rawData</th>
                % end
                <th>Title</th>
                <th>Start Year</th>
                <th>End Year</th>
                <th>runtimeMinutes</th>
                <th>genres</th>
            </tr>
        </thead>


        <tbody class="">
        % for entry in data['results']['bindings']:
            <tr class="my-3">
                % if devMode == True:
                <td> {{entry}} </td>
                % end
                <td> <a href="https://www.imdb.com/title/{{entry['movie']['value'][32:]}}" target="_blank"> {{entry['movieLabel']['value']}} </a> </td>
                
                
                <% 
                    if 'startYear' in entry.keys():
                        startYear = entry['startYear']['value']
                    else:
                        startYear = ""
                    end
                %>                
                <td>{{ startYear }}</td>



                <% 
                    if 'endYear' in entry.keys():
                        endYear = entry['endYear']['value']
                    else:
                        endYear = ""
                    end
                %>                
                <td>{{ endYear }}</td>



                <% 
                    if 'runtimeMinutes' in entry.keys():
                        runtimeMinutes = entry['runtimeMinutes']['value']
                    else:
                        runtimeMinutes = ""
                    end
                %>                
                <td>{{ runtimeMinutes }}</td>



                <% 
                    if 'genres' in entry.keys():
                        genres = entry['genres']['value']
                        genres = genres.replace("http://www.example.com/sis/lda/imdb/","")
                        genres = genres.replace(" ",", ")
                    else:
                        genres = ""
                    end
                %>                
                <td>{{ genres }}</td>
            </tr>
        % end
        </table>

</div>


% end # end of if from top