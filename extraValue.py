tripleWord = [0, 7, 14, 105, 119, 210, 217, 224]
doubleWord = [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]
doubleLetter = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]
tripleLetter = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]

dictionary = {'А' : 10, 'Б' : 3, 'В' : 5, 'Г' : 3, 'Д' : 5, 'Е' : 9, 'Ж' : 2, 'З' : 2,
                      'И' : 8, 'Й' : 4, 'К' : 4, 'Л' : 4, 'М' : 5, 'Н' : 8, 'О' : 10, 'П' : 6,
                      'Р' : 6, 'С' : 6, 'Т' : 5, 'У' : 3, 'Ф' : 1, 'Х' : 2, 'Ц' : 1, 'Ч' : 2,
                      'Ш' : 1, 'Щ' : 1, 'Ъ' : 1, 'Ы' : 2, 'Ь' : 2, 'Э' : 1, 'Ю' : 1, 'Я' : 3}

def calcWordValue(combo, letterDict, board):
    wordValue = 0
    timesDouble = 0
    timesTriple = 0
    
    for spot in combo:
        if spot in doubleWord:
            timesDouble += 1
        elif spot in tripleWord:
            timesTriple += 1
        if spot in doubleLetter:
            if spot in letterDict.keys():
                wordValue += 2 * dictionary[letterDict[spot]]
            else:
                wordValue += 2 * dictionary[board[spot]]
        elif spot in tripleLetter:
            if spot in letterDict.keys():
                wordValue += 3 * dictionary[letterDict[spot]]
            else:
                wordValue += 3 * dictionary[board[spot]]
        else:
            if spot in letterDict.keys():
                wordValue += dictionary[letterDict[spot]]
            else:
                wordValue += dictionary[board[spot]]
                
    return wordValue * (2**timesDouble) * (3**timesTriple)

def maxComboValue(workingCombos, board):
    maxCombo = [-1, [], []]
    maxLocations = []
    for workingCombo in workingCombos:
        letterDict = {}
        for (letter, space) in zip(workingCombo[0], workingCombo[1]):
            letterDict[space] = letter
        comboValue = 0
        for combo in workingCombo[2]:
            # add value of every combo to the total comboValue
            comboValue += calcWordValue(combo, letterDict, board)
        if len(workingCombo[1]) == 7:
            # add 50 to any combo that uses all seven letters in hand
            comboValue += 50
        if comboValue > maxCombo[0]:
            maxCombo = [comboValue, workingCombo[0], workingCombo[1]]
            maxLocations = workingCombo[1]
    for location in maxLocations:
        if location in tripleWord:
            tripleWord.remove(location)
        elif location in doubleWord:
            doubleWord.remove(location)
        elif location in doubleLetter:
            doubleLetter.remove(location)
        elif location in tripleLetter:
            tripleLetter.remove(location)
    return maxCombo
