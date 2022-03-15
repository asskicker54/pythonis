def palindrome(s):
    s = list(s.lower().replace(" ", ""))
    if s == s[::-1]:
        return "palindrom"
    else:
        return "not palindrome"