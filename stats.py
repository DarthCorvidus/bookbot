def getNumWords(text):
    words = text.split()
    return len(words)

def getNumChars(text):
    chars = {}
    for char in text:
        char = char.lower()
        # get(char, 0) serves as some sort of coalesce here.
        chars[char] = chars.get(char, 0) + 1
    return chars

def sortAmount(entry):
    return entry["num"]

def getSortedChars(chars):
    sorted = []
    for char in chars:
        entry = {"char": char, "num": chars[char]}
        sorted.append(entry)
    sorted.sort(key=sortAmount, reverse=True)
    return sorted
