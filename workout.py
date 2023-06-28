# list = [1, 3, 2, 2, 3, 0]
# x = 0
# for i in range(len(list)):
#     if list[i] != 0:
#         list[i], list[x] = list[x], list[i]
#         x += 1
# print(list)
# list1 = [1, 2, 3]
# list2 = [2, 5, 6]
# list3 = []
# i = j = 0
# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         list3.append(list1[i])
#         i += 1
#     else:
#         list3.append(list2[j])
#         j += 1
# while i < len(list1):
#     list3.append(list1[i])
#     i += 1
# while j < len(list2):
#     list3.append(list2[j])
#     j += 1
# print(list3)
# list = [2, 7, 11, 15]
# indices = []
# target = 18
# for i in range(len(list)-1):
#     found = False
#     for j in range(1, len(list)):
#         if list[i]+list[j] == target:
#             indices.append(i)
#             indices.append(j)
#             found = True
#     if found:
#         break
# print(indices)
# def lists_sum_list(list1, list2):
#     str1 = str2 = ""
#     for i in list1:
#         str1 += str(i)
#     for j in list2:
#         str2 += str(j)
#     sumstr = list(str(int(str1)+int(str2)))
#     for i in range(len(sumstr)):
#         sumstr[i] = int(sumstr[i])
#     print(sumstr)


# list1 = [1, 5, 9]
# list2 = [8, 0, 2]
# lists_sum_list(list1, list2)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert(self, list):
#         for i in list:
#             newnode = Node(i)
#             if self.head is None:
#                 self.head = self.tail = newnode
#             else:
#                 newnode.next = self.head
#                 self.head = newnode

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, "-->", end=" ")
#             current = current.next
#         print()

#     def tonumber(self):
#         str1 = ""
#         current = self.head
#         while current:
#             str1 += str(current.data)
#             current = current.next
#         num = int(str1[::-1])
#         return num


# list1 = [1, 5, 9]
# list2 = [8, 0, 2]
# ll1 = Linkedlist()
# ll2 = Linkedlist()
# ll1.insert(list1)
# ll1.display()
# num1 = ll1.tonumber()
# ll2.insert(list2)
# ll2.display()
# num2 = ll2.tonumber()
# ll3 = Linkedlist()
# sumstr = list(str((num1+num2)))
# for i in range(len(sumstr)):
#     sumstr[i] = int(sumstr[i])
# ll3.insert(sumstr)
# ll3.display()
# str = str(int(input("Enter a number ")))
# print("number is  palindrome") if str == str[::-
#                                              1] else print("number is not palindrome")
# list = [1, 2, 3, 4]
# list1 = []
# sum = 0
# for i in list:
#     sum += i
#     list1.append(sum)
# print(list1)
# list = [1, 22, 55, 8]


# def elementsum(list):
#     sum = 0
#     for i in list:
#         sum += i
#     print(sum)


# def digitsum(list):
#     sum = 0
#     str1 = ''
#     for i in list:
#         str1 += str(i)
#     for i in range(len(str1)):
#         sum += int(str1[i])
#     print(sum)


# elementsum(list)
# digitsum(list)
# def isPowerOfTwo(n):
#     while n > 2:
#         n = n / 2
#         print(n)
#     if n == 2 or n == 1:
#         return True
#     return False


# print(isPowerOfTwo(3))
# def commonFactors(a, b):
#     if a < b:
#         c = a
#     else:
#         c = b
#     count = 0
#     for i in range(1, c+1):
#         if a % i == 0 and b % i == 0:
#             count += 1
#     return count


# print(commonFactors(12, 6))
# k = int(input("enter the number of the rotation"))
# list = [1, 2, 3, 4, 5, 6, 7]
# list = list[-k:]+list[:-k]
# print(list)
nums=[0,0,1,1,1,2,2,3,3,4]
for i in range(len(nums)-1):
    while i < len(nums)-1:
         if nums[i]==nums[i+1]:
              nums[i]='_'
              i+=1     
print(nums)
