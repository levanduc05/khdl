#11.1
a = [1, 2, 3]
len_a = len(a)
print("Độ dài của danh sách a là:", len_a)
#..........................................
b = [1, [2, 3]]
len_b = len(b)
print("Độ dài của danh sách b là:", len_b)
#..........................................
c = []
len_c = len(c)
("Độ dài của danh sách c là:", len_c)
#.........................................
d = [1, 2, 3][1:]
len_d = len(d)
print("Độ dài của danh sách d là:", len_d)

#11.2
# Danh sách các đội (thứ tự giảm dần từ đội tốt nhất)
teams = [
    ["Huấn luyện viên A", "Đội trưởng A", "Cầu thủ 1", "Cầu thủ 2"],
    ["Huấn luyện viên B", "Đội trưởng B", "Cầu thủ 3", "Cầu thủ 4"],
   
]

# Chọn đội trưởng của đội tệ nhất
doi_truong_te = teams[-1][1]

# In ra tên đội trưởng của đội tệ nhất
print("Đội trưởng của đội tệ nhất là:", doi_truong_te)

#11.3

# Tạo danh sách các con thú
animals = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

# In ra danh sách các con thú và số lượng các con thú
print("List of animals:", animals)
print("Number of animals:", len(animals))

# Nhập vào con thú cần tìm
thu_dang_tim = input("\nI want to find:\n")

# Kiểm tra xem con thú có trong danh sách không và in kết quả
if thu_dang_tim in animals:
    print("There is", thu_dang_tim, "in list of animals")
else:
    print("There is no", thu_dang_tim, "in list of animals")

#11.8
def has_lucky_number(nums):
    """
    Kiểm tra xem danh sách các số có chứa số may mắn hay không.
    
    Parameters:
    - nums: danh sách các số
    
    Returns:
    - True nếu danh sách có chứa số may mắn, False nếu ngược lại.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

# Ví dụ 
numbers = [2, 6, 7, 9]
result = has_lucky_number(numbers)

print("Danh sách các số:", numbers)
print("Có chứa số may mắn hay không:", result)

#11.9
def tiec(nguoi_den, ten):
    """
    Kiểm tra xem một vị khách có đến trễ tiệc hay không.
    
    Parameters:
    - arrivals: danh sách các tên khách
    - name: tên của vị khách cần kiểm tra
    
    Returns:
    - True nếu vị khách đến trễ tiệc, False nếu ngược lại.
    """
    so_khach = len(arrivals)
    index_of_guest = arrivals.index(ten)
    
    return index_of_guest >= so_khach / 2 and index_of_guest != so_khach - 1

arrivals = ['duc','van','kduc','quan','duong']

name_to_check = 'duong'
result = tiec (arrivals, name_to_check)

print(name_to_check, "có đến trễ tiệc hay không:", result)

#11.10
def danh_sach_bua_an(meals):
    """
    Kiểm tra xem có bữa ăn liên tiếp nào nhàm chán hay không.
    
    Parameters:
    - meals: danh sách các bữa ăn
    
    Returns:
    - True nếu có bữa ăn liên tiếp nào nhàm chán, False nếu ngược lại.
    """
    for i in range(1, len(meals)):
        if meals[i] == meals[i - 1]:
            return True
    return False

# Ví dụ 
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']

result_1 = danh_sach_bua_an(meals_1)
result_2 = danh_sach_bua_an(meals_2)

print("Danh sách bữa ăn 1:", meals_1)
print("Có bữa ăn liên tiếp nào nhàm chán hay không:", result_1)

print("\nDanh sách bữa ăn 2:", meals_2)
print("Có bữa ăn liên tiếp nào nhàm chán hay không:", result_2)

#11.12
# Tạo tuple a chứa 4 số nguyên dương đầu tiên
a = (1, 2, 3, 4)

# Tạo tuple b chứa 4 số nguyên dương tiếp theo
b = (5, 6, 7, 8)

# Tạo tuple c là sự kết hợp của các phần tử trong tuple a và b
c = a + b

# Tạo tuple d từ tuple c với các phần từ được sắp xếp
d = tuple(sorted(c))

# In phần tử thứ 3 của d
print("Phần tử thứ 3 của d:", d[2])

# In 3 phần tử cuối cùng của d
print("3 phần tử cuối cùng của d:", d[-3:])

    