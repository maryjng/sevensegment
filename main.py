digitList = [("###", "# #", "# #", "# #", "###"), (" # ", " # ", " # ", " # ", " # "), ("###", "  #", "###", "#  ", "###"), ("###", "   #", "###","  #", "###"), ("# #", "# #", "###", "  #", "  #"), ("###", "#  ", "###", "  #", "###"), ("###", "#  ", "###", "# #", "###"), ("###", "  #", "  #", "  #", "  # "), ("###", "# #", "###", "# #", "###"), ("###", "# #", "###", "  #", "###")]

def sevensegment():
    segment = input()
    if segment.isdigit(): 
       templist = []
    
        for ch in segment:
            templist.append(digitlist[ch])
        for n in range(5):
            sevenseg = [tup[n] for tup in templist]
            print(sevenseg)
            
    else: print("invalid entry")
