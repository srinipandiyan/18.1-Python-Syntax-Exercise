def print_upper_words(words):
    """Prints out each word in list as uppercase on a separate line"""
    
    for word in words:
        sample = word.lower().swapcase()
        print(f'\n {sample}')
    
def print_upper_words_two(words):
    """Prints out each word in a list if it begins with case insensitive E as uppercase"""
    
    for word in words:
        sample = word.lower().swapcase()
        if sample.startswith('E'):
            print(f'\n {sample}')

def print_upper_words_three(words, prefix):
    """Prints out each word in a list if it begins with the specified case insensitive letter(s) as uppercase"""
    
    for word in words:
        sample = word.lower()
        for letter in prefix:
            if sample.startswith(f'{letter}'):
                print(f'\n {sample.swapcase()}')

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words_three(["hello", "hey", "goodbye", "yo", "yes"], prefix={"h", "y"})