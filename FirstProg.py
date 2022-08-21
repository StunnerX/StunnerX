# Enter Name & Print, Input, Type_Conversion

firstname = "Tony"
lastname = "Stark"
age = 51
is_genius = True
print(firstname + " " + lastname)  # We can print like this(Correct Form)
print(age, is_genius)  # We can also print like this
#--------------------------------------------------------------
Tony = input("Who is your superhero: ")  #<-- Taking Input-->
print("Your superhero is: " + Tony)   #<-- Print Input -->
#----------------------------------------------------------------

old_age = input("Enter your old age: ")
new_age = int(old_age) + 2  # Type_Conversion because can't concatenate str & int together
print(new_age)

number = 18   # Another Example Type_Conversion
print(float(number))
#------------------------------------------------------------------

print(8+2)

sum = 8+2
print(sum)

a = 10
b = 10
sum = a+b
print(sum)

a = input("Enter first number:" )
b = input("Enter second number: ")
sum = int(a) + int(b)
# print("Sum of two numbers is: ", sum)     # Receives Output Without error
print("Sum of two numbers is: "+ str(sum))  # But this is correct method
#--------------------------------------------------------------------

name = "Tony Stark"
print(name.find('S'))   # To find character
print(name.find('s'))   # If character doesn't find, Output: -1

name1 = "Tony Stark"
print(name1.replace("Tony Stark", "IronMan"))    # To replace String
print(name1.replace("Stark", "IronMan"))     # Some more examples
print(name1.replace("", "m"))       # Some more examples

name2 = "Iron man"      # Check Character/String is present or not
print('I' in name2, "Stark" in name2, 'Iron' in name2)
#------------------------------------------------------------------------

            # Mathemetical Operators
print(5+2)      # Sum
print(5-2)      # Subtraction
print(5*2)      # Multiply
print(5/2)      # Divide (Gives Decimal values)
print(5//2)     # Divide (Does not gives Decimal values)
print(5%2)      # Divide (Gives Remainder)
print(5**2)     # 5 to the Power 2
print(5+2, 5-2, 5*2, 5/2, 5//2, 5%2, 5**2)  # Legend :)

                # Shortcuts
i = 10
# i = i + 2
i += 2  # i=i+2 shortcut ---> i += 2
i -= 2
i *= 2
i **= 2
print(i)

                # Operator Precedence

a = 2 + 3 * 5       # (*,/ has high priority than +,-)
b = (2 + 3) * 5     # (Put them in Brackets)
print(a, b)

