import sys

print("Reading words.txt")
words = set()
for line in open("words.txt", encoding="utf-16").readlines():
    words.add(line.lower().strip())
print(f'read {len(words)} words')

def findWords(prefix, charsLeft, minLength):
    for i in range(len(charsLeft)):
        char = charsLeft[i]
        candidate = prefix + char
        #print(candidate)
        if len(candidate) >= minLength and candidate in words:
            print(f"*** {candidate} ***")
        newCharsLeft = charsLeft[:i] + charsLeft[i+1:]
        if newCharsLeft:
            findWords(candidate, newCharsLeft, minLength)

def findWordsPattern(pattern, charsLeft):
    index = pattern.find("_")
    for i in range(len(charsLeft)):
        char = charsLeft[i]
        candidate = pattern[:index] + str(char) + pattern[index+1:]
        if "_" in candidate:
            newCharsLeft = charsLeft[:i] + charsLeft[i+1:]
            findWordsPattern(candidate, newCharsLeft)
        elif candidate in words:
            print(f"*** {candidate} ***")

chars = sys.argv[1]
minLength = int(sys.argv[2])
charList = list(chars)
charList.sort()

if len(sys.argv) == 4:
    pattern = sys.argv[3]
    for char in pattern:
        if char != "_":
            charList.remove(char)
    charList.sort()
    findWordsPattern(pattern, charList)
else:
    findWords("", charList, minLength)
