BASE = "0123456789abcdefghijklmnopqrstuvwxyz"


# def index(digit: str) -> int:
#     i: int = 0
#     for d in base:
#         if d == digit:
#             break
#         i += 1
#     return i


# def to_dec(num: str, base_from: int) -> int:
#     dec: int = 0
#     i: int = 0
#     for digit in num:
#         dec += index(digit)*(base_from**i)
#         i += 1
#     return dec


# def to_base_to(dec: int, base_to: int) -> str:
#     num: str = ""
#     while dec > 0:
#         num += str(base[dec % base_to])
#         dec = int(dec/base_to)
#     return num[::-1]


# def convertbase(num: str, base_from: int, base_to: int) -> str:
#     x = to_dec(num[::-1], base_from)
#     return to_base_to(x, base_to)


def convertbase(num: str, base_from: int, base_to: int) -> str:
    dec = int(num, base_from)
    if dec == 0:
        return '0'
    res = []
    while dec:
        res.append(BASE[dec % base_to])
        dec //= base_to
    return "".join(res[::-1])


print(convertbase("100", 2, 2))
