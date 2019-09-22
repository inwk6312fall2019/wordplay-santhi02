def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def file_avoid(f):
    forbidden = input('enter the forbidden letters: ')
    count = 0
    for word in f:
        if avoids(word.strip(), forbidden):
            count += 1
    return count
fin = open('words.txt')

print(file_avoid(fin))
