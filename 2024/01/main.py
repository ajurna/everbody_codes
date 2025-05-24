def potion_count(c, extra=0)-> int:
    match c:
        case "A":
            return 0 + extra
        case "B":
            return 1 + extra
        case "C":
            return 3 + extra
        case "D":
            return 5 + extra
        case "x":
            return 0
        case _:
            raise ValueError("Invalid character")

with open("data01") as f:
    data = f.read().strip()
total = 0
for creature in data:
    total += potion_count(creature)
print(total)
with open("data02") as f:
    data = f.read().strip()
total = 0
for i in range(0, len(data), 2):
    pair = data[i:i+2]
    if 'x' in pair:
        for creature in pair:
            total += potion_count(creature)
    else:
        for creature in pair:
            total += potion_count(creature, 1)
print(total)
total = 0
with open("data03") as f:
    data = f.read().strip()
for i in range(0, len(data), 3):
    triple = data[i:i+3]
    x_count = triple.count('x')
    if x_count == 0:
        for creature in triple:
            total += potion_count(creature, 2)
    elif x_count == 1:
        for creature in triple:
            total += potion_count(creature, 1)
    elif x_count == 2:
        for creature in triple:
            total += potion_count(creature)
print(total)