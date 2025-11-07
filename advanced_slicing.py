def advanced_slicing():
    pass
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
string_2 = "abcdefghijklmnopqrstuvwxyz,"
string_2 = string_2[7:10]
print(string_2)
# b. Extract every second letter starting from 'a' to 'm'.
every_second_alphabet = "abcdefghijklmnopqrstuvwxyz,"[0:13:2]
print(every_second_alphabet)
# c. Reverse the entire string using slicing.
reverse_alphabet = "abcdefghijklmnopqrstuvwxyz,"[::-1]
print(reverse_alphabet)