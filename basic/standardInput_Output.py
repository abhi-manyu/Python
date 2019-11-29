------------------------------------------------------------------------------------------------------
#  In python version : 2
------------------------------------------------------------------------------------------------------

name = raw_input()  #here bydefault the input is string type so to check there is one method in python.
#   using type(instance)---------> gives the type of that instance,   so here if we write ,

print(type(name)) #    ------------> <class 'str'> that means the variable 'name' is string type.

sys.stdout.write('Hiiii {}'.format(name))
----------------------------------------------------------------------------------------------------------------

#   if we will take a simmple input, and by default it is a string type, and use it as the int or float type , then we will get exception.
#   For that we need to convert that into our required type as bellow : 

age = raw_input();
sys.stdout.write('after 5 yr later , ur age will be {}'.format(age+5));  #    here i m trying to add 5 to the age variable as int type.
                                               #    But it will through error or exception, cuz defaultly it is string type, and that is not possible.

#    So to avaoiding that situation we need to convert the variable from string to int or float type.
   
age = int(raw_input())   #    Now it is converted into int type and we can use 'age' as integer type
print(type(age))    #-------------->   <class 'int'>   that means now it is showing age as integer type

sys.stdout.write('after 5 years later ur age will be {}'.format(age+5))
---------------------------------------------------------------------------------------------------------------------



---------------------------------------------------------------------------------------------------
In Python 3 , there is no certain method like raw_input(),
---------------------------------------------------------------------------------------------------

in python 3 if we want to take any input , just write:  
                                                       input() , thats enough
or if we want to take input after showing some instruction, then write :
                                                     name =  iput('enter ur name please')
#   Here also by default value taken is string only, so we can't use that as integer or float directly,
#   if we want then first we hav to convert it into int or float type , then use it


age = input('enter ur age')
print(type(age))    # ---------->   <class 'str'>   that means string type, so
sys.stdout.write('after 10 yrs ur age will be {}'.format(age+10))    # ---------error or exception, that is impossible

# so we need to convrt first as bellow

age = int(input('enter ur age'))  #   here it will auto converted into int type.
print(type(age))   #-------->    <class 'int'>  that means int type

sys.stdout.write('ur age after 10 yrs will be {}'.format(age+10))    #---------  correct output






