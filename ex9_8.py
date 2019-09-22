def is_palindrome(word):
    return word == word[::-1]

def search_number(number):
    if is_palindrome(str(number)[2:]):
        number += 1
        if is_palindrome(str(number)[1:]):
            number += 1
            if is_palindrome(str(number)[1:5]):
                number += 1
                if is_palindrome(str(number)):
                    return True
    return False

for num in range(100000, 1000000):
    if search_number(num):
        print(num)



