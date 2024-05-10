original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')
for (k, v) in original_dict.items()}
print(new_dict_1)