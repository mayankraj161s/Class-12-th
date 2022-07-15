# WAP to remove all words that contain character entered by user in the file and then write all the content in another file.
try:
    f = open("myfile1.txt", "r")
    chr = input("Enter a character to remove words containing it: ")
    lines = f.readlines()
    for a in lines:
        index = lines.index(a)
        words = a.split()
        length = len(words)
        i, c = 0, 0
        while i < (length-c):
            if chr.upper() in words[i]  or chr.lower() in words[i]:
                del words[i]
                c = c + 1
                i = i - 1
            i = i + 1
        j = ""
        for k in words:
            j = j + "{} ".format(k)
        lines[index] = j
    f.close()

    f1 = open("myfile2.txt", "w")
    c = ""
    for b in lines:
        c = c + "{}\n".format(b)
    f1.write(c)
    f1.close()

except:
    print('''Create "myfile1.txt"''')
