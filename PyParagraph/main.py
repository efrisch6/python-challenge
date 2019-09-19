import os
import csv
import re
import statistics

para1 = os.path.join("paragraph_1.txt")

para2 = os.path.join("paragraph_2.txt")

wordCount = 0
sentenceCount = 0

with open(para2,'r') as txtfile:
    passage = txtfile.read()


#passage = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."

sentenceLength = []
wordCount = len(passage.split(" "))
sentences = re.split("(?<=[.!?]) +", passage)
sentenceCount = len(sentences)
words = []
letters = []
for sentence in sentences:
    words.append(sentence.split(" "))


for word in words:
    sentenceLength.append(len(word))
    for letter in word:
        letters.append(len(letter))


print("Paragraph Analysis")
print("-"*30)
print(f'Approximate Word Count: {wordCount}')
print(f'Approximate Sentence Count: {sentenceCount}')
print(f'Average Letter Count: {"{0:.1f}".format(statistics.mean(letters))}')
print(f'Average Sentence Length: {"{0:.1f}".format(statistics.mean(sentenceLength))}')











