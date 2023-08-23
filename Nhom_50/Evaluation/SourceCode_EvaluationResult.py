import pandas as pd
import os
import re

def merge_excel_files(input_folder, output_file):
    # Khởi tạo DataFrame để chứa dữ liệu nối
    merged_data = pd.DataFrame()

    # Lấy danh sách tệp Excel trong thư mục đầu vào
    excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

    # Đọc dữ liệu từ từng tệp Excel và nối vào DataFrame merged_data
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        data = pd.read_excel(file_path)
        merged_data = pd.concat([merged_data, data])

    # Lưu kết quả vào tệp Excel đầu ra
    merged_data.to_excel(output_file, index=False)

def remove_empty_rows(input_file, output_file):
    # Đọc dữ liệu từ tệp Excel vào DataFrame
    df = pd.read_excel(input_file)

    # Lọc và xoá các hàng không có nội dung
    df = df.dropna(how='all')

    # Ghi dữ liệu đã được lọc vào tệp Excel mới
    df.to_excel(output_file, index=False)

def is_ascii_or_vietnamese(s):
    # Kiểm tra xem từng ký tự trong từ có nằm trong bảng ASCII hoặc bảng tiếng Việt hay không
    for char in s:
        if ord(char) > 127 and not 128 <= ord(char) <= 417:  # Tham khảo bảng mã ASCII và bảng mã tiếng Việt
            return False
    return True

def count_non_ascii_vietnamese_words(input_file):
    # Đọc dữ liệu từ tệp Excel vào DataFrame
    df = pd.read_excel(input_file)

    # Tạo một danh sách chứa tất cả các nội dung trong tệp Excel
    all_contents = df.values.flatten().tolist()

    # Kết hợp tất cả các nội dung thành một chuỗi duy nhất
    combined_text = " ".join(map(str, all_contents))

    # Sử dụng biểu thức chính quy để tách các từ
    words = re.findall(r'\b\w+\b', combined_text.lower())

    # Đếm số lần xuất hiện của từng từ không nằm trong bảng ASCII và tiếng Việt
    count_non_ascii_vietnamese = 0
    for word in words:
        if not is_ascii_or_vietnamese(word):
            count_non_ascii_vietnamese += 1

    return count_non_ascii_vietnamese


# Gọi hàm merge_excel_files với thư mục đầu vào và tên tệp Excel đầu ra
input_folder = './Text'
output_file = 'output.xlsx'
merge_excel_files(input_folder, output_file)

# Gọi hàm remove_empty_rows với tên tệp Excel đầu vào và tên tệp Excel đầu ra
input_file = './output.xlsx'
output_file = 'EvaluationResult.xlsx'
remove_empty_rows(input_file, output_file)

# Gọi hàm count_non_ascii_vietnamese_words với tên tệp Excel đầu vào
input_file = './EvaluationResult.xlsx'
count = count_non_ascii_vietnamese_words(input_file)

print(f"Số từ không nằm trong bảng ASCII và tiếng Việt là: {count}")
