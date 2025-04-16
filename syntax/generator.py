def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 10)


def sentence(my_sentence):
    for word in my_sentence.split():
        yield word


my_sentence = sentence("This is a test")
for word in my_sentence:
    print(word)


# def square_numbers(nums):
#     for num in nums:
#         yield num**2

square_numbers = (num**2 for num in nums)

for number in square_numbers:
    print(number)
