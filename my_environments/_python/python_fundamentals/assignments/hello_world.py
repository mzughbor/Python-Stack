# 1. TASK: print "Hello World" 
print("Hello World") 

# 2. print "Hello Noelle!" with the name in a variable 
name = "Noelle"
print("Hello ", name, "!")    # with a comma 
print("Hello " + name, "!")    # with a + 

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name, "!")    # with a comma
#print("Hello" + name, "!")    # with a +    -- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables 
fave_food1 = "sushi" 
fave_food2 = "pizza" 
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format() 
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

# Bonus .. string methods 
text = "Mahmoud Said :)"
print(text.upper())
print(text.lower())
print(text.count("d"))

print(text.split("d")) #['Mahmou', ' Sai', ' :)'] or no given value will behave as normal split by space
print(text.find("d"))

print("Company%".isalnum(), "Company 12".isalnum(), "Company12".isalnum())

print("Company%".isalnum(), "Company 12".isalnum(), "Company12".isalnum()) # other one isdigit()

print("Company ".isalpha(), "Company$".isalpha(), "Company12".isalpha())

list = ["f", "Mahmoud", "Lara", "Sohada"]
x = " ".join(list)
#x = " ".join(list)
print(x)

print(x.endswith("hadA")) # key sensitave...
print(x.endswith("hada"))

