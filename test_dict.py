
mydict = {
    "name": "John",
    "city": "Dublin"
        
}

res = list(sorted({ele for val in mydict.values() for ele in val}))

print(res[1])

print(mydict)