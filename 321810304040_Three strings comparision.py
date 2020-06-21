# Take 3 inputs from user and check :
           all are equal
           any of two are equal
           ( use and or )
 
 
str1=str(input("Enter first string:"))
str2=str(input("Enter second string:"))
str3=str(input("Enter third string:"))
if (str1==str2==str3):
      print("All Strings are equal")
elif (str1==str2 and (str1!=str3 or str2!=str3)):
    print("First and Second strings are equal")
elif (str1==str3 and (str1!=str2 or str3!=str2)):
    print("First and Third strings are equal")
elif (str2==str3 and (str2!=str1 or str3!=str1)):
    print("Second and Third strings are equal")
else:
    print("All strings are not equal")  