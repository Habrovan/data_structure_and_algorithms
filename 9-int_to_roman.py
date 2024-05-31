def int_to_roman(y):
    numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman= ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    j=12
    roman_numerals = ""
    while y!=0:
        if numbers[j]<=y:
            roman_numerals += roman[j]
            y=y-numbers[j]
        else:
            j-=1
    return roman_numerals
user_input_button=int(input("Enter Number: "))
print("The Number Entered is Equivalent to ",int_to_roman(user_input_button),"Roman Numerals")