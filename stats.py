def getNumWords(text):
    words = text.split()
    return len(words)

def getNumChars(text):
    chars = {}
    for i in range(0, len(text)):
        char = text[i].lower()
        if char not in chars:
            chars[char] = 0
        chars[char] = chars[char] + 1
    return chars