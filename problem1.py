#program to count occurence of a character in a string

sentence = str(input("Enter Sentence : "))
letter = str(input("Enter word : "))
count = 0
for i in range (len(sentence)):
               if (sentence[i] == letter):
                   count = count+1

print(count)
