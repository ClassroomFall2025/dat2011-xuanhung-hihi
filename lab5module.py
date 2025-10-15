class SanPham:
    def __init__(self, ten = "", gia = 0, giam_gia = 0):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia
    def get_ten(self):
        return self.__ten
    def set_ten(self, ten):
        self.__ten = ten
    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia
    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    def nhap(self):
        ten_sp = input("Nhập tên sản phẩm: ")
        self.set_ten(ten_sp)
        self.gia = float(input("Nhập đơn giá: "))
        self.giam_gia = float(input("Nhập giảm giá: "))

    def thue_nhap_khau(self):
        return self.get_gia(self) * 0.1# 10% thuế nhập khẩu

    def xuat_thong_tin(self):
        print("Tên sản phẩm:", self.get_ten())
        print("Đơn giá:", self.gia)
        print("Giảm giá:", self.giam_gia)
        print("Thuế nhập khẩu:", self.thue_nhap_khau())
        print("Giá cuối:", self.gia - self.giam_gia + self.thue_nhap_khau())# Giá cuối = Giá - Giảm giá + Thuế nhập khẩu
