# sort first by length then by alphab order in lowercase
def weird_sort(strings: list[str]) -> list[str]:
	strings.sort(key = str.lower)
	strings.sort(key = len)

strng = ["Hall", "allo", "All", "e"]
weird_sort(strng)
print(strng)