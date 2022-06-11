"""
Convert string input to integer without using built-in int function
Time  O(n)
Space O(1)
"""
def str_to_int(input_str):
  is_negative = False
  if (input_str[0] == "-"):
    is_negative = True
    input_str = input_str[1:]
  
  result = 0
  for i, v in enumerate(input_str[::-1]):
    result += (ord(v)-48) * (10 ** i)
  
  if is_negative:
    return -1 * result
  else:
    return result