from lab4module import *
class Maytinhbotui:
    def __init__(self):
        self.History = []
        
    def hien_menu(self):
        self.menu = {
            0: "Thoát",
            1: "Tính cộng trừ nhân chia",
            2: "Tính lũy thừa",
            3: "Tính căn bậc 2 ",
            4: "Tính hàm lượng giác",
            5: "Tính logarit",
            6: "Giải phương trình bậc 1",
            7: "Giải phương trình bậc 2",
            8: "Xem lịch sử sử dụng",
            9: "Xem đồng hồ"
        }
        print("="*24+"MENU CHƯƠNG TRÌNH"+"="*23)
        for self.key , self.value in self.menu.items():
            print(f"| {self.key} : {self.value} {(55 - len(self.value)) * ' '} |")
        print("="*64)
    def thuc_hien_chuc_nang(self):

        while True:
            try:
                self.lua_chon = int(input("Chọn chức năng chương trình 0-9:"))
                if self.lua_chon == 0:
                    break
                if self.lua_chon == 1:
                    nhap_a = float(input("Nhập hệ số a: "))
                    nhap_b = float(input("Nhập hệ số b: "))
                    chon_chuc_nang = input("Nhập chọn chức năng: +, -, *, /")

                    if chon_chuc_nang == "+":
                        print(f"Tổng = {tong(nhap_a, nhap_b)}")
                        self.History.append(f"Phép tính cơ bản: Tổng = {tong(nhap_a, nhap_b)}")

                    elif chon_chuc_nang == "-":
                        print(f"Hiệu = {hieu(nhap_a, nhap_b)}")
                        self.History.append(f"Phép tính cơ bản: Hiệu = {hieu(nhap_a, nhap_b)}")

                    elif chon_chuc_nang == "*":
                        print(f"Tich = {tich(nhap_a, nhap_b)}")
                        self.History.append(f"Phép tính cơ bản: Tích = {tich(nhap_a, nhap_b)}")

                    elif chon_chuc_nang == "/":
                        if nhap_b == 0:
                            print("Không thể chia cho 0")
                        else:
                            print(f"Thương = {thuong(nhap_a, nhap_b)}")
                            self.History.append(f"Phép tính cơ bản: Thương = {thuong(nhap_a, nhap_b)}")
                    else: 
                        print("Nhập sai chức năng")
                        self.History.append("Phép tính cơ bản")
                elif self.lua_chon == 2:
                    nhap_a = float(input("Nhập hệ số a: "))
                    nhap_b = float(input("Nhập số mũ: "))
                    print(f"Lũy thừa của số {nhap_a} là {luy_thua(nhap_a, nhap_b)}")
                    self.History.append(f"Lũy thừa: {luy_thua(nhap_a, nhap_b)}")
                elif self.lua_chon == 3:
                    nhap_a = float(input("Nhập hệ số a: "))
                    print(f"căn bậc hai của {nhap_a} = {can_bac2(nhap_a)}")
                    self.History.append(f"Căn: {can_bac2(nhap_a)}")
                elif self.lua_chon == 4:
                    try:
                        nhap_a = float(input("Nhập hệ số a: "))
                        chon_chuc_nang = input("Chọn hàm lượng giác: Sin, Cos, Tan\n")
                        if chon_chuc_nang == "Sin":
                            print(f"Sin của số a là {sin(nhap_a)}\n")
                            self.History.append(f"Sin: {sin(nhap_a)}")

                        elif chon_chuc_nang == "Cos":
                            print(f"Cos của số a là {cos(nhap_a)}\n")
                            self.History.append(f"Cos: {cos(nhap_a)}")

                        elif chon_chuc_nang == "Tan":
                            print(f"Tan của số a là {tan(nhap_a)}\n")
                            self.History.append(f"Tan: {tan(nhap_a)}")

                        else:
                            print("Nhập sai chức năng")
                    except ValueError:
                        print("Bạn hãy nhập số, không nhập ký tự khác")
                elif self.lua_chon == 5:
                    chon_chuc_nang = str(input("Chọn log10, ln, log cơ số tùy chọn: "))
                    if chon_chuc_nang == "log10":
                        nhap_a = float(input("Nhập hệ số a: "))
                        print(f"Log cơ số 10 của số a là {log10(nhap_a)}\n")
                        self.History.append(f"Log cơ số 10: {log10(nhap_a)}")

                    elif chon_chuc_nang == "ln":
                        nhap_a = float(input("Nhập hệ số a: "))
                        co_so_log = float(input("Nhập cơ số log: "))
                        print(f"Log cơ số tùy chọn của số {nhap_a} với cơ số {co_so_log} là {ln(nhap_a, co_so_log)}\n")
                        self.History.append(f"Log cơ số tùy chọn: {ln(nhap_a, co_so_log)}")

                    elif chon_chuc_nang == "log":
                        nhap_a = float(input("Nhập hệ số a: "))
                        print(f"Log của a là {log(nhap_a)}\n")
                        self.History.append(f"Log: {log(nhap_a)}")
                elif self.lua_chon == 6:
                    nhap_a = float(input("Nhập hệ số a: "))
                    nhap_b = float(input("Nhap hệ số b"))
                    print(f"Phương trình bậc nhất có nghiệm x = {pt_1(nhap_a, nhap_b)}")
                    self.History.append(f"Phương trình bậc nhất có nghiệm: x = {pt_1(nhap_a, nhap_b)}")
                elif self.lua_chon == 7:
                    nhap_a = float(input("Nhập hệ số a: "))
                    nhap_b = float(input("Nhập hệ số b: "))
                    nhap_c = float(input("Nhập hệ số c: "))
                    print(f"Nghiệm phương trình bậc hai là: {pt_2(nhap_a, nhap_b, nhap_c)}")
                    self.History.append(f"Phương trình bậc hai có nghiệm: {pt_2(nhap_a, nhap_b, nhap_c)}")
                elif self.lua_chon == 8:
                    print(f"{check_history(History = self.History)}")
                elif self.lua_chon == 9:
                    print("Thời gian hiện tại", thoi_gian())
                else:
                    print("Nhập sai chức năng, vui lòng nhập lại.")
            except ValueError:
                print("Lựa chọn không hợp lệ")



        

        
        
