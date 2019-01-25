
word = input("Give me a word: ")

palindrome = word[::-1]

if word == palindrome:
    print("This is a palindrome")

else:
    print("Nothing special about this word. ")
