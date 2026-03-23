class Field:
    def __init__(self, field_id: str, name: str, location: str, size: float, hourly_rate: float, is_available: bool = True):
        self._field_id = field_id
        self._name = name
        self._location = location
        self._size = size
        self._hourly_rate = hourly_rate
        self._is_available = is_available

    @property
    def field_id(self):
        return self._field_id

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, status: bool):
        self._is_available = status

    def __str__(self):
        status = "Available" if self._is_available else "Booked"
        return f"[{self._field_id}] {self._name} | {self._location} | {self._size} sqm | ${self._hourly_rate}/h | Status: {status}"

    def to_csv_format(self):
        # Trả về chuỗi để ghi vào file txt
        return f"{self._field_id},{self._name},{self._location},{self._size},{self._hourly_rate},{self._is_available}"

    @classmethod
    def from_csv_format(cls, data_string: str):
        # Khởi tạo đối tượng từ chuỗi đọc trong file txt
        parts = data_string.strip().split(',')
        if len(parts) == 6:
            return cls(parts[0], parts[1], parts[2], float(parts[3]), float(parts[4]), parts[5] == 'True')
        raise ValueError("Dữ liệu không hợp lệ")