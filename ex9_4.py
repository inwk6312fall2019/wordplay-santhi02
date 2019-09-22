def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_only(word, 'a c e f h l o') == True:
        print(word) 
        count += 1

"""we can form a sentence using any of the 188 words that doesn't have 'a c e f h l o' """

print(count)
