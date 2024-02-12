def filemanipulation(file1):
    word_count={}
    with open(file1,'r') as file:
        for line in file:
            words=line.split()
            for wrd in words:
                wrd=wrd.strip('.,!?').lower()
                if wrd in word_count:
                    word_count[wrd]+=1
                else:
                    word_count[wrd]=1
    print(word_count)
    for wrd in sorted(word_count):
        print(wrd ,":" ,word_count[wrd])
file="Task 5 Rohit Sharma.txt"
filemanipulation(file)

