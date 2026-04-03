def rev_matrice(arr: list[list[int]]) -> list[list[int]]:
	rev = []
	arr_rev = []
	for r in arr:
		rev.append(r[::-1])
	i = len(rev) - 1
	for r in rev:
		arr_rev.append(rev[i])
		i -= 1
	return (arr_rev)

print(rev_matrice([[1, 2, 3], [-1, -2], [5, 6]]))

def rev_deux(arr: list[list[int]]) -> list[list[int]] :
	rev = [l[::-1] for l in arr]
	return rev[::-1]

print(rev_deux([[1, 2, 3], [-1, -2], [5, 6]]))