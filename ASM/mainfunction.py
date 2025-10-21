from class_manager import * 
import csv
import os
import re
ds_nhanvien ={
        "Hành chính" :[],
        "Tiếp thị" :[],
        "Trưởng phòng": [] 
    }

ds_toanbo_nhanvien = {
    "Hành chính" :[],
    "Tiếp thị" :[],
    "Trưởng phòng": [] 
}

def get_id(file_name):
    if  os.path.exists(file_name):
        with open(file_name, mode = 'r', encoding= 'utf-8') as file:
            line = csv.reader(file)
            next(line, None)
            lst_ma = [(row[0]) for row in line if row]
            if lst_ma :
                a = lst_ma[-1]
                match = re.sub(r"[^/0-9]", "", a)
                return int(match)
            else:
                return 0
    else : 
        return 0
    
hanh_chinh = get_id("hanh_chinh.csv")
tiep_thi = get_id("tiep_thi.csv")
truong_phong = get_id("truong_phong.csv")

def nhap_ds_nv():
    print("Chọn Loại Nhân Viên Muốn Nhập")

    while True:
        print("\nChọn loại nhân viên:")
        print("1. Hành chính")
        print("2. Tiếp thị") 
        print("3. Trưởng phòng")
        print("0. Thoát")
        
        try:
            the_loai= int(input("Nhập Thể Loại Nhân Viên:"))
        except ValueError:
            print("Vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
            continue
        
        if the_loai == 1:
            global hanh_chinh
            nhap_nhan_vien = NhanVien().nhap_thong_tin()
            ma_nv="HC"+str(hanh_chinh+1)
            nhap_nhan_vien.set_ma_nv(ma_nv)
            hanh_chinh+=1
            ds_nhanvien["Hành chính"].append(nhap_nhan_vien)
            ghi_file_hanh_chinh(nhap_nhan_vien)
            
            
        elif the_loai == 2:
            global tiep_thi
            nhap_nhan_vien_tiep_thi = NhanVienTiepThi().nhap_thong_tin()
            ds_nhanvien["Tiếp thị"].append(nhap_nhan_vien_tiep_thi)
            ma_nv="TT"+str(tiep_thi+1)
            nhap_nhan_vien_tiep_thi.set_ma_nv(ma_nv)
            tiep_thi+=1
            ghi_file_tiep_thi(nhap_nhan_vien_tiep_thi)
            
        elif the_loai == 3:
            global truong_phong
            nhap_truong_phong = TruongPhong().nhap_thong_tin()
            ds_nhanvien["Trưởng phòng"].append(nhap_truong_phong)
            ma_nv="TP"+str(truong_phong+1)
            nhap_truong_phong.set_ma_nv(ma_nv)
            truong_phong+=1
            ghi_file_truong_phong(nhap_truong_phong)
            
        elif the_loai ==0 :
            break
        else:
            print("Vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
    return ds_nhanvien

#Mới thêm cái này (xuất nhân viên theo loại ,truyên vào loại và danh sách theo loại đó để xuất ra theo định dạng tương ứng)
def xuat_ds_theo_loai(loai,danh_sach: list):
    if loai == "Hành chính" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*55)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} |")
        print("-"*55)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*55)
        
    elif loai == "Tiếp thị" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*91)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Doanh số':^15} | {'Tỉ lệ hoa hồng':^15} |")
        print("-"*91)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*91)
        
    elif loai == "Trưởng phòng" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*75)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Lương trách nhiệm':^17} |")
        print("-"*75)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*75)

    else :
        print("Loại nhân viên: ", loai)
        print("Không có nhân viên!")

#Mới thêm cái này (xuất nhân viên theo phòng ban có lựa chọn phòng ban muôn xuất)
def xuat_ds_theo_phong_ban(ds : dict):
    while True:
        while True:
            try:
                print("Chọn loại nhân viên cần xuất: ")
                print("1. Hành chính")
                print("2. Tiếp thị")
                print("3. Trưởng phòng")
                print("0. Quay lại menu chính")
                loai=int(input("Nhập lựa chọn của bạn (0-3): "))
                if loai in [0,1,2,3]:
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại")
            except ValueError:
                print("Vui lòng nhập đúng định dạng số")
        match loai:
            case 1:
                xuat_ds_theo_loai("Hành chính",ds["Hành chính"])
            case 2:
                xuat_ds_theo_loai("Tiếp thị",ds["Tiếp thị"])
            case 3: 
                xuat_ds_theo_loai("Trưởng phòng",ds["Trưởng phòng"])
            case 0:
                break

# đã sửa cái này theo cái trên (xuất toàn bộ danh sách nhân viên theo loại)  
def nap_du_lieu():
    global tmp
    tmp = {"Hành chính": [], "Tiếp thị": [], "Trưởng phòng": []}
    doc_file("hanh_chinh.csv")
    doc_file("tiep_thi.csv")
    doc_file("truong_phong.csv")
    ds_toanbo_nhanvien.clear()
    ds_toanbo_nhanvien.update(tmp)
    
    
def xuat_ds():
    print("="* 30 ,"DANH SÁCH NHÂN VIÊN", "="*30)
    for loai,danh_sach in ds_toanbo_nhanvien.items():
        xuat_ds_theo_loai(loai,danh_sach)
       
def tim_nv_theo_luong ():
    tim_kiem_nv_theo_luong = []
    while True:
        try:
            min_sal = int(input("Nhập lương tối thiểu: "))
            break
        except ValueError:
            print("Mức lương nhập không hợp lệ, vui lòng nhập lại")

    while True:
        try:
            max_sal = int(input("Nhập lương tối đa: "))
            break
        except ValueError:
            print("Mức lương nhập không hợp lệ, vui lòng nhập lại")
            
    for loai_nv in ds_toanbo_nhanvien.values():
        for employee in loai_nv:
            if min_sal <= employee.tinh_thu_nhap() <= max_sal:
                tim_kiem_nv_theo_luong.append(employee)
    if not tim_kiem_nv_theo_luong:
        print(f"Không tìm thấy nhân viên trong khoảng mức lương từ {min_sal:,} tới {max_sal:,}!")
    return tim_kiem_nv_theo_luong

def tim_nv_theo_ma():
    ma_nv = input("Nhập mã nhân viên: ").upper()
    for loai, danh_sach in ds_toanbo_nhanvien.items():
        for nv in danh_sach:
            if nv.ma_nv == ma_nv:
                return nv, loai
    return None,None

# đã sửa , isinstance là kiểm tra đối tượng thuộc cả lớp cha và lớp con nên phải kiểm tra theo thứ tự lớp con trước.    
def tim_kiem_nhan_vien():
    kq_tim_kiem = {
        "Hành chính": [],
        "Tiếp thị": [],
        "Trưởng phòng": []
    }
    print("*"*15+" TÌM KIẾM NHÂN VIÊN "+"*"*15)
    print("|    1. Tìm kiếm nhân viên theo mã               |")
    print("|    2. Tìm kiếm nhân viên theo khoảng lương     |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            tim_kiem = int(input("Bạn hãy chọn 1 hoặc 2: "))
            if tim_kiem in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if tim_kiem == 1:
        result, loai =tim_nv_theo_ma()
        #Neu result khong rong thi moi append
        if result is not None:
            if loai == "Hành chính":
                kq_tim_kiem["Hành chính"].append(result)
            elif loai == "Tiếp thị":
                kq_tim_kiem["Tiếp thị"].append(result)
            else:
                kq_tim_kiem["Trưởng phòng"].append(result)
        else:
            print("Không tìm thấy nhân viên trong danh sách.")
    else :
        list_tim_kiem =tim_nv_theo_luong()
        for nv in list_tim_kiem:
            if isinstance(nv, NhanVienTiepThi):
                kq_tim_kiem["Tiếp thị"].append(nv)
            elif isinstance(nv, TruongPhong):
                kq_tim_kiem["Trưởng phòng"].append(nv)
            elif isinstance(nv, NhanVien):
                kq_tim_kiem["Hành chính"].append(nv)
    return kq_tim_kiem
    
def xoa_nv_theo_ma():
    result, loai = tim_nv_theo_ma()
    if result is not None:
        for loai_nhanvien in ds_toanbo_nhanvien.keys():
            for nv in ds_toanbo_nhanvien[loai_nhanvien]:
                if result.ma_nv == nv.ma_nv:
                    print(f"Đã xóa nhân viên mã {result.ma_nv}")
                    ds_toanbo_nhanvien[loai_nhanvien].remove(result)
                    return
    else:
        print("Không có nhân viên cần xóa trong danh sách!")  
        return    
            
def sap_xep_nv_theo_thu_nhap():
    check = {}
    for loai, ds_nv in ds_toanbo_nhanvien.items():
        check[loai] = sorted(ds_nv, key=lambda nv:nv.tinh_thu_nhap(), reverse= True)
    return check

def sap_xep_nv_theo_ho_ten():
    check = {}
    for loai, ds_nv in ds_toanbo_nhanvien.items():
        check[loai] = sorted(ds_nv, key=lambda nv:nv.ten_nv, reverse= False)
    return check

def sap_xep_nv():
    print("*"*15+" SẮP XẾP NHÂN VIÊN "+"*"*16)
    print("|    1. Sắp xếp nhân viên theo tên               |")
    print("|    2. Sắp xếp nhân viên theo thu nhập          |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    kqua_sap_xep = {}
    while True:
        try:
            sap_xep = int(input("Bạn hãy chon 1 hoặc 2: "))
            if sap_xep in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if sap_xep == 1:
        kqua_sap_xep=sap_xep_nv_theo_ho_ten()
        print("Đã sắp xếp theo tên")
    elif sap_xep == 2:
        kqua_sap_xep=sap_xep_nv_theo_thu_nhap()
        print("Đã sắp xếp theo thu nhập")
    else:
        print("Thoát sắp xếp")
    print("Kết quả:")
    xuat_ds_theo_phong_ban(kqua_sap_xep)
    
    # ds_toanbo_nhanvien.clear()
    # ds_toanbo_nhanvien.update(kqua_sap_xep)
    # return kqua_sap_xep

def xuat_5_nv_thu_nhap_cao_nhat():
    check =[]
    for ds_nhan_vien in ds_toanbo_nhanvien.values():
        for nhan_vien in ds_nhan_vien:
            check.append(nhan_vien)
    sort_lst= sorted(check, key=lambda nv:nv.tinh_thu_nhap() , reverse= True)
    return sort_lst[:5]

def cap_nhat_tt_theo_ma():
    nv_can_sua, loai = tim_nv_theo_ma()
    if nv_can_sua is not None:
        
            #Nhap ten moi
            print(f"Tìm thấy nhân viên tên:{nv_can_sua.ten_nv} thuộc loại: {loai}")
            ten_moi = input("Nhập tên mới ( hoặc nhập q để bỏ qua):")
            if ten_moi.strip() and ten_moi.lower() != "q":
                nv_can_sua.ten_nv = ten_moi
                
            #Nhap luong moi
            while True:
                luong_moi = input("Nhập lương mới (hoặc nhập q để bỏ qua): ")
                try:
                    if luong_moi.strip() and luong_moi.lower() != "q":
                        nv_can_sua.luong_thang = int(luong_moi)
                    break
                except ValueError:
                    print("Nhập sai! Vui lòng nhập lại")
            
                
        #Sua lai thong tin nhan vien tiep thi 
            if isinstance(nv_can_sua,NhanVienTiepThi):
                #Sua lai doanh so
                dso_moi = input("Nhập doanh số mới (hoặc nhập q để bỏ qua): ")
                while True:
                    if dso_moi.strip() and dso_moi.lower() != "q":
                        nv_can_sua.doanh_so = int(dso_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
                    
                #Sua lai ty le hoa hong
                hoa_hong_moi = input("Nhập tỷ lệ hoa hồng mới (hoặc nhập q để bỏ qua):")
                while True:
                    if hoa_hong_moi.strip() and hoa_hong_moi.lower() != "q":
                        nv_can_sua.ti_le_hoa_hong = int(hoa_hong_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
                    
        #Sua lai thong tin truong phong
            if isinstance(nv_can_sua,TruongPhong):
                #Sua lai luong trach nhiem
                luong_trach_nhiem_moi = input("Nhập lương trách nhiệm mới (hoặc nhập q để bỏ qua): ")
                while True:
                    if luong_trach_nhiem_moi.strip() and luong_trach_nhiem_moi.lower() != "q":
                        nv_can_sua.luong_trach_nhiem = int(luong_trach_nhiem_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
            print("\n")
            xuat_ds()
    else:
        print("Không tìm thấy nhân viên trong danh sách.")
        
        
def ghi_toanbo_file():
    for loai, danhsach in ds_toanbo_nhanvien.items():
        if loai == "Hành chính":
            with open("hanh_chinh.csv", 'w', encoding='utf-8') as file:
                file.write("Ma_nhanvien,Ten_nhanvien,Luong_nv\n")
                for nv in danhsach:
                    file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang}\n")
            
        elif  loai == "Tiếp thị":
            with open("tiep_thi.csv", 'w', encoding='utf-8') as file:
                file.write("Ma_nhanvien,Ten_nhanvien,Luong_nv,Doanh_so,Ty_le_hoa_hong\n")
                for nv in danhsach:
                    file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.doanh_so},{nv.ti_le_hoa_hong}\n")
        else:
            with open("truong_phong.csv", 'w', encoding='utf-8') as file:
                file.write("Ma_nhanvien,Ten_nhanvien,Luong_thang,luong_trach_nhiem\n")
                for nv in danhsach:  
                    file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.luong_trach_nhiem}\n")

    
def ghi_file_hanh_chinh(nv):
    import os
    if os.path.exists('hanh_chinh.csv'):
        with open("hanh_chinh.csv", 'a', encoding='utf-8') as file:
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang}\n")
    else:
        with open("hanh_chinh.csv", 'w', encoding='utf-8') as file:
            file.write("Ma_nhanvien,Ten_nhanvien,Luong_nv\n")
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang}\n")
            
def ghi_file_tiep_thi(nv):
    import os
    if os.path.exists('tiep_thi.csv'):
        with open("tiep_thi.csv", 'a', encoding='utf-8') as file:
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.doanh_so},{nv.ti_le_hoa_hong}\n")
    else:
        with open("tiep_thi.csv", 'w', encoding='utf-8') as file:
            file.write("Ma_nhanvien,Ten_nhanvien,Luong_nv,Doanh_so,Ty_le_hoa_hong\n")
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.doanh_so},{nv.ti_le_hoa_hong}\n")
            
def ghi_file_truong_phong(nv):
    import os
    if os.path.exists('truong_phong.csv'):
        with open("truong_phong.csv", 'a', encoding='utf-8') as file:
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.luong_trach_nhiem}\n")
    else:
        with open("truong_phong.csv", 'w', encoding='utf-8') as file:
            file.write("Ma_nhanvien,Ten_nhanvien,Luong_thang,luong_trach_nhiem\n")   
            file.write(f"{nv.ma_nv},{nv.ten_nv},{nv.luong_thang},{nv.luong_trach_nhiem}\n")  
            
def doc_file(file_name):
    # if ds_toanbo_nhanvien is None:
    #     ds_toanbo_nhanvien = {
    #         "Hành chính": [],
    #         "Tiếp thị": [],
    #         "Trưởng phòng": []
    #     }
    
    with open(file_name,"r",encoding="utf-8") as file:
        ds = csv.DictReader(file)
        if file_name == "hanh_chinh.csv":
            for row in ds:
                nv = NhanVien(ma_nv=row["Ma_nhanvien"],
                            ten_nv=row["Ten_nhanvien"],
                            luong_thang=int(row["Luong_nv"]))
                
                tmp["Hành chính"].append(nv)
        elif file_name == "tiep_thi.csv":
            for row in ds:
                nv = NhanVienTiepThi(ma_nv=row["Ma_nhanvien"],
                            ten_nv=row["Ten_nhanvien"],
                            luong_thang=int(row["Luong_nv"]),
                            doanh_so=int(row["Doanh_so"]),
                            ti_le_hoa_hong=float(row["Ty_le_hoa_hong"]))
                tmp["Tiếp thị"].append(nv)
        else:
            for row in ds:
                nv = TruongPhong(ma_nv=row["Ma_nhanvien"],
                            ten_nv=row["Ten_nhanvien"],
                            luong_thang=int(row["Luong_thang"].strip()),
                            luong_trach_nhiem=int(row["luong_trach_nhiem"]))
                tmp["Trưởng phòng"].append(nv)
    return tmp
    


