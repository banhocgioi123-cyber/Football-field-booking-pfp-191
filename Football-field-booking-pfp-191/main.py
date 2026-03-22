from models.field import Field
from services.field_manager import FieldManager

def main():
    manager = FieldManager('data/fields.txt')

    while True:
        print("\n=== FOOTBALL FIELD BOOKING SYSTEM ===")
        print("1. Thêm sân mới")
        print("2. Xem danh sách tất cả các sân")
        print("3. Xóa sân")
        print("4. Đặt sân (Book a field)")
        print("5. Hủy đặt sân (Cancel booking)")
        print("6. Xem các sân đang được đặt (View current bookings)")
        print("0. Thoát")
        
        choice = input("Vui lòng chọn chức năng (0-6): ")

        try:
            if choice == '1':
                f_id = input("Nhập ID sân: ")
                name = input("Nhập tên sân: ")
                loc = input("Nhập vị trí: ")
                size = float(input("Nhập kích thước (m2): "))
                rate = float(input("Nhập giá thuê/giờ ($): "))
                new_field = Field(f_id, name, loc, size, rate)
                manager.add_field(new_field)
            
            elif choice == '2':
                manager.display_fields()
                
            elif choice == '3':
                f_id = input("Nhập ID sân cần xóa: ")
                manager.delete_field(f_id)
                
            elif choice == '4':
                f_id = input("Nhập ID sân muốn đặt: ")
                manager.book_field(f_id)
                
            elif choice == '5':
                f_id = input("Nhập ID sân muốn hủy đặt: ")
                manager.cancel_booking(f_id)
                
            elif choice == '6':
                manager.display_fields(filter_booked=True)
                
            elif choice == '0':
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại!")
        except ValueError:
            print("Lỗi: Dữ liệu nhập vào không hợp lệ (ví dụ: kích thước hoặc giá tiền phải là số).") [cite: 55]
        except Exception as e:
            print(f"Đã xảy ra lỗi hệ thống: {e}") [cite: 55]

if __name__ == "__main__":
    main()