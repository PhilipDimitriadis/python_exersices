str = "Factory"

for i in range(len(str)):
  char = str[i] * (i + 1)
  asterisk = "*" * (len(str) - i - 1)
  print(char + asterisk)