class SinhVienPoly:
    def __init__(self, ho_ten = "", nganh = ""):
        self.ho_ten = ho_ten
        self.nganh = nganh
    def get_diem(self):
        pass
    def get_hoc_luc(self):
        if self.get_diem() >= 9:
            return "Xuat sac"
        elif self.get_diem() >= 8:
            return "Gioi"
        elif self.get_diem() >= 7:
            return "Kha"
        elif self.get_diem() >= 5:
            return "Trung binh"
        else:
            return "Yeu"
    def xuat(self):
        print("Ho ten sinh vien: ", self.ho_ten)
        print("Nganh hoc: ", self.nganh)
        print("Diem: ", self.get_diem())
        print("Hoc luc: ", self.get_hoc_luc())
class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_java = 0, diem_html = 0, diem_css = 0):
        super().__init__(ho_ten, nganh)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css
    def get_diem(self):
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_mkt = 0, diem_sales = 0):
        super().__init__(ho_ten, nganh)
        self.diem_mkt = diem_mkt
        self.diem_sales = diem_sales
    def get_diem(self):
        return (2 * self.diem_mkt + self.diem_sales) / 3
