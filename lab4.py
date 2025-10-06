def tinh_tien_nuoc(khoi_nuoc):
    if khoi_nuoc <= 10:
        tien = khoi_nuoc * 7500
    elif khoi_nuoc <= 20:
        tien = 10 * 7500 + (khoi_nuoc - 10) * 8800
    elif khoi_nuoc <= 30:
        tien = 10 * 7500 + 10 * 8800 + (khoi_nuoc - 20) * 12000
    else:
        tien = 10 * 7500 + 10 * 8800 + 10 * 12000 + (khoi_nuoc - 30) * 24000
    return tien


def tinh_nguyen_lieu(dau_xanh, thap_cam, deo):
    # Tính lượng đường
    duong = dau_xanh * 0.04 + thap_cam * 0.06 + deo * 0.05
    # Tính lượng đậu
    dau = dau_xanh * 0.07 + thap_cam * 0.04 + deo * 0.02

    # Kết quả trả về dạng dictionary
    nguyen_lieu = {
        "Đường": duong,
        "Đậu": dau
    }

    return nguyen_lieu

import math
import datetime
def tong(a, b):
    ket_qua = a + b
    return ket_qua

def hieu(a, b):
    ket_qua = a - b
    return ket_qua

def tich(a, b):
    ket_qua = a * b
    return ket_qua

def thuong(a, b):
    if b == 0:
        return
    ket_qua = a/b
    return ket_qua

def luy_thua(a, b):
    ket_qua = a ** b
    return ket_qua

def can_bac2(a):
    if a < 0:
        return
    ket_qua = math.sqrt(a)
    return ket_qua

def sin(a):
    ket_qua = math.sin(a)
    return ket_qua

def cos(a):
    ket_qua = math.cos(a)
    return ket_qua

def tan(a):
    ket_qua = math.tan(a)
    return ket_qua

def log10(a):
    ket_qua = math.log10(a)
    return ket_qua

def ln(a, b):
    ket_qua = math.log(a, b)
    return ket_qua

def log(a):
    ket_qua = math.log(a)
    return ket_qua

def pt_1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b/a

def pt_2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm" 
            else:
                return "Phương trình vô nghiệm"
        else:
            return -c/b
    else:     
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
        else:
            return "Phương trình vô nghiệm"

def check_history(History):
    if len(History) == 0:
        return "Lịch sử trống, chưa có chức năng nào được chọn"
    else:
        return "======Lịch sử======\n"
        for i, j in enumerate(History, start = 1):
            return f"{i}. {j}\n"

def thoi_gian():
    return datetime.datetime.now().strftime("%d/%M/%Y %H:%M:%S")
