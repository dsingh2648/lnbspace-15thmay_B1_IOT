                            ## Question1: to print all even numbers from a given numbers list

print("Solution 1: to print all even numbers")
print()
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for i in numbers:
    if i==237:
        break
    elif i%2==0:
        print(i)
print("__"*30)
print()

#-------------------------------------------------------------------------------------------------------------------------------------

                    ## Question2: print out all colour of color_list_1 which are not present in color_list_2.

print("Solution 2: print out all colour of color_list_1 ")
print()

colour_list_1=set(["White","Black","Red"])
colour_list_2=set(["Red","Green"])
print(colour_list_1.difference(colour_list_2))
print("__"*30)
print()

#-----------------------------------------------------------------------------------------------------------------------------------

                        ## Question3: the given input string is Pangram or no.

print("Solution 3: the given input string is Pangram or no.")
print()

def pangram(st):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for char in alpha:                                                                          
        if char not in st.lower():
            print("The string is not pangram!!")
            return
    else:
            print("The string is pangram!!")
sentence=pangram(input("Enter any sentence: "))
print("__"*30)
print()
#-----------------------------------------------------------------------------------------------------------------------------------
                        ## Question4: computes the value of n+nn+nnn.
print("Solution 4:computes the value of n+nn+nnn.")
print()

def integer(n):
    a=n
    b=n*11
    c=n*111
    sum=a+b+c
    print ("The value is: ",sum)     
value=integer(int(input("Enter any integer: ")))
print("__"*30)
print()
#-------------------------------------------------------------------------------------------------------------------------
                        ##Question5: take input from console in following fashion 23 54 12#98 3 17 and generate 2 list
print("Solution 5:Take input from console in following fashion")
print()
str = input('Enter the string : ')
l = str.split('#')
X = l[0].split()
Y = l[1].split()
X = [int(i) for i in X]
Y= [int(i) for i in Y]

print("list1:",X)
print("list2:",Y)
print("__"*30)
print()
#--------------------------------------------------------------------------------------------------------------------------
                        ## Question6: prints the words in a comma-separated sequence after sorting them alphabetically

print("Solution 6:prints the words in a comma-separated")
print()

def arrange(str):
        words= str.split(",")
        words.sort()
        print((",").join(words))
all_word=arrange(input("Enter different words seperate by comma: "))
print("__"*30)
print()
#------------------------------------------------------------------------------------------------------------------
                        ## Question7: find the name of person obtained highest marks

print("Solution 7: the name of person obtained highest marks ")
print()
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakh'],'Marks': [57,87,67,79]}
marks_list = d['Marks']
max_marks = max(marks_list)
max_marks_index = marks_list.index(max_marks)

student_list = d['Student']
print(d)
print('Student with maximum marks : ',student_list[max_marks_index])
print("__"*30)
print()
#--------------------------------------------------------------------------------------------------------------

                        ## Question8: calculate the number of letters and digits.
print("Solution 8: calculate the number of letters and digits")
print()
string = input("Please Enter your Own String : ")
alphabets = digits =0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
        
print("\nLetters :  ", alphabets)
print("Digit:  ", digits)
print("__"*30)
print()
#-------------------------------------------------------------------------------------------------------------

                    ## Question9: function which creates a new dictionary of students from a given

print("Solution 9: function which creates a new dictionary of students from a given")
print()
d = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

d1 = {'Name' : [],'Ratings' : []}
index = 0
for sub in d['Subject']:
    if(sub == 'Python'):
        d1['Name'].append(d['Name'][index])
        d1['Ratings'].append(d['Ratings'][index])
    index += 1 

print('New dictionary: ',d1)
print("__"*30)
print()
#---------------------------------------------------------------------------------------------------------------

                        ## Question10: Define a class with generator
print("Solution 10: class with a generator which can iterate")
print()
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
generate=putNumbers(int(input("enter any number:")))
for i in generate:
    print(i)
print("__"*30)
print()
#-----------------------------------------------------------------------------------------------------------

                        ## Question11: to compute the distance from current position of robot

print("Solution 11: to compute the distance from current position of robot")
print()
import math
pos=[0,0]
moves={"UP":[0,1],
       "DOWN":[0,-1],
       "LEFT":[-1,0],
       "RIGHT":[1,0]}
data=["UP 5",
    "DOWN 3",
    "LEFT 3",
    "RIGHT 2"]
for inp in data:
    parts=inp.split()    
    mv=parts[0]
    val=parts[1]
    if mv in moves and val.isnumeric():
        pos[0] += moves[mv][0]*int(val)
        pos[1] += moves[mv][1]*int(val)    
distance=math.sqrt(pos[0]**2 + pos[1]**2)
print("The distance is: ",int(distance))
print("__"*30)
print()
#---------------------------------------**********END********--------------------------------------------------------


