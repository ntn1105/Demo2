# Bài 5
# def soduongcuoicung(a):
#     soduong=0;
#     for num in a:
#         if num > 0:
#             soduong=num
#     return soduong

# a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# result = soduongcuoicung (a)
# print("Số dương cuối cùng", result)


#Bài 7
# a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]


# sorted_a = sorted(a, reverse=True)


# sothunhi = 0
# for num in sorted_a:
#     if num < max(a):
#         sothunhi = num
#         break


# for i in range (len(a)):
#     if a[i]==sothunhi:
#         print(i, end=' ')
        


#Bài 9
# def SUM(arr):
#     Tonglonnhat = 0  
#     soduonglientiep = 0  
#     sum=0 
#     for i in range (len(arr)):
#         if arr[i]>0:
#             soduonglientiep+=1
#             sum+=arr[i]
#         else :
#             soduonglientiep=0
#             sum=0
#         if Tonglonnhat<sum:
#             Tonglonnhat=sum
#     return soduonglientiep


        


# arr = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# soluong = SUM(arr)
# print("Số lượng các số dương liên tiếp có tổng lớn nhất:", soluong)

#Bài 1 
# arr = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# tong = sum(arr)
# print("Tổng các phần tử trong danh sách là:", tong)

#Bài 3
# arr = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# count=0

# sum1=0

# tong=sum(arr)/len(arr)
# print(tong)

# for num in arr:
#     if num>0:
#         count+=1
#         sum1+=num
            
# sum1=sum1/count
# print(sum1)
lst = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ").split(",")
k = int(input("Nhập phần tử thứ k muốn xóa: "))
if k <= len(lst):
    lst.pop(k-1)
    print("Danh sách mới là:", lst)
else:
    print("Không thể xóa phần tử thứ", k, "vì danh sách chỉ có", len(lst), "phần tử.")