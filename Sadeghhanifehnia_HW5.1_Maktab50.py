myfile = open('test_file.txt', 'r+')
mystr = myfile.read()

word_count = 0
char_count = 0
for line in mystr.split("\n"):
    for word in line.strip().split(" "):
        word_count += 1
        for c in word:
            char_count += 1
myfile.close()
print("tedad line barabar ast ba : ", len(mystr.split("\n")))
print("tedad word barabar ast ba : ", word_count)
print("tedad char barabar ast ba : ", char_count)
