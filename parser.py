import glob

#iterate through files
for filename in glob.iglob('data/*.txt'):
    print("### Parsing file " + filename)
    file = open(filename)
    lines = file.readlines()
    i = 0
    while i < len(lines) and not lines[i].startswith("###"):
        i = i + 1
    while i < len(lines):
        artist = lines[i][3:].strip()
        title = lines[i+1][3:].strip()
        print (artist + " - " + title)
        i = i + 2
        while i < len(lines) and not lines[i].startswith("###"):
            line = lines[i].strip()
            #print (line)
            i = i + 1

