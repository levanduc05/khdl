#10.1
numbers = [5, 2, 8, 1, 6]
max = max(numbers)
min = min(numbers)
print("Giá trị lớn nhất là:",max )
print("Giá trị nhỏ nhất là:",min)

#10.2
x = -10
tri_tuyet_doi  = abs(x)
print("|{x}| = ",tri_tuyet_doi)

#10.3
x = 2
n = 3
S = pow(x**2 + 1, n)
print("S = (x² + 1)^n =",S )

#10.4
x = 2
n = 3
A = pow(x**2 + x + 1, n) + pow(x**2 - x + 1, n)
print("A = (x² + x + 1)^n + (x² - x + 1)^n =", A)

#10.5
def zip_code_vn(zip_code):
    return len(zip_code) == 6 and zip_code.isdigit()
zip_code = "123456"
print(zip_code_vn(zip_code))

#10.6
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

deta = b**2 - 4*a*c

if deta > 0:
    x1 = (-b + math.sqrt(deta)) / (2*a)
    x2 = (-b - math.sqrt(deta)) / (2*a)
    print("Nghiệm x1 =", x1, "x2 =", x2)
elif deta == 0:
    x = -b / (2*a)
    print("Nghiệm kép x = ",x)
else:
    print("Phương trình vô nghiệm.")

#10.7
    s = "   hello world   "
s_sub = "o"
s_find = "world"
s_replace = "Python"

# In chuỗi s
print("Chuỗi s:", s)

# Loại bỏ khoảng trắng ở đầu và cuối chuỗi
s = s.strip()

# In chuỗi với ký tự đầu chuỗi viết hoa
print("Chuỗi viết hoa:", s.capitalize())

# Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
print("Số lần ",s_sub," xuất hiện trong chuỗi s:", s.count(s_sub))

# Tìm kiếm s_find trong s và thay thế bằng s_replace
s = s.replace(s_find, s_replace)
print("Chuỗi sau khi tìm kiếm và thay thế:", s)

#10.8
from datetime import datetime
# Nhập vào ngày, tháng, năm (hợp lệ)
ngay = int(input("Ngày: "))
thang = int(input("Tháng: "))
nam = int(input("Năm: "))

# Xuất ngày theo định dạng ngày - tháng - năm
date = datetime(ngay,thang,nam)
dinh_dang_ngay= date.strftime("%d-%m-%Y")
print("Ngày theo định dạng ngày - tháng - năm:", dinh_dang_ngay)

# Cho biết năm được nhập vào có phải là năm nhuận hay không
nam_nhuan  = (nam,"% 4 == 0 and year % 100 != 0) or (year % 400 == 0")
print("Năm", nam ,"là năm nhuận:",nam_nhuan )

# Cho biết ngày/tháng/năm nhập vào là thứ mấy
ngay = date.strftime("%A")
print("Ngày ",dinh_dang_ngay,"là thứ ",ngay)

# Cho biết tháng nhập vào có bao nhiêu ngày
so_ngay = (date.replace(month=date.month % 12 + 1, day=1) - date).days
print("Tháng",thang,"có ",so_ngay,"ngày.")

