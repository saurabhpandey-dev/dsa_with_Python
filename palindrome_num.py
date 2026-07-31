# string ko reverse karke original se compare karo.

def check_palindrome(data):
    data.lower()
    data.replace(' ','')
    return data == data[::-1]

print(check_palindrome('madam'))