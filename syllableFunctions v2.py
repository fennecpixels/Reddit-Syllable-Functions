# Loading Settings
checkForSylBreak = True
smartSearch = True

# Loading Syllables
file = open("C:/Users/agent/OneDrive/Documents/Conlangs University/Conlang-Code/Word Generation/allPossibleSymbols.txt","r") #Opens file
syllables = file.read().split("\n")
syllables.pop(0) #Encoding error
print("Syllables loaded correctly",len(syllables),"found.")

# Welcoming the user
print("Welcome to the Sinkebwnja Word Checking program v2!")
options = """[1] Check syllables
[2] Shuffle syllable list
[3] View syllables
[4] View Changelog
[5] Settings
[6] Exit"""
optionsIndex = [1,2,3,4,5,6]
choice = -1
while choice not in optionsIndex:
    print(options)
    choice = int(input("Please select an option by using its index: ").strip())
    print(choice)
    if choice not in optionsIndex:
        print("Sorry, that is invalid. Please try again.")

# Syllable Search
if choice == 1:
    while True:
        validSyllables = []
        invalidSyllables = []
        word = str(input("In the romanised form, please type the word you want to include:").strip())
        # Input validation: No '.'; no IPA symbols (/ [ ])
        syllableBreak = False
        IPAsymbols = False
        IPAlist = ['/','[',']','ː','ˑ','ˈ','ˌ']
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

                
