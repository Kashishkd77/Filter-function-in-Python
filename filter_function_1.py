#illustration of filter function
letter=['a','r','t','y','u','i','e','o','m','x']

#check_value() should return a value then only acceptable by filter function as its parameter
def check_vowel(letter):
    vowel=['a','e','i','o','u']
    if letter in vowel:
        return True
    else:
        return False
f1=filter(check_vowel,letter)

#if we try to directly print the vowels in the given list then the output wont be correct
#as we need to check the elements of given list multiple times and print them so, we used for loop here
for vowel in f1:
    print(vowel)

# printing elements without using for loop i.e. in list format
f = list(filter(check_vowel, letter))
print(f)