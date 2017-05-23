__author__ = "Samuel Bancroft"

# Python uses operator precedence, this means that mathematical functions (add, subtract, square, root, etc.) are carried
# out in a strict order if more than one is used in an equation i.e. 2 x 10 + 6 / 4
# Below is a full list of the mathematical operators in Python, they appear in order of precedence from first to last
# **            Exponentiation (to the power of)
# ~ + -         Complement, unary plus and minus (unary operators will be discussed later)
# * / % //      Multiple, divide, modulo and floor division (modulo returns the remainder and floor removes any non whole part)
# + -           Addition and subtraction
# >> <<         Right and left bitwise shift (bit shifting is also covered later)
# &             Bitwise 'AND'
# ^ |           Bitwise 'EOR' and 'OR'
# <= < > >=     Less than or equal to, less than, greater than and greater than or equal to
# <> == !=      Equality operators, not equal, equal, not equal
# = %= /= //= -= += *= **=      Assignment operators, same as a = a (assignment operator) b, so a = a + 1 == a += 1
# is  is not    Identity operators, used to determine is objects point to the same value
# in  not in    Membership operators, determines whether one object is a member of another so "a" in "main" is true
# not or and    Logical operators, if a = 1 and b = 2, a and b = false, a or b = true and not(a and b) = true
# You can use ( ) brackets to alter precedence as bracketed operations will always be evaluated first
# When more than one operator of the same precedence exists in an operation they will be evaluated left to right

a = 20
b = 10
c = 15
d = 5
e = 0

bitwiseA = 60               # 60 = 0011 1100
bitwiseB = 13               # 13 = 0000 1101
bitwiseC = 0                # 0 = 0000 0000

answer = a + b * d          # 20 + 10 * 5 == 20 + 50 == 70
print("a = 20; b = 10; c = 15; d = 5; e = 0")
print("------------------------------------")
print("a + b * d = ", answer)
answer = (a + b) * d        # (20 + 10) * 5 == 30 * 5 == 150
print("(a + b) * d = ", answer)
answer = a / b + c * d      # 20 / 10 + 15 * 5 == 2 + 15 * 5 == 2 + 75 == 77
print("a / b + c * d = ", answer)
answer = a / (b + c) * d    # 20 / (10 + 15) * 5 == 20 / 25 * 5 == 0.8 * 5 = 4
print("a / (b + c) * d = ", answer)
answer = e + b / a ** d     # 0 + 10 / 20 ** 5 == 0 + 10 / 3200000 == 0 + 0.000003125 == 0.000003125 == 3.125 x 10 to the -6
print("e + b / a ** d = ", answer, "\n")
print("bitwiseA = 60 or 0011 1100 in binary")
print("bitwiseB = 13 or 0000 1101 in binary")
print("bitwiseC = 0 or 0000 0000 in binary")
print("-----------------------------------")
bitwiseC = bitwiseA & bitwiseB      # bitwiseC = 60 & 13 == 0011 1100 AND 0000 1101 == 0000 1100 == 12
print("bitwiseA & bitwiseB = ", bitwiseC)
bitwiseC = bitwiseA | bitwiseB      # bitwiseC = 60 | 13 == 0011 1100 OR 0000 1101 == 0011 1101 == 61
print("bitwiseA | bitwiseB = ", bitwiseC)
bitwiseC = bitwiseA ^ bitwiseB      # bitwiseC = 60 ^ 13 == 0011 1100 EOR 0000 1101 == 0011 0001 == 49
print("bitwiseA ^ bitwiseB = ", bitwiseC)
bitwiseC = ~bitwiseA                # bitwiseC = ~60 == inverse 0011 1100 == 1100 0011 == -61 (the first 1 is now a -, so -64 + -2 + -1 = -61)
print("bitwiseC = ~bitwisaA, so bitwiseC = ", bitwiseC)
bitwiseC = bitwiseA << 2            # bitwiseC = 0011 1100 << 2 = 1111 0000 = 240
print("bitwiseC = bitwiseA << 2, so bitwiseC = ", bitwiseC)
bitwiseC = bitwiseA >> 2            # bitwsieC = 0011 1100 >> 2 = 0000 1111 = 15
print("bitwiseC = bitwiseA >> 2, so bitwiseC = ", bitwiseC)