xau_ki_tu = input("Nhập một xâu kí tự: ")

try:
    so_thap_phan = float(xau_ki_tu)
    print("Số thập phân tương ứng là:", so_thap_phan)
except ValueError:
    print("Không thể chuyển đổi xâu thành số thập phân.")


    so_thap_phan = float(input("Nhập một số thập phân: "))
xau_ki_tu = str(so_thap_phan)
print("Xâu kí tự tương ứng là:", xau_ki_tu)