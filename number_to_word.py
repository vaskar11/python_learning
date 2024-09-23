words_upto_19 = [
    '', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
words_for_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def number_to_words(n):
    if n == 0:
        return "zero"
    elif n <= 19:
        return words_upto_19[n]
    elif n <= 99:
        return words_for_tens[n // 10] + " " + words_upto_19[n % 10]
    elif n <= 999:
        return words_upto_19[n // 100] + " hundred " + (number_to_words(n % 100) if n % 100 != 0 else "")
    elif n <= 999999:
        return number_to_words(n // 1000) + " thousand " + (number_to_words(n % 1000) if n % 1000 != 0 else "")
    elif n<= 999999999:
        return number_to_words(n//1000000) + " million " +(number_to_words(n%1000000) if n%1000000!=0  else " ")
    elif n<= 999999999999:
        return number_to_words(n//1000000000) + " billion " +(number_to_words(n%1000000000) if n%1000000000!=0  else " ")
    elif n<= 999999999999999:
        return number_to_words(n//1000000000000) + " trillion " +(number_to_words(n%1000000000000) if n%1000000000000!=0  else " ")    
    else:
        return "Number out of range"
n = int(input("Enter a number: "))
output = number_to_words(n)
print(output)
