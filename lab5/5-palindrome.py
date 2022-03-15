def palindrome(s):
    s = list(s.lower().replace(" ", ""))
    if s == s[::-1]:
        print("palindrom")
    else:
        print("not palindrome")

palindrome(input())