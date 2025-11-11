import pytest

def dict_examples2():
    d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
    res = list(set(sum(d.values(), [])))
    print("the resulst is res ", res)
    return res


if __name__ == "__main__":

    dict_examples2()
    

