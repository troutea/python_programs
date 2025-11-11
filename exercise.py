word_count = {}

print("hello")

# Test string
text = "Later in the course, you'll see how to use the collection Counter class"


# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1
        word_count.items()

# printing the dictionary

for letter , count in sorted(word_count.items()):
    print(letter, count)
