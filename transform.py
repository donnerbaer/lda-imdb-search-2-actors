import os


def transformNameBasics() -> None:
    """
    nconst  primaryName     birthYear       deathYear       primaryProfession       knownForTitles
    nm0000001       Fred Astaire    1899    1987    soundtrack,actor,miscellaneous  tt0053137,tt0050419,tt0045537,tt0072308
    nm0000002       Lauren Bacall   1924    2014    actress,soundtrack      tt0117057,tt0037382,tt0038355,tt0075213
    nm0000003       Brigitte Bardot 1934    N      actress,soundtrack,music_department     tt0054452,tt0057345,tt0049189,tt0056404
    nm0000004       John Belushi    1949    1982    actor,soundtrack,writer tt0078723,tt0080455,tt0077975,tt0072562
    """
    with open('data/unzipped/name.basics.tsv', encoding='UTF-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
    print ("Founded Entries: " + str(line_count))

    #input file
    fileTSV = open("data/unzipped/name.basics.tsv", "r", encoding='UTF-8')
    # output file
    fileTTL = open("data/transformed/name.basic.ttl","w", encoding='UTF-8')


    fileTTL.write("@prefix imdb: <http://www.example.com/sis/lda/imdb/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
    #for _ in range(0,100,1):
        line = fileTSV.readline()
        line = line[:-1]
        line = line.split('\t')
        
        line[4] = line[4].split(',')
        line[5] = line[5].split(',')

        output = "imdb:" + line[0] + ' imdb:primaryName' + ' "' + line[1] + '";\n'
        if '\\N' not in line[2]:
            output = output + 'imdb:birthYear "' + line[2] + '"^^xsd:date;\n'
        if '\\N' not in line[3]:
            output = output + 'imdb:deathYear "' + line[3] + '"^^xsd:date;\n'

        if line[4][0] != '\\' and line[4][0] != '' and line[4][0] != '\\N' and line[4][0] != None: 
            job = 'imdb:primaryProfession '
            for j in line[4]:
                job = job + 'imdb:' + j + ',\n'
            job = job[:-2]
            job = job + ';\n'
            output = output + job

        if line[5][0] != '\\' and line[5][0] != '' and line[5][0] != '\\N' and line[5][0] != None: 
            knownFor = 'imdb:knownForTitles '
            for k in line[5]:
                knownFor = knownFor + 'imdb:' + k + ',\n'
            knownFor = knownFor[:-2]
            knownFor = knownFor + '.\n'
            output = output + knownFor

        output = output[:-2]
        output = output + '.\n'
        fileTTL.write(output)

    fileTSV.close()
    fileTTL.close()




def transformTitleBasics() -> None:
    """
    tconst  titleType       primaryTitle    originalTitle   isAdult startYear       endYear runtimeMinutes  genres
    tt0000001       short   Carmencita      Carmencita      0       1894    N      1       Documentary,Short
    tt0000002       short   Le clown et ses chiens  Le clown et ses chiens  0       1892    N      5       Animation,Short
    tt0000003       short   Pauvre Pierrot  Pauvre Pierrot  0       1892    N      4       Animation,Comedy,Romance
    tt0000004       short   Un bon bock     Un bon bock     0       1892    N      12      Animation,Short
    """
    with open('data/unzipped/title.basics.tsv', encoding='UTF-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
    print ("Founded Entries: " + str(line_count))

    # input file
    fileTSV = open("data/unzipped/title.basics.tsv", "r", encoding='UTF-8')
    # output file
    fileTTL = open("data/transformed/title.basics.ttl","w", encoding='UTF-8')

    fileTTL.write("@prefix imdb: <http://www.example.com/sis/lda/imdb/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
        line = fileTSV.readline()
        line = line[:-1]
        line = line.split('\t')
        
        line[8] = line[8].split(',')

        output = "imdb:" + line[0] + ' imdb:titleType' + ' "' + line[1] + '";\n'
        if '\\N' not in line[2]:
            output = output + 'imdb:primaryTitle "' + line[2] + '";\n'
        if '\\N' not in line[3]:
            output = output + 'imdb:originalTitle "' + line[3] + '";\n'
        if '\\N' not in line[4]:
            output = output + 'imdb:isAdult ' + line[4] + '^^xsd:integer;\n'
        if '\\N' not in line[5]:
            output = output + 'imdb:startYear "' + line[5] + '"^^xsd:date;\n'
        if '\\N' not in line[6]:
            output = output + 'imdb:endYear "' + line[6] + '"^^xsd:date;\n'
        if '\\N' not in line[7]:
            output = output + "imdb:runtimeMinutes " + line[7] + '^^xsd:integer;\n'
        if line[8][0] != '\\' and line[8][0] != '' and line[8][0] != '\\N' and line[8][0] != None: 
            genre = 'imdb:genres '
            for g in line[8]:
                genre = genre + 'imdb:' + g + ',\n'
            genre = genre[:-2]
            genre = genre + '.\n'
            output = output + genre
      
        output = output[:-2]
        output = output + '.\n'
        fileTTL.write(output)

    fileTSV.close()
    fileTTL.close()



def transformTitleCrew() -> None:
    """
    tconst  directors       writers
    tt0000001       nm0005690       N
    tt0000002       nm0721526       N
    tt0000003       nm0721526       N
    tt0000004       nm0721526       N
    """
    with open('data/unzipped/title.crew.tsv', encoding='UTF-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
        
        
        print ("Founded Entries: " + str(line_count))

        # input file
        fileTSV = open("data/unzipped/title.crew.tsv", "r", encoding='UTF-8')
        # output file
        fileTTL = open("data/transformed/title.crew.ttl","w", encoding='UTF-8')

        fileTTL.write("@prefix imdb: <http://www.example.com/sis/lda/imdb> .\n")

        # head / row names
        fileTSV.readline()
        
        for _ in range(0,line_count-1,1):
            line = fileTSV.readline()
            line = line[:-1]
            line = line.split('\t')
            line[1] = line[1].split(',')
            line[2] = line[2].split(',')
            
            output = "imdb:" + line[0] + " " 
            if line[1][0] != '\\' and line[1][0] != '' and line[1][0] != '\\N' and line[1][0] != None: 
                directors = 'imdb:directors '
                for d in line[1]:
                    directors = directors + ' imdb:' + d + ',\n'
                directors = directors[:-2]
                directors = directors + ';\n'
                output = output + directors

            if line[2][0] != '\\' and line[2][0] != '' and line[2][0] != '\\N' and line[2][0] != None: 
                writers = 'imdb:writers '
                for w in line[1]:
                    writers = writers + ' imdb:' + w + ',\n'
                writers = writers[:-2]
                writers = writers + ';\n'
                output = output + writers
        
            output = output[:-2]
            output = output + '.\n'
            fileTTL.write(output)

        fileTSV.close()
        fileTTL.close()

    

def transformTitlePrincipals() -> None:
    """
    tconst  ordering        nconst  category        job     characters
    tt0000001       1       nm1588970       self    N      ["Self"]
    tt0000001       2       nm0005690       director        N      N
    tt0000001       3       nm0374658       cinematographer director of photography N
    tt0000002       1       nm0721526       director        N      N
    """
    with open('data/unzipped/title.principals.tsv', encoding='UTF-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
            

    print ("Founded Entries: " + str(line_count))

    # input file
    fileTSV = open("data/unzipped/title.principals.tsv", "r", encoding='UTF-8')
    # output file
    fileTTL = open("data/transformed/title.principals.ttl","w", encoding='UTF-8')

    fileTTL.write("@prefix imdb: <http://www.example.com/sis/lda/imdb/> .\n")
    fileTTL.write("@prefix principals: <http://www.example.com/sis/lda/imdb/principals/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
        line = fileTSV.readline()
    
        line = line[:-1]
        line = line.split('\t')
        
        output = "imdb:" + line[0] + ' imdb:hasInvolved' + ' imdb:' + line[2] + ';\n'
        if '\\N' not in line[3]:
            output = output + 'imdb:category ' + 'imdb:' + line[3] + ';\n'
            
        if '\\N' not in line[4]:
            output = output + 'imdb:job' + ' imdb:' + line[4] + ';\n'
            
        if line[5][0] != '\\' and line[5][0] != '' and line[5][0] != '\\N' and line[5][0] != None: 
            line[5] = eval(line[5])
            characters = 'imdb:characters '
            for c in line[5]:
                characters = characters + '"' + c + '",\n'
            characters = characters[:-2]
            characters = characters + ';\n'
            output = output + characters
            
       
        output = output[:-2]
        output = output + '.\n'
        fileTTL.write(output)

    fileTSV.close()
    fileTTL.close()



if __name__ == '__main__':
    outputFolder = 'data/transformed/'
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    print("Start name.basics")
    transformNameBasics()
    print("Finish name.basics")
    
    print("\n")
    
    print("Start title.basics")
    transformTitleBasics()
    print("Finish title.basics")
    
    print("\n")
    
    print("Start title.principals")
    transformTitlePrincipals()
    print("End title.principals")

