import os

diedActors = set()
movies = set()

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


    fileTTL.write("@prefix i: <http://www.example.com/sis/lda/imdb/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
    #for _ in range(0,100,1):
        line = fileTSV.readline()
        line = line[:-1]
        line = line.split('\t')
                
        if '\\N' in line[3]:
            continue
        diedActors.add(line[0])    
            
        
        output = "i:" + line[0] + ' i:n' + ' "' + line[1] + '";\n'
        #if '\\N' not in line[2]:
        #    output = output + 'i:b "' + line[2] + '";\n'
        #if '\\N' not in line[3]:
        #    output = output + 'i:d "' + line[3] + '";\n'

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

    fileTTL.write("@prefix i: <http://www.example.com/sis/lda/imdb/> .\n")
    #fileTTL.write("@prefix principals: <http://www.example.com/sis/lda/imdb/principals/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
        line = fileTSV.readline()
    
        line = line[:-1]
        line = line.split('\t')

        if line[2] not in diedActors:
            continue
        movies.add(line[0])
        
        output = "i:" + line[0] + ' i:p' + ' i:' + line[2] + ';\n'
       
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

    fileTTL.write("@prefix i: <http://www.example.com/sis/lda/imdb/> .\n")

    # head / row names
    fileTSV.readline()
    for _ in range(0,line_count-1,1):
        line = fileTSV.readline()
        line = line[:-1]
        line = line.split('\t')


        if line[0] not in movies:
            continue

        output = "i:" + line[0] + ' i:t' + ' "' + line[2] + '";\n'

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
    
    print("Start title.principals")
    transformTitlePrincipals()
    print("End title.principals")
    
    print("Start title.basics")
    transformTitleBasics()
    print("Finish title.basics")