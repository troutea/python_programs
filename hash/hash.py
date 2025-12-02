data = [
    ("orange", "one"),
    ("apple", "two"),
    ("lemon", "three"),
    ("grape", "four"),
    ("melon", "five"),  
]

# print(ord("a"))
# print(ord("b"))

def simple_hash(s: str) -> int:
    basic_hash = ord(s[2])
    return basic_hash % 10


if __name__ == "__main__":
    for key, value in data:
        
     sha = simple_hash(key)
     print(key, sha)
   
   