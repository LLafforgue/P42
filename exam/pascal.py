def pascal_letter(string: str)->str:
	i = 0
	pascal = ""
	for r in string:
		if i % 2 == 0:
			pascal += r.lower()
		else :
			pascal += r.upper()
		i += 1
	return (pascal)

strg = "Hello"

strg = pascal_letter(strg)
print(strg)