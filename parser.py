import glob
import csv

def main():
    with open('data.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(["Genre", "Artist", "Title", "UniqueLinesRatio"])
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
                #extract features from song
                lyrics = []
                while i < len(lines) and not lines[i].startswith("###"):
                    line = lines[i].strip()
                    if line != "":
                        lyrics.append(line)
                        #print (line)
                    i = i + 1

                uniqueLinesRatio = calc_unique_lines_ratio(lyrics)
                #TODO: average character count per word
                #TODO: average word count per line
                #TODO: total word count
                #TODO: bag of words extraction
                #TODO: unique word ratio per song
                #TODO: unique word ratio per line
                csvWriter.writerow([genre, artist, title, uniqueLinesRatio])
            print("### "+ str(numberOfSongs) + " songs found for "+ genre +"\n")

def calc_unique_lines_ratio(lyrics):
    return len(set(lyrics)) / len(lyrics)

if __name__ == "__main__":
    main()