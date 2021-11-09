def palindrome(word):
    word= word.replace(' ','')
    word=word.lower()
    invert= word[::-1]
    if word == invert:
        return True
    else:
        return False


def run():
    word = input('Type a Word: ') 
    verify= palindrome(word)
    if (verify):
        print('It is a palindrome')
    else:
        print('Sorry, this word isn\'t a palindrome') 

if __name__ == '__main__':
    run()