import csv
#Need to stop words from repeating in csv

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "input_data.txt"

fh = open(fname)
WordAndCounts = dict()
Newlist = list()
Totalstuff = list()

for line in fh:
    word1 = line.strip()
    words = word1.split()
    for word in words:
        Totalstuff.append(word)
        if word in Newlist:
            continue
        else:
            Newlist.append(word)

with open('results.csv', 'w', newline='') as csvfile:
    wordwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    wordwriter.writerow(["Word", "Count"])
    for word in Newlist:
            word2 = Totalstuff.count(word)
            WordAndCounts[word] = word2
            wordwriter.writerow([word,word2])

print ("Done, check results.csv")

            




