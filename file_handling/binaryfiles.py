# f1= open('ticket.png','rb')
# f2= open('new.png','wb')
# a= f1.read()
# f2.write(a)
# print('I hope image is copied')

# import csv
# with open('emp.csv','w',newline='') as f:
#     w= csv.writer(f)
#     # print(type(w))
#     w.writerow(['E-num','Name','Salary','Address'])
#     n= int(input('Enter number of employees: '))
#     for i in range(n):
#         eno= input('Enter employee number: ')
#         name= input('enter name: ')
#         salary= input('enter salary: ')
#         add= input('Enter address: ')
#         w.writerow([eno, name, salary, add])

# print("our csv file is created")


# import csv
# f= open('emp.csv','r')
# r= csv.reader(f)
# data= list(r)
# for line in data:
#     for words in line:
#         print(words, end=' ')
#     print()


'''zipping and unzipping of files'''

from zipfile import *
'''Zipping'''
# f= ZipFile('files.zip','w',ZIP_DEFLATED)
# f.write('file1.txt')
# f.write('file2.txt')
# f.write('file3.txt')
# f.write('file4.txt')
# f.close()
# print('My files.zip is created. You can check it. ')

'''unzipping'''
# f= ZipFile('files.zip','r',ZIP_STORED)
# names= f.namelist()
# for name in names:
#     print("Unzipped files are: ",name)
#     print("COntent of files are:")
#     f1= open(name,'r')
#     print()


'''working with directories'''
# #to know current working directory
# import os
# cwd= os.getcwd()
# print('My current working directory is: ',cwd)

import os
# os.makedirs("my_sub_dir/subdir/bhaskar")
# os.rmdir('my_sub_dir/subdir/bhaskar')
# os.removedirs('my_sub_dir/subdir')
# print("deleted")

# os.rename('sub_dir','new_sub_dir')
# print("renamed")

# l= os.listdir('file_handling')
# print(l)

# g= os.walk("file_handling")
# for x in g:
#     print(x)

# for dirpath, dirname,filename in os.walk('.'):
#     print('current dir path: ',dirpath)
#     print('current dir name: ',dirname)
#     print('current file name: ',filename)
#     print()

# os.system('notepad')

stats= os.stat('abc.txt')
print(stats)


