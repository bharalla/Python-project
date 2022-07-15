# #decorators or wrapper function -- nested functions
#
# def sum(func):
#     # import pdb
#     # pdb.set_trace()
#     def inner(*args):
#
#         print(func(*args))
#         return ("do something")
#     return inner
#
#
# @sum
# def mul(c,d,**kwargs):
#     print("mul")
#     return c,d
#
# m = mul(1,2)
# print(m)
#
# # pickle and unpickle
# import pickle
#
#
# class emp:
#
#     def sal(self,name,age):
#         self.name = name
#         self.age = age
#
#
# e = emp()
#
# with open("hi.dat",'wb') as f:
#     pickle.dump(e,f)
#
# with open("hi.pkl") as f:
#     e = pickle.load(f)

# l = [1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 10]
# l1 = []
# min = l[0]
# while list:
#
#     for i in l:
#         if i<min:
#             min = i
#     l1.append(min)
#
# print(l1)
# import pdb
# pdb.set_trace()
#
#
# def arguments(*args, **kwargs):
#     # print(*args,**kwargs)
#     for i, j in kwargs.items():
#         print(i,j)
#
#
# # kwargs = {1:'20',2:'Ram',3:'hello'}
# arguments((10, 20, 30, 40), {1: '20', 2: 'Ram', 3: 'hello'})
# l = 10, 22, 33, 121, 45, 10
# l1 = []

# def my_fun(*args):
#     # import pdb
#     # pdb.set_trace()
#     for i in args:
#         l1.append(i)
#     if l1[0]==l1[1]:
#         print(f'substraction of {l1[0]} and {l1[1]} is zero')
#     else:
#         print('multiplication :', l1[0]*l1[1])
#     print(l1)
#
#     # if l1[0] == l1[1]:
#     #     print('substraction is zero')
#     # else:
#     #     print('multiplication :' , l1[0] * l1[1])
#
#
# my_fun(10,10, 33, 121, 45, 10)
#
# def fun(n): # factorial number by using recursive function
#     import pdb
#     pdb.set_trace()
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fun(n-1)
# print(fun(5))

# l=[]
# try:
#
#     print(l[0])
# except Exception as msg:
#     # if msg == "list index out of range":
#     #     print('please provide list elements')
#     print(msg)

# import openpyxl
# # import pyexcel
#
# filename = openpyxl.load_workbook('C:/Users/Administrator/Desktop/test.xlsx')
# filename.get_sheet_by_name()

s = '''eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'''

























