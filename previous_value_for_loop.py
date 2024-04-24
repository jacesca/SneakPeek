from itertools import accumulate 

n=5
result = list(accumulate(range(n), lambda acc, val: acc/2, initial=100))
print(result)

result = list(accumulate(range(n), lambda acc, val: f'{val}+{acc}'))
print(result)

result = list(accumulate(range(n), lambda acc, val: val+acc))
print(result)

result = list(accumulate(range(n), lambda acc, val: (val, acc)))
print(result)