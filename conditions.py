def cat_hat(str):
    a=str.count('cat')
    b=str.count('hat')
    if a == b:
        return True
    else:
        return False

result = cat_hat("catinahad")
print(result)
