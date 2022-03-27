#Word counter
#Prompt the user for a setence and print out how many words in the setence

answ = input("Write a setence and I tell you how many words it have ")
word_counter = len(answ.split())
print("You write '", answ, "' and it contains ", word_counter , "words")

