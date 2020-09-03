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
