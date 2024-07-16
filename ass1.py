def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
input_string=input("enter the string:")
print("number of vowels:",count_vowels(input_string))    
       