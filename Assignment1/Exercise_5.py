from nltk.corpus import words, brown

examplesString = "iliketurtles"
exampleEncryptedText = "psprlabyaslz" # 7-shift


def break_cipher(encrypted_text):
    allCombinations = []
    for i in range(0,27):
        newText = ""
        for char in encrypted_text:
            if ord(char) + i >= 97 and ord(char) + i <= 122:
                newText += chr((ord(char) + i))
            else:
                newText += chr(ord(char) - (26-i))

        allCombinations.append(newText)
    return (allCombinations)

wordlist_lowercased = set(i.lower() for i in brown.words())

allPermutations = break_cipher(exampleEncryptedText)

likelyPermutations = {}

for permutation in allPermutations:
    for word in wordlist_lowercased:
        if word in permutation and len(word)>2:
            if permutation in likelyPermutations:
                likelyPermutations[permutation] += 1
            else:
                likelyPermutations[permutation] = 1

print(list(likelyPermutations.keys())[list(likelyPermutations.values()).index(max(likelyPermutations.values()))], "is likely to be the actual sentence")
#whichever permutation has the most occurances of actual words is likely to be the real sentence
