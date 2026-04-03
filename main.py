# 15
a = [15, 23, 35, 42, 55]
natija = list(filter(lambda x: x % 10 == 5, a))
print(natija)


# 16
a= ["apple", "banana", "kiwi", "strawberry"]

roy = list(filter(lambda x: len(x) > 5, a))

print(roy)


# 17
a= ["apple", "pear", "grape", "plum"]

roy = list(filter(lambda x: "a" in x, a))
print(roy)

# 18
a = ["Ali", "vali", "Sardor", "john"]

roy = list(filter(lambda x: x[0].isupper(), a))
print(roy)

# 19
a = ["123", "abc", "456", "78a"]

roy = list(filter(lambda x: x.isdigit(), a))
print(roy)

# 20
a = ["", "hello", "", "world"]

roy = list(filter(lambda x: x != "", a))
print(roy)


# 21
a = ["hi", "hello", "world", "python"]

roy = list(filter(lambda x: len(x) % 2 == 0, a))
print(roy)

# 22
a = ["java", "python", "javascript", "c++"]

roy = list(filter(lambda x: len(x) > len("python"), a))
print(roy)

# 23
a = ["python", "java", "kotlin", "go"]

roy = list(filter(lambda x: x.endswith('n'), a))
print(roy)
