# refactoring means to 
# restructure code without
# changing its external behavior
# this helps improve code readability
# and maintainability
from problem_set1 import problem_set1
from advanced_slicing import advanced_slicing

problem_set1()
advanced_slicing()


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
parts= quote.split ("-")
name_1 = parts[1].strip()
print(name_1)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
info = "Python is fun. Fun is good. Good is subjective."
import re

info = "Python is fun. Fun is good. Good is subjective."



every_third = info[2::3]
print(every_third)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_words = ' '.join(info[::-1])
print(reversed_words)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
star = "MAY THE FORCE BE WITH YOU."
star_war = star.lower()
print(star_war)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
list = ["apple" "banana" "cherry"]
seperator = "a"
final_list = seperator.join(list)
print(final_list)
# b. Now, split the string at every occurrence of the letter 'a'.
split_string = final_list.split('a')
print(split_string)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
text = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
text_1 = text.replace("busy", "distract")
print(text_1)
# b. Replace "plans" with "mistakes".
text_2 = text.replace("plans", "mistakes")
print(text_2)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
result = "Iteration" * 7
print(result)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text_3 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
if "moonlight" in text_3:
            print("Word found!")
else:
        print("Word not found!")
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase = "Supercalifragilisticexpialidocious"
char_count = len(phrase)
print(f"The number of characters in the phrase is: {char_count}")
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_i = phrase.lower().count('i')
print(f"The letter 'i' appears {count_i} times in the string.")