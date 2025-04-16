# An iterable is any object in Python that can return its elements one at a time.
# It has a __iter__() method that returns an iterator.
# It's possible to loop over it with for loop.

# An iterator is an object that remembers where it is during iteration.
# It has two methods:
# 1. __iter__() -> returns the iterator object itself.
# 2. __next__() -> returns the next element or raises StopIteration.


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


class CountDown:
    def __init__(self, start):
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < 1:
            raise StopIteration
        current = self.value
        self.value -= 1
        return current


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current = self.index
        self.index += 1
        return self.words[current]


nums = MyRange(1, 10)

count = CountDown(3)

my_sentence = Sentence("This is a test")

for num in nums:
    print(num)

for num in count:
    print(num)

for word in my_sentence:
    print(word)
