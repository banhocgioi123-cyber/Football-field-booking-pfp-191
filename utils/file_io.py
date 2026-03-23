def save_data_to_file(filepath, data_list):
    try:
        # Mở file trực tiếp ở chế độ ghi ('w')
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in data_list:
                # Gọi phương thức chuyển đổi sang định dạng lưu trữ
                f.write(item.to_csv_format() + '\n')
    except Exception as e:
        print(f"Không thể lưu dữ liệu: {e}")

def load_data_from_file(filepath, class_ref):
    data_list = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    # Khởi tạo đối tượng từ dòng text
                    data_list.append(class_ref.from_csv_format(line))
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu: {e}")
    return data_list