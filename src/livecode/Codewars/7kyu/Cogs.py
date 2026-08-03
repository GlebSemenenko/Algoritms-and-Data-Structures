from fractions import Fraction

def cog_RPM(cogs):
    a = Fraction(cogs[0], cogs[-1])
    b = 1
    if len(cogs) % 2 == 0:
        b = -1
    return a * b

print(cog_RPM([100, 75]))

s = "asd"
ss = s[::-1]
print(ss)
