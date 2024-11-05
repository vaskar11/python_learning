# l=[]
# a= input('enter name: ')
# b= input('enter address: ')
# l.append(a)
# l.append(b)
# print(l)


# f= open('abc.txt','r')
# print("The file that is opend is: ", f.name)
# print('Ths file mode is: ',f.mode)
# print('Ths file mode is: ',f.closed)
# print('Is file readable? ', f.readable())
# print('Is file writable? ', f.writable())
# f.close()
# print('Ths file mode is: ',f.closed)

# # f.write()
# f= open('abc.txt','w')
# f.write("Bhaskar\n")
# f.write("Dipesh\n")
# f.write("Nikita\n")
# f.write("Isha\n")
# f.write("Pragyan\n")
# print("written in file successfully")
# f.close()

# #f.writelines(list_of_lines)
# f= open('abc.txt','w')
# list= ["Bhaskar","Dipesh","Ayush","Pragyan"]

# f.writelines(list)
# print("I think data is written on file")
# f.close()

# writting in a file
# fname= input("Enter the file name you want: ")
# f=open(fname,'w')
# while True:
#     data= input("enter data you want to add to file ")
#     f.write(data + "\n")
#     option= input("Do you want to add more data(yes/no): ")
#     if option.lower() == 'no':
#         break
# f.close()
# print("data return successfully")
    
# # # reading from files
''' 2 ways:
f.read(): read total data
f.read(n): read n character from a file
f.readline(): it read one line at a time
f.readline(): it read multiple line at a time

'''
# f= open("abc.txt",'r')
# data= f.readline()
# print(data)
# data1= f.readline()
# print(data1)
# f.close()

# f= open("abc.txt",'r')
# line= f.readline()
# while line!= " ":
#     print(line,end=' ')
#     line= f.readline()
# f.close()

# f= open('abc.txt','r')
# lines= f.readlines()
# print(lines)
# for line in lines:
#     print(line, end="")
# f.close()


# a= input("Enter the name of file from which you want to read: ")
# b= input("Enter the name of file in which you want to write: ")

# f1= open(a,'r')
# f2= open(b,'w')
# data= f1.read()
# f2.write(data)
# print("File read and write succesfully")
# f1.close()
# f2.close()

''' there is one way not to close file everytime while we open . we can open using with statement so that it is not compulsary to close that file'''

# #f1= open('abc.txt','w')  this is same to with method
# with open('abc.txt','w') as f1:
#     f1.write('I have written something')
#     print('Is file closed? ',f1.closed)
# print('Is file closed? ',f1.closed)

# f= open('abc.txt','r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())

# import os,sys
# fname= input("Enter the file name: ")
# if os.path.isfile(fname):
#     print(fname," is in our system. ")
#     f= open(fname,'r')
#     data= f.read()
#     print(data)
#     f.close()
# else:
#     print("file doesnot exist. ")
#     sys.exit(0)
    
    
''' finding number of character,words and line in a file'''

import os,sys
fname= input("Enter the file name: ")
if os.path.isfile(fname):
    print(fname," is in our system. ")
    lcount=0 
    wcount=0
    ccount=0
    f= open(fname,'r')
    for line in f:
        lcount+=1
        no_of_words= len(line.split())
        wcount= wcount+ no_of_words
        no_of_character= len(line)
        ccount+= no_of_character
    
    f.close()
else:
    print("file doesnot exist. ")
    sys.exit(0)

print("Number of lines: ",lcount)
print("Number of words: ",wcount)
print("Number of character: ",ccount)
