def palindrome(word: str) -> bool:
    word= word.replace(' ','').lower()
    return word == word[::-1]
    


def run():
    word = input('Type a Word: ') 
    if (palindrome(word)):
        print('It is a palindrome')
    else:
        print('Sorry, this word isn\'t a palindrome') 

if __name__ == '__main__':
    run()