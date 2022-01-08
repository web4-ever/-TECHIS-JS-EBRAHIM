number = int(input("Enter the number:"))
string = str(number)
rev_string = string[::-1]
print("reversed:" ,rev_string)
if string == rev_string:
  print("number is palindrome")
else:
  print("number is not palindrome")   
