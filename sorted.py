pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)

print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)


empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)

#more_numbers = list(numbers)
#more_numbers = numbers[:]

more_numbers = numbers.copy()

print(more_numbers)

print(numbers is more_numbers)
