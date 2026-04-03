s = "a-b_c:d!"
to_remove = "-_:!"
result = "".join(c for c in s if c not in to_remove)
print(result)
# str.lstrip(str)

# str.maketrans(ori:str, fin:str, supp:str)

# str.rsplit(sep, maxsplit)
#     sep : le séparateur
#     maxsplit : nombre maximum de découpages
#     le résultat est une liste de chaînes