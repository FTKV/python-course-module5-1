lorem = "Ljrhwp hhwejlw  riljw oi qjrjlkqw e?"

print(lorem.split())

lorem = "Ljrhwp hhwejlw\n  riljw oi\n qjrjlkqw e?"

split_data = [i.strip() for i in lorem.split("\n")]

print(split_data)

print(":".join(split_data))

print(":".join(split_data))

print(lorem[10:30])