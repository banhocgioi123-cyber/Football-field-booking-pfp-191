from models.field import Field
from utils.file_io import save_data_to_file, load_data_from_file

class FieldManager:
    def __init__(self, data_filepath: str):
        self.data_filepath = data_filepath
        self.fields = load_data_from_file(self.data_filepath, Field)

    def save_fields(self):
        save_data_to_file(self.data_filepath, self.fields)

    def add_field(self, field: Field):
        if any(f.field_id == field.field_id for f in self.fields):
            print("Lỗi: Mã sân đã tồn tại!")
            return
        self.fields.append(field)
        self.save_fields()
        print("Thêm sân thành công!")

    def display_fields(self, filter_booked=False):
        print("\n--- Danh sách sân bóng ---")
        if not self.fields:
            print("Chưa có dữ liệu sân bóng.")
            return

        for f in self.fields:
            if filter_booked and f.is_available:
                continue
            print(f)

    def delete_field(self, field_id: str):
        for f in self.fields:
            if f.field_id == field_id:
                self.fields.remove(f)
                self.save_fields()
                print("Xóa sân thành công!")
                return
        print("Không tìm thấy mã sân!")

    def book_field(self, field_id: str):
        for f in self.fields:
            if f.field_id == field_id:
                if f.is_available:
                    f.is_available = False # Cập nhật trạng thái thành booked [cite: 42]
                    self.save_fields()
                    print("Đặt sân thành công!")
                else:
                    print("Sân này đã được đặt!")
                return
        print("Không tìm thấy mã sân!")

    def cancel_booking(self, field_id: str):
        for f in self.fields:
            if f.field_id == field_id:
                if not f.is_available:
                    f.is_available = True
                    self.save_fields()
                    print("Hủy đặt sân thành công!")
                else:
                    print("Sân này hiện đang trống, không thể hủy!")
                return
        print("Không tìm thấy mã sân!")