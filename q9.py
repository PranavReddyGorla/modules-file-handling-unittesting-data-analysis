my_list = ["geeks", "geeg", "keek", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
#If the original string is equal to its reverse, it's a palindrome and is kept in the result
print(result) 