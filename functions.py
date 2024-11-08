# def even_odd():
#     user_input = int(input("write any no :"))
#     if  user_input % 2 == 0:
#      print("it is even no ")
#     else:
#      print("it is odd")

# even_odd()    
# print(even_odd)
# parameters:
# #a,b is the parameters and values are arguments  
# def sum(x,y=2):#default variable make on the end 
#     z= x + y # return is a function killer is ke neeechay wala code ni chalay ga , it is like break in loop 
#     return z
# num1 = int(input("enter the no 1:"))
# num2 = int(input("enter the no 2:")) 
# print(sum())
# types of python arguments :  
# default Arguments : 
# def intro(name,age,grade,city,degree):
#     print(f"My name is {name} and my age is {age} and my grade is  {grade} and my city is {city} and my degree is {degree}")
# #positioning argument:
# intro("mujtaba","20","A","lahore","Bscs")
# #keyword argument:
# intro(degree="bscs", city="lahore",grade="A",name="mujtaba",age="20")
# arbitary arguments :
# def add(*args):   #simple arbitrary arguments(args)
#     print(args)#it return an tuple 
# print(add(1,2,4,5))
# #keyword arbitrary argument (kargs):
# def mix(**kargs):   #simple arbitrary arguments(args)
#     for x,y in kargs.items():
#         print(f"{x} = {y}")#it returs us dictionary 
# mix(a=1,b=2,c=4,d=5) 
# add = lambda x , y : x + y
# print(add(2,8))
# #docstring : 
# """hello how are you"""#its act like the comments that descrbes the functionality in the function we can also print it 
# print(print.__doc__)
# #assignment: 
# #write a function to reverse a string from user input 
# #write a function to count the vowel from user input 
# #1. 
# def count_vowel():
#     string = str(input("enter the string : "))
#     vowels = "aeiou"
#     vowels_count = 0
#     string = string.lower()

#     for char in string:
#         if char in vowels:
#             vowels_count +=1
#     print(vowels_count)
    
# count_vowel()
# #2.
# def reverse_string():
#     user_input = str(input("enter the string:"))
#     reversed = user_input[::-1]
#     print(reversed)
# reverse_string()

            
