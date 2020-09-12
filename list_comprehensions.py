numbers = [1,2,3,4,5,6,7,8,9,10]


# using a list comprehension
# print a list of all nums multiplied by 2

a = [num * 2 for num in numbers]
print(a) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# using a list comprehension
# print all of the nums that are greater than 5

b = [num for num in numbers if num > 5]
print(b) # [6, 7, 8, 9, 10]


# using a list comprehension
# square each number in nums but only if the number is even

c = [num**2 for num in numbers if num % 2 == 0]
print(c) # [4, 16, 36, 64, 100]


# using a list comprehension
# create a new list that shows the length of each word in this sentence
# BUT ONLY IF THE WORD IS NOT "the"
# don't forget: you need to turn the sentence into a list first
sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split()
word_len = [len(word) for word in words if word != "the"]
print(word_len) # [5, 5, 3, 5, 4, 4, 3]


