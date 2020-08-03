digitList = [("###", "# #", "# #", "# #", "###"), (" # ", " # ", " # ", " # ", " # "), ("###", "  #", "###", "#  ", "###"), ("###", "   #", "###","  #", "###"), ("# #", "# #", "###", "  #", "  #"), ("###", "#  ", "###", "  #", "###"), ("###", "#  ", "###", "# #", "###"), ("###", "  #", "  #", "  #", "  # "), ("###", "# #", "###", "# #", "###"), ("###", "# #", "###", "  #", "###")]

def sevensegment():
    segment = input()
    if segment.isdigit(): 
       templist = []
    
        for ch in segment:
            templist.append(digitlist[ch])
        for n in range(5):
            print(templist[(n)] + " ")
    else: print("invalid entry")
