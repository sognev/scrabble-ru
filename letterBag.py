import random

class letterBag():

    def __init__(self):
        letterDict = {'А' : 10, 'Б' : 3, 'В' : 5, 'Г' : 3, 'Д' : 5, 'Е' : 9, 'Ж' : 2, 'З' : 2,
                      'И' : 8, 'Й' : 4, 'К' : 4, 'Л' : 4, 'М' : 5, 'Н' : 8, 'О' : 10, 'П' : 6,
                      'Р' : 6, 'С' : 6, 'Т' : 5, 'У' : 3, 'Ф' : 1, 'Х' : 2, 'Ц' : 1, 'Ч' : 2,
                      'Ш' : 1, 'Щ' : 1, 'Ъ' : 1, 'Ы' : 2, 'Ь' : 2, 'Э' : 1, 'Ю' : 1, 'Я' : 3}
        self.letterBag = []
        for key in letterDict.keys():
            for _ in range(letterDict[key]):
                self.letterBag.append(key)

    def removeLetters(self, num):
        removedLetters = ''
        if num < len(self.letterBag):
            for _ in range(num):
                x = random.random()
                index = int(x*len(self.letterBag) // 1)
                removedLetters += self.letterBag[index]
                self.letterBag.pop(index)
        else:
            for letter in self.letterBag:
                removedLetters += letter
            self.letterBag = []
        return removedLetters
            
