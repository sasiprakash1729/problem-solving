# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insertAtFront(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#
#     def insertAtEnd(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             cur_node = self.headcaca
#             while cur_node.next:
#                 cur_node = cur_node.next
#
#             cur_node.next = Node(data)
#
#     def insertAtPosition(self, data, pos):
#         if (pos < 0 or pos > self.length() - 1):
#             print("out of range")
#         elif (pos ==  0):
#             self.insertAtFront(data)
#         elif (pos == self.length() - 1):
#             self.insertAtEnd(data)
#         else:
#             p = 0
#             cur = self.head
#             prev = self.head
#
#             while cur:
#                 if (pos == p):
#                     new = Node(data)
#                     t = prev.next
#                     prev.next = new
#                     new.next = t
#                     break
#
#                 else:
#                     prev = cur
#                     cur = cur.next
#                     p += 1
#
#     def printLL(self):
#         if (self.head is None):
#             print("list is empty")
#         else:
#             current_node = self.head
#             while (current_node):
#                 print(current_node.data, end=" ")
#                 current_node = current_node.next
#
#     def length(self):
#         cur = self.head
#         l = 0
#         while cur:
#             l += 1
#             cur = cur.next
#         return l
#
#     def deleteAtFront(self):
#         if self.head is not None:
#             t = self.head
#             self.head = self.head.next
#             del t
#
#
#     def deleteAtEnd(self):
#         if self.head.next is None:
#             self.head = None
#         else:
#             cur = self.head
#             prev = cur
#             while cur.next:
#                 prev = cur
#                 cur = cur.next
#             t = cur
#             prev.next = None
#             del t
#     def deleteAtPos(self, pos):
#         if (pos < 0 or pos > self.length() - 1):
#             print("out of range")
#         elif pos == 0:
#             self.deleteAtFront()
#         elif pos == self.length() - 1:
#             self.deleteAtEnd()
#         else:
#             p = 0
#             cur = self.head
#             pre = cur
#             while 1:
#                 if (p == pos):
#                     t = cur
#                     pre.next = cur.next
#                     del t
#                     break
#                 else:
#                     pre = cur
#                     cur = cur.next
#                     p += 1
#     def reverse_list(self):
#         cur = self.head
#         prev = None
#
#         while cur:
#             cur_next = cur.next
#             cur.next = prev
#
#             prev = cur
#             cur = cur_next
#         self.head = prev
#     def merge_sorted_list(self, list1, list2, merge):
#         c1 = list1.head
#         c2 = list2.head
#
#         while c1 and c2:
#             if (c1.data < c2.data):
#                 merge.insertAtEnd(c1.data)
#                 c1 = c1.next
#             else:
#                 merge.insertAtEnd(c2.data)
#                 c2 = c2.next
#
#         while c1:
#             merge.insertAtEnd(c1.data)
#             c1 = c1.next
#
#         while c2:
#             merge.insertAtEnd(c2.data)
#             c2 = c2.next
#
#     def delete_last_ocrr_node(self, key):
#         self.reverse_list()
#         cur = self.head
#         p = cur
#         while cur:
#             if (cur.data == key):
#                 if (cur is self.head):
#                     self.deleteAtFront()
#                 else:
#                     p.next = cur.next
#                     cur = cur.next
#                 break
#             else:
#                 p = cur
#                 cur = cur.next
#
#     def rotate_list(self, k):
#         k = k % self.length()
#         cur = self.head
#         while k > 0:
#             self.insertAtEnd(cur.data)
#             t = cur.next
#             self.deleteAtFront()
#             cur = t
#             k -= 1
#
#     def find_nth_node(self, pos):
#         self.reverse_list()
#         cur = self.head
#         p = 1
#         while cur:
#             if (pos == p):
#                 print(cur.data)
#                 break
#             else:
#                 cur = cur.next
#                 p += 1
#
#     def delete_middlie_node(self):
#         cur = self.head
#         prev = cur
#         l = self.length() // 2
#         while (l > 0):
#             prev = cur
#             cur = cur.next
#             l -= 1
#         prev.next = cur.next
#
#     def remove_duplicates_sorted(self):
#         cur = self.head
#         while cur.next:
#             if (cur.data == cur.next.data):
#                 t = cur.next.next
#                 cur.next.next = None
#                 cur.next = t
#             else:
#                 cur = cur.next
#
#     def check_palindrome(self):
#         if (self.head is None):
#             return None
#         else:
#             cur1 = self.head
#             k = 0
#             self.reverse_list()
#             cur2 = self.head
#             while cur1 and cur2:
#                 if (cur1.data != cur2.data):
#                     k = -1
#                     break
#                 else:
#                     cur1 = cur1.next
#                     cur2 = cur2.next
#             if (k == -1):
#                 print("false")
#             else:
#                 print("true")
#
#     def palindrome(self):
#         l = self.length()
#         l1 = l // 2
#         bm = None
#         am = None
#         cur = self.head
#
#         while l1 > 0:
#             if (bm is None):
#                 bm = cur
#             else:
#                 bm.next = cur
#             cur = cur.next
#             l1 -= 1
#
#         t = cur.next
#         cur.next = None
#         l1 = l // 2
#
#         while l1 > 0:
#             if (am is None):
#                 am = t
#                 t = t.next
#             else:
#                 am.next = t
#                 t = t.next
#             l1 -= 1
#
#         while am:
#             print(am.data)
#             am = am .next
# list1 = LinkedList()
# list1.insertAtEnd(1)
# list1.insertAtEnd(2)
# list1.insertAtEnd(3)
#
# list2 = LinkedList()
# list2.insertAtEnd(4)
# list2.insertAtEnd(5)
# list2.insertAtEnd(6)
#
# merge = LinkedList()
# merge.merge_sorted_list(list1, list2, merge)
# merge.printLL()
#
# #sorting algorithms
#
# # arr = [5, 4, 3, 2, 1, 0]
# # n = len(arr)
# # #bubble sort
# # def bubble_sort():
# #     for i in range(n - 1):
# #         for j in range(i + 1, n):
# #             if (arr[i] > arr[j]):
# #                 t = arr[i]
# #                 arr[i] = arr[j]
# #                 arr[j] = t
# # #selection sort
# # def selction_sort():
# #     for i in range(n - 1):
# #         m = i
# #         for j in range(i + 1, n):
# #             if (arr[j] < arr[m]):
# #                 m = j
# #         t = arr[i]
# #         arr[i] = arr[m]
# #         arr[m] = t
# #
# # #insertion sort
# # def insertion_sort():
# #     for i in range(1, n):
# #         m = i
# #         while arr[m] < arr[m - 1] and m > 0:
# #             t = arr[m]
# #             arr[m] = arr[m - 1]
# #             arr[m - 1] = t
# #             m -= 1
# #
# # def merge(l, m, h):
# #     n1 = m - l + 1
# #     n2 = h - m
# #
# #     L = [0] * n1
# #     R = [0] * n2
# #
# #     for i in range(n1):
# #         L[i] = arr[l + i]
# #     for i in range(n2):
# #         R[i] = arr[m + 1 + i]
# #
# #     i = 0
# #     j = 0
# #     k = l
# #
# #
# #     while i < n1 and j < n2:
# #         if (L[i] <= R[j]):
# #             arr[k] = L[i]
# #             i += 1
# #         else:
# #             arr[k] = R[j]
# #             j += 1
# #         k += 1
# #
# #     while i < n1:
# #         arr[k] = L[i]
# #         i += 1
# #         k += 1
# #
# #     while j < n2:
# #         arr[k] = R[j]
# #         j += 1
# #         k += 1
# # #megre sort
# # def merge_sort(l, h):
# #     if (l < h):
# #         m = (l + h) // 2
# #         merge_sort(l, m)
# #         merge_sort(m + 1, h)
# #         merge(l, m, h)
# # #quick sort
# # def quick_sort(l, r):
# #     if (l < r):
# #         pivot = l
# #         i = l + 1
# #         j = r
# #
# #         while (i < j):
# #             while arr[i] < arr[pivot]:
# #                 i += 1
# #             while arr[j] > arr[pivot]:
# #                 j -= 1
# #             if (i < j):
# #                 t = arr[i]
# #                 arr[i] = arr[j]
# #                 arr[j] = t
# #         t = arr[pivot]
# #         arr[pivot] = arr[j]
# #         arr[j] = t
# #         quick_sort(l, j - 1)
# #         quick_sort(j + 1, r)
# #
# # quick_sort(0, n - 1)
# # print(arr)
#
# divide and conquer

# a = [3, 4, 5, 9, 0]
# def find_min(l, h):
#     if (l == h):
#         return a[l]
#     elif (l == h - 1):
#         if (a[l] < a[h]):
#             return a[l]
#         return a[h]
#     elif (l < h):
#         m = (l + h) // 2
#         left = find_min(l, m)
#         right = find_min(m + 1, h)
#     return min(left, right)
#
# print(find_min(0,  len(a) - 1))


#prefix
#strs = ["flower","flow","flight"]
# strs = ["dog","dacecar","dar"]
# c = len(strs[0])
# inx = strs[0]
# for i in strs:
#     if (len(i) < c):
#         c = len(i)
#         inx = i
#
# inx = strs.index(inx)
# h = 0
# k = strs[inx]
# s = ""
# for i in range(c):
#     for j in range(len(strs)):
#         if (j != inx):
#             z = strs[j]
#             if (z[i] != k[i]):
#                 h = 1
#                 break
#     if (h == 0):
#         s += k[i]
#
# print(s)

#dynamic programming
#climbing stairs
#n = 2 -> 2
#n = 3 -> 3
#n = 5 -> 5
# n = 3
# c = 0
# if (n % 2 == 0):
#     c += 2
# else:
#     c += 1
#
# h = n // 2


# divide and conquer

# def find_min(l, h):
#     if (l == h):
#         return a[l]
#     elif (l == h - 1):
#         if (a[l] < a[h]):
#             return a[l]
#         return a[h]
#     elif (l < h):
#         m = (l + h) // 2
#         left = find_min(l, m)
#         right = find_min(m + 1, h)
#     return min(left, right)
#
#
# a = [0, 3, 4, 6, 2, 0]
# def no_of_zeros(l, h):
#     c = 0
#     if (l < h):
#         m = (l + h) // 2
#         l1 = no_of_zeros(l, m)
#         r1 = no_of_zeros(m + 1, h)
#         if (l1 == 0):
#             c += 1
#         elif (r1 == 0):
#             c += 1
#     return c
# print(no_of_zeros(0, len(a) - 1))

arr = [5, 3, 4, 2, 1]
s = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if (arr[i] + arr[j] > s):
                s = arr[i] + arr[j]
print(s)