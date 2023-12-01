def palindrome(s):
    return s==s[::-1]
    
    
s = input("Please enter your Text: ")
result=palindrome(s)

if result:
   print("Text is palindrome")
else:
   print("Text is not palindrome")
