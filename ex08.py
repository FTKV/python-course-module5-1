import re

s = "I am 25 years old 34, 563"
age = re.search("\d+", s)
print(age)
print(age.group())
print(type(age.group()))

all_ages = re.findall("\d+", s)
print(all_ages)

all_ages = re.findall("\d", s)
print(all_ages)

all_ages = re.findall("\d{2}", s)
print(all_ages)

all_ages = re.findall("\d{3}", s)
print(all_ages)

all_ages = re.findall("\d{2}\W", s)
print(all_ages)

all_ages = re.findall("\d{2}\s", s)
print(all_ages)


result_sub = re.sub(r"am", "sam", s)

print(result_sub)

result_sub = re.sub(r"(\d+)", "тут має бути реклама", s)

print(result_sub)