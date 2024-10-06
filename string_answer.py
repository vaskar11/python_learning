# 1 Write a Python program that asks the user to input a string and then outputs the string in reverse.
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)


# 2. Extract the Substring "World" from "Hello, World!" Using Slicing:
my_string = "Hello, World!"
substring = my_string[7:12]
print("Substring:", substring)


# 3. Count the Number of Vowels in a Given String:
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
print("Number of vowels:", vowel_count)


# 4. Convert String to Uppercase and Replace 'A' with '@':
# Ask the user to input a string
user_input = input("Enter a string: ")
new_string = user_input.upper().replace('A', '@')
print("Modified string:", new_string)


# 5. Create a String Using f-String Formatting:
name = "Bhaskar"
age = 23
city = "Kathmandu"
formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}."
print(formatted_string)


# 6. Format a float number 123.456789 to display only two decimal places.
number = 123.456789
formatted_number = f"{number:.2f}"
print("Formatted number:", formatted_number)


# 7. Capitalize the First Letter of Every Word in a Sentence:
user_input = input("Enter a sentence: ")


capitalized_sentence = user_input.title()
print("Capitalized sentence:", capitalized_sentence)


# 8. Check if a String is a Palindrome:
user_input = input("Enter a string: ")
is_palindrome = user_input == user_input[::-1]
print("Is palindrome:", is_palindrome)


# 9. Check if a Substring Exists Within a String:
string = input("Enter a string: ")
substring = input("Enter a substring: ")
exists = substring in string
print("Substring exists:", exists)


# 10. Find All Occurrences of 'a' in the String "banana" and Print Their Positions:
my_string = "banana"
positions = [i for i, char in enumerate(my_string) if char == 'a']
count= len(positions)
print(f"Total number of a :{count} \nPositions of 'a':", positions)


# 11. Split a String Into a List of Words:
my_string = "apple, banana, cherry"
word_list = my_string.split(", ")
print("List of words:", word_list)


# 12. Join a List of Words into a Single String Separated by Spaces:
word_list = ["Python", "is", "fun"]
joined_string = " ".join(word_list)
print("Joined string:", joined_string)


# 13. Compare Two Strings Lexicographically:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if string1 < string2:
    print(f'"{string1}" comes before "{string2}" alphabetically.')
elif string1 > string2:
    print(f'"{string1}" comes after "{string2}" alphabetically.')
else:
    print(f'"{string1}" and "{string2}" are equal alphabetically.')


# 14. Check if Two Strings are Anagramsm ie (contain the same letters in different orders).:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
is_anagram = sorted(string1) == sorted(string2)
print("The strings are anagrams:", is_anagram)


# 15. Remove All Spaces from a String:
user_input = input("Enter a string: ")
no_spaces = user_input.replace(" ", "")
print("String without spaces:", no_spaces)


# 16. Escape Special Characters in a String:
special_string = "This is a line.\nThis is a tab:\tHere is a backslash: \\"
print(special_string)
escaped_string = repr(special_string)
print("Escaped string:", escaped_string)


# 17. Replace All Occurrences of a Substring with Another Substring:
original_string = input("Enter the original string: ")
to_replace = input("Enter the substring to replace: ")
replacement = input("Enter the replacement substring: ")
modified_string = original_string.replace(to_replace, replacement)
print("Modified string:", modified_string)


# 18. Count the Number of Words in a String:
user_input = input("Enter a string: ")
word_count = len(user_input.split())
print("Number of words:", word_count)

# 19. Remove Duplicate Characters from a String (Preserving Order):
user_input = input("Enter a string: ")
seen = set()
result = ''.join([char for char in user_input if not (char in seen or seen.add(char))])
print("String without duplicate characters:", result)

# 20. Find the Longest Word in a Given String:
user_input = input("Enter a string: ")
words = user_input.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)


# 21. Split a string by commas and sort each word alphabetically
def split_and_sort(string):
    word= string.split(",")
    word.sort()
    return word

string= "banana, apple, grape, orange"
sorted_words= split_and_sort(string)
print(sorted_words)


# 22 Remove punctuation from a string
import string
def remove_punc(s):
    return ''.join(c for c in s if c not in string.punctuation)

s = "Hello, world! How's it going?"
clean_word= remove_punc(s)
print(clean_word)

# 23. Check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()
str="HelloWorld"
print(is_alpha(str))

# 24. Find the frequency of each character in a string
def char_feq(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq

s= 'hello world'
freq= char_feq(s)
print(freq)

#25 convert a string from snake_Case to camelCase
def snake_to_camel(s):
    c= s.split('_')
    return c[0]+''.join(x.capitalize() for x in c[1:])

snake_str = "this_is_snake_case"
camel_str = snake_to_camel(snake_str)
print(camel_str)


# 26. Concatenate two strings without using the + operator
def concatenate_strings(s1, s2):
    return f"{s1}{s2}"

s1 = "Hello"
s2 = "World"
result = concatenate_strings(s1, s2)
print(result)


# 27. Convert all spaces in a string to underscores
def space(s):
    return s.replace(" ","_")
s="Hi I am Bhaskar Subedi"
print(space(s))


#28. Repeat a string n times
def repeat(s,n):
    return s*n
s= input("enter string that you want to repeat: ")
n=int(input("enter how many times: "))
print(repeat(s,n))

# 29. Remove the first and last characters from a string
s= "hello"
print(s[1:-1])


# 30. Check if a string starts and ends with the same character
def check(s):
    return s[0]==s[-1] if len(s)>0 else False
s="nabin"
print(check(s))


#31. Count how many times each vowel appears in a given string:
def count_vowel(s):
    vowels='aeiouAEIOU'
    vow_count= {v:0 for v in vowels}
    for char in s:
        if char in vowels:
            vow_count[char]+=1
    return vow_count
s="Hi I am Bhaskar Subedi"
print(count_vowel(s))

# 32. find shortest word in string
def shortest(s):
    words= s.split()
    w= min(words,key=len)
    return w
s="Hi I am Bhaskar Subedi"
print(shortest(s))

# 33. Find and print the longest repeated substring in a given string:
def longest_repeated_substring(input_string):
    n = len(input_string)
    substrings = [input_string[i:j] for i in range(n) for j in range(i+1, n+1)]
    repeated_substrings = [sub for sub in substrings if input_string.count(sub) > 1]
    
    if repeated_substrings:
        return max(repeated_substrings, key=len)
    else:
        return ""

input_string = "abcabcabc"
print("Longest repeated substring:", longest_repeated_substring(input_string))


# 34. Check if a string contains any numeric characters:
def contain(s):
    for char in s:
        if char.isdigit():
            return True
    return False
s='Hi I am bhaskar subedi 124'
print(contain(s))


#  35. Replace every second character of a string with *
def replace(s):
    char_list= list(s)
    for i in range(1, len(char_list),2):
        char_list[i]='*'
    return ''.join(char_list)
s='Hi I am bhaskar subedi'
print(replace(s))