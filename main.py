digitList = [("###", "# #", "# #", "# #", "###"), (" # ", " # ", " # ", " # ", " # "), ("###", "  #", "###", "#  ", "###"), ("###", "  #", "###","  #", "###"), ("# #", "# #", "###", "  #", "  #"), ("###", "#  ", "###", "  #", "###"), ("###", "#  ", "###", "# #", "###"), ("###", "  #", "  #", "  #", "  #"), ("###", "# #", "###", "# #", "###"), ("###", "# #", "###", "  #", "###")]

def sevensegment():
    segment = input()
    segment = segment.replace(" ", "")
    if segment.isdigit():
        templist = []
        for ch in segment:
            templist.append(digitList[int(ch)])
        for n in range(5):
            sevenseg = [tup[n] for tup in templist]
            print(" ".join(sevenseg))

    else: print("invalid entry")

sevensegment()


##### starting hexadecimal A b C d E F

hexDict = {"A" : (" # ", "# #", "###", "# #", "# #"), "b" : ("#  ", "#  ", "###", "# #", "###"), "C" : ("###", "#  ", "#  ", "#  ", "###"), "d" : ("  #", "  #", "###", "# #", "###"), "E" : ("###", "#  ", "###", "#  ", "###"), "F" : ("###", "#  ", "###", "#  ", "#  ")}
           
def hexadecimal():
    segment = input()
    for ch in segment:
        if ch not in hexDict:
           print("invalid entry")
           return
        else: templist.append(hexDict[ch])
        for n in range(5):
            hexadecimal = [tup[n] for tup in templist]
            print(" ".join(hexadecimal))
            
