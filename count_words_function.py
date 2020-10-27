introduction = input("Enter Your Intro: ")
char_count = 0
word_count = 1

def word_count_func(char, words):
    for i in introduction:
        char = char + 1
        
        if(i == " "):
            words = words + 1
        
        print("Number of Words:")
        print(words)
        print("Number of Characters:")
        print(char)

word_count_func(char_count, word_count)