st = input("Enter the characters: ")
words = st.split(" ")

coding = input("Enter 1 for True or 0 for False: ")
coding = True if coding == '1' else False

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "fsd"
            r2 = "dsb"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 6:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1] 
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
