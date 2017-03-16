import glob

#iterate through files
for filename in glob.iglob('data/*.txt'):
    print("### Parsing file " + filename)
    genre = filename[5:len(filename)-4]
    print("### Genre: "+ genre)
    numberOfSongs = 0
    file = open(filename)
    lines = file.readlines()
    i = 0
    while i < len(lines) and not lines[i].startswith("###"):
        i = i + 1
    while i < len(lines):
        artist = lines[i][3:].strip()
        title = lines[i+1][3:].strip()
        numberOfSongs = numberOfSongs + 1
        print (artist + " - " + title)
        i = i + 2
        while i < len(lines) and not lines[i].startswith("###"):
            line = lines[i].strip()
            #print (line)
            i = i + 1
    print("### "+ str(numberOfSongs) + " songs found for "+ genre +"\n")
