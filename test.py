def alphabet_filter(word):
    word_constants = ""
    word_vowels = ""
    for i in "aeiou":
        word_constants = word.replace(i,"")
        print(word_constants)
        return word_constants
    for i in not("aeiou"):
        word_vowels = word.replace(i,"")
        print(word_vowels)
        return word_vowels
    return word_consonants, word_vowels

def main():
    word = input()
    alphabet_filter(word)
    
main()