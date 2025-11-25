
animals = {
        "lion": "scary",
        "elephant": "big",
        "teddy": "cuddly",   
    }

def shallow_copy(dict_animals):
    """
    This is code is to demonstrate shallow copy
    """
    
    
    
    things = animals.copy()
    animals["teddy"] = "toy"
    print(things["teddy"])
    print(animals["teddy"])
    print("hello")
    
if __name__ == "__main__":
     shallow_copy(animals)
   
    
    


