introduction = input("Enter Your Intro: ")
char_count = 0
word_count = 1

for i in introduction:
    char_count = char_count + 1
    
    if(i == " "):
        word_count = word_count + 1
    
    print("Number of Words:")
    print(word_count)
    print("Number of Characters:")
    print(char_count)