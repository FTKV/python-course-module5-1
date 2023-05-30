text = "Test {} {} {} {}"

print(text.format("this", 
                  "and this", 
                  "more this", 
                  "and more this"))

text1 = "{:#f}".format(10)

print(text1)

for num in range(20):
    print("{n:#d} {n:#x} {n:#o} {n:#b}".format(n=num))

for num in range(20):
    print("{n:^10d} {n:>10x} {n:>10o} {n:>10b}".format(n=num))

for num in range(20):
    print("{n:^10d}||||{n:>10x}|{n:>10o}|{n:>10b}".format(n=num))

for num in range(20):
    print("{n:03d}||||{n:>10x}|{n:>10o}|{n:>10b}".format(n=num))

print("pi {:0.3}".format(3.1415))
print("pi {:0.3}".format(13.1415))
print("pi {:0.3}".format(123.1415))