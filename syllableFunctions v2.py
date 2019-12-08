#I've edited this so that only the code in question is here.

# Loading Settings
checkForSylBreak = True
smartSearch = True

# Loading Syllables
file = open("allPossibleSymbols.txt","r") #Opens file
syllables = file.read().split("\n")
syllables.pop(0) #Encoding error
print("Syllables loaded correctly",len(syllables),"found.")


# Syllable Search
choice = 1 
if choice == 1:
    while True:
        validSyllables = []
        invalidSyllables = []
        word = str(input("In the romanised form, please type the word you want to include:").strip())
        # Input validation: No '.'; no IPA symbols (/ [ ])
        syllableBreak = False
        IPAsymbols = False
        IPAlist = ['/','[',']','ː','ˑ','ˈ','ˌ'] #Symbols I don't want to have while searching - could be used by someone, so it checks for the basic ones
        for letter in word:
            if letter == '.':
                syllableBreak = True
            if letter in IPAlist:
                IPAsymbols = True
        if syllableBreak and checkForSylBreak:
            print("Sorry, you've included a syllable break. This version does not need that. To change this, see the settings tab.")
        if IPAsymbols:
            print("Sorry, you've used IPA symbols, which do not work due to encoding.",IPAlist,"are not allowed.")
        # Search - Smart Search
        if smartSearch:
            y = 0
            for x in range(0,len(word)):
                if y>x:
                    continue
                if word[y:x] in syllables:
                    for z in range(x+1,len(word)):
                        validSyllables.append(word[x:z])
                        y = z
                        print(word[y:x],"found with z")
                        continue
                    validSyllables.append(word[y:x])
                    y = x
                    print(word[y:x],"found")
            print(word,validSyllables)
            