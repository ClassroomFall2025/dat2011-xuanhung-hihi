from ... import as svpl
class QuanLySinhVien:
    # Khởi tạo danh sách sinh viên rỗng
    def __init__(self):
        self.danh_sach_sinh_vien = []
    # Phuơng thức nhập danh sách sinh viên
    def nhap_dssv(self):
        while True:
            ho_ten_sv = input("Nhập họ tên sinh viên: ")
            nganh_hoc = input("Nhập ngành học: ")
            if nganh_hoc.lower() == "it":
                java = float(input("Nhập điểm Java: "))
                html = float(input("Nhập điểm HTML: "))
                css = float(input("Nhập điểm CSS: "))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.danh_sach_sinh_vien.append(sv)
            elif nganh_hoc.lower() == "biz":
                marketing = float(input("Nhập điểm Marketing: "))
                sales = float(input("Nhập điểm Sales: "))
                sv = svpl.SinhVienBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                self.danh_sach_sinh_vien.append(sv)
            elif nganh_hoc.lower() == "exit":
                break
            else:
                print("Ngành học không hợp lệ. Vui lòng nhập lại.")
            return self.danh_sach_sinh_vien
    # Phuơng thức xuất danh sách sinh viên
    def xuat_dssv(self):
        if not self.danh_sach_sinh_vien:
            print("Danh sách sinh viên rỗng.")
        else:
            print(f"{Ten Sinh Vien}, {Nganh Hoc}, {Diem}, {Hoc Luc}")
            for sv in self.danh_sach_sinh_vien:
                sv.xuat_thong_tin()
    def xuat_dssv_gioi(self):
        pass
    def sap_xep_dssv(self):
        pass
