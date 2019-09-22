def main():
    fin = open('words.txt')
    count = 0
    no_e_count = 0
    for words in fin:
        word = words.strip()
        count += 1
        if has_no_e(word):
            no_e_count += 1
            print (word)
    percentage = (no_e_count / count) * 100
    print(percentage)

def has_no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True

main()
