# Thu thập dữ liệu song ngữ chữ Nôm - chữ Quốc ngữ

## Giới thiệu

Dự án "Thu thập dữ liệu song ngữ chữ Nôm - chữ Quốc ngữ" nhằm mục đích thu thập và tổ chức dữ liệu song ngữ giữa hai hệ thống chữ viết chính tại Việt Nam: chữ Nôm và chữ Quốc ngữ. Dự án cung cấp nguồn tài liệu quý báu cho nghiên cứu ngôn ngữ, phát triển ứng dụng học tập và khám phá văn hóa truyền thống.


## Mô tả thư mục

1. **Reports/**
   - Thư mục chứa các báo cáo và slide liên quan đến dự án.
   - Thư mục con **Report/** chứa các phiên bản của báo cáo dưới dạng docx và pdf.
   - Thư mục con **Slide/** chứa các phiên bản của slide dưới dạng pptx và pdf.

2. **SourceCode/**
   - Thư mục chứa mã nguồn của dự án.
   - File **NLP_Project.ipynb** là mã nguồn trong định dạng IPython Notebook.

3. **Results/**
   - Thư mục chứa các kết quả thu thập và xử lý dữ liệu.
   - Thư mục con **Constant_HTML_file/** chứa các file html dùng cho bước lọc nội dung.
   - Thư mục con **file_html/** chứa các file html thu thập được.
   - Thư mục con **images/** chứa các hình ảnh thu thập được.
   - Thư mục con **Text/** chứa các file dữ liệu thu thập được dưới dạng đôi một xlsx và txt.

4. **Evaluation/**
   - Thư mục chứa mã nguồn và kết quả đánh giá dữ liệu thu thập.
   - File **SourceCode_EvaluationResult.py** là mã nguồn để đánh giá và ước tính số lượng dữ liệu thu thập được.
   - File **EvaluationResult.xlsx** chứa toàn bộ dữ liệu thu thập được, được lưu thành hai cột: một cột chữ Nôm và một cột chữ Quốc ngữ.


## Cấu trúc thư mục

Dưới đây là cấu trúc thư mục của dự án:
```
📦Nhom_50
 ┣ 📂Evaluation
 ┃ ┣ 📜EvaluationResult.xlsx
 ┃ ┗ 📜SourceCode_EvaluationResult.py
 ┣ 📂Reports
 ┃ ┣ 📂Report
 ┃ ┃ ┣ 📜22C11005_22C11048_XLNNTN_K32.docx
 ┃ ┃ ┗ 📜22C11005_22C11048_XLNNTN_K32.pdf
 ┃ ┣ 📂Slide
 ┃ ┃ ┣ 📜Slide_22C11005_22C11048_XLNNTNNC_K32.pdf
 ┃ ┃ ┗ 📜Slide_22C11005_22C11048_XLNNTNNC_K32.pptx
 ┃ ┗ 📜.DS_Store
 ┣ 📂Results
 ┃ ┣ 📂Constant_HTLM_file
 ┃ ┃ ┣ 📜1547-Truyền-Kỳ-Mạn-Lục-Nguyễn-Dữ.html
 ┃ ┃ ┣ 📜1898-Quảng-Tập-Viem-Văn-Edmond-Nordemann.html
 ┃ ┃ ┣ 📜1950-Cung-Oan-Ngam-Khuc-Dẫn-Giải-Va-Chu-Thich-Ton-Thất-Lương.html
 ┃ ┃ ┣ 📜1952-Gia-Huấn-Ca-Nguyễn-Trai-Đinh-Gia-Thuyết-Chu-Thich.html
 ┃ ┃ ┣ 📜1958-Giai-Nhan-Kỳ-Ngộ-Phan-Chau-Trinh.html
 ┃ ┃ ┣ 📜1958-Thien-Nam-Ngữ-Lục-Tập-1-Nguyễn-Lương-Ngọc-Đinh-Gia-Khanh.html
 ┃ ┃ ┣ 📜Ba-Huyện-Thanh-Quan-Lam-Trau-Diễn-Nom.html
 ┃ ┃ ┣ 📜Bai-Hat-Đĩ-Diễn-Nom.html
 ┃ ┃ ┣ 📜Bai-Tựa-Đại-Nam-Quốc-Ngữ.html
 ┃ ┃ ┣ 📜Bạch-Van-Am-Quốc-Ngữ-Nguyễn-Bỉnh-Khiem.html
 ┃ ┃ ┣ 📜Bạch-Van-Thi-Tập-Maurice-Durand.html
 ┃ ┃ ┣ 📜Cac-Bai-Tuyệt-Cu-Trong-Quốc-Am-Thi-Tập-Nguyễn-Đinh-Hoa-Le-Văn-Đặng.html
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Diễn-Ca-Nguyễn-Văn-Xuan.html
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Han-Việt.html
 ┃ ┃ ┣ 📜Cung-Oan-Ngam-Khuc-Nguyễn-Gia-Thiều-Le-Văn-Đặng-Diễn-Nom.html
 ┃ ┃ ┣ 📜Cung-Oan-Thi-Maurice-Durand.html
 ┃ ┃ ┣ 📜Di-Chuc-Văn-Nguyễn-Khuyến.html
 ┃ ┃ ┣ 📜Giao-Tử-Phu-Mạc-Đĩnh-Chi.html
 ┃ ┃ ┣ 📜Hồ-Xuan-Hương-Thi-Tập-Le-Văn-Đặng-Diễn-Nom.html
 ┃ ┃ ┣ 📜Le-Triều-Nguyễn-Tướng-Cong-Gia-Huấn-Ca-Maurice-Durand.html
 ┃ ┃ ┣ 📜Ma-Thanh-Tan-Truyện-Lý-Hồng-Phượng.html
 ┃ ┃ ┣ 📜Minh-Tam-Bửu-Giam-Diễn-Nom.html
 ┃ ┃ ┣ 📜Mộng-Lien-Đinh-Thi-Thảo-Nguyễn-Gia-Tuyển.html
 ┃ ┃ ┣ 📜Nữ-Tử-Tu-Tri-Diễn-Nom.html
 ┃ ┃ ┣ 📜Phương-Hoa-Tan-Truyện-Maurice-Durand.html
 ┃ ┃ ┣ 📜Phật-Thuyết-Đại-Thanh-Mạt-Kiếp-Chan-Kinh-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thanh-Tổ-Kệ-Diễn-Quốc-Am-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thien-Nam-Ngữ-Lục-Thơ-Nom.html
 ┃ ┃ ┣ 📜Thien-Nam-Toan-Quốc-Diễn-Am-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thập-Giới-Co-Hồn-Quốc-Ngữ-Văn-Le-Thanh-Tong.html
 ┃ ┃ ┣ 📜Truyện-Vua-Le-Thai-Tổ-Maurice-Durand.html
 ┃ ┃ ┣ 📜Tổng-Tập-Văn-Học-Nom-Thơ-Nom-Han-Luật-Nguyễn-Ta-Nhi.html
 ┃ ┃ ┣ 📜Văn-Tế-Tướng-Sĩ-Trận-Vong-Maurice-Durand.html
 ┃ ┃ ┣ 📜Đi-Chợ-Tinh-Tiền-Diễn-Nom.html
 ┃ ┃ ┗ 📜Đại-Nam-Quốc-Tuý-Maurice-Durand.html
 ┃ ┣ 📂Text
 ┃ ┃ ┣ 📜1547-Truyền-Kỳ-Mạn-Lục-Nguyễn-Dữ.txt
 ┃ ┃ ┣ 📜1547-Truyền-Kỳ-Mạn-Lục-Nguyễn-Dữ.xlsx
 ┃ ┃ ┣ 📜1898-Quảng-Tập-Viem-Văn-Edmond-Nordemann.xlsx
 ┃ ┃ ┣ 📜1950-Cung-Oan-Ngam-Khuc-Dẫn-Giải-Va-Chu-Thich-Ton-Thất-Lương.txt
 ┃ ┃ ┣ 📜1952-Gia-Huấn-Ca-Nguyễn-Trai-Đinh-Gia-Thuyết-Chu-Thich.txt
 ┃ ┃ ┣ 📜1958-Giai-Nhan-Kỳ-Ngộ-Phan-Chau-Trinh.txt
 ┃ ┃ ┣ 📜1958-Giai-Nhan-Kỳ-Ngộ-Phan-Chau-Trinh.xlsx
 ┃ ┃ ┣ 📜1958-Thien-Nam-Ngữ-Lục-Tập-1-Nguyễn-Lương-Ngọc-Đinh-Gia-Khanh.txt
 ┃ ┃ ┣ 📜1958-Thien-Nam-Ngữ-Lục-Tập-1-Nguyễn-Lương-Ngọc-Đinh-Gia-Khanh.xlsx
 ┃ ┃ ┣ 📜Ba-Huyện-Thanh-Quan-Lam-Trau-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Ba-Huyện-Thanh-Quan-Lam-Trau-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Bai-Hat-Đĩ-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Bai-Hat-Đĩ-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Bai-Tựa-Đại-Nam-Quốc-Ngữ.txt
 ┃ ┃ ┣ 📜Bai-Tựa-Đại-Nam-Quốc-Ngữ.xlsx
 ┃ ┃ ┣ 📜Bạch-Van-Am-Quốc-Ngữ-Nguyễn-Bỉnh-Khiem.txt
 ┃ ┃ ┣ 📜Bạch-Van-Am-Quốc-Ngữ-Nguyễn-Bỉnh-Khiem.xlsx
 ┃ ┃ ┣ 📜Bạch-Van-Thi-Tập-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Bạch-Van-Thi-Tập-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Cac-Bai-Tuyệt-Cu-Trong-Quốc-Am-Thi-Tập-Nguyễn-Đinh-Hoa-Le-Văn-Đặng.xlsx
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Diễn-Ca-Nguyễn-Văn-Xuan.txt
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Diễn-Ca-Nguyễn-Văn-Xuan.xlsx
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Han-Việt.txt
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Han-Việt.xlsx
 ┃ ┃ ┣ 📜Cung-Oan-Ngam-Khuc-Nguyễn-Gia-Thiều-Le-Văn-Đặng-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Cung-Oan-Ngam-Khuc-Nguyễn-Gia-Thiều-Le-Văn-Đặng-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Cung-Oan-Thi-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Di-Chuc-Văn-Nguyễn-Khuyến.xlsx
 ┃ ┃ ┣ 📜Giao-Tử-Phu-Mạc-Đĩnh-Chi.txt
 ┃ ┃ ┣ 📜Giao-Tử-Phu-Mạc-Đĩnh-Chi.xlsx
 ┃ ┃ ┣ 📜Hồ-Xuan-Hương-Thi-Tập-Le-Văn-Đặng-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Hồ-Xuan-Hương-Thi-Tập-Le-Văn-Đặng-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Ma-Thanh-Tan-Truyện-Lý-Hồng-Phượng.txt
 ┃ ┃ ┣ 📜Ma-Thanh-Tan-Truyện-Lý-Hồng-Phượng.xlsx
 ┃ ┃ ┣ 📜Minh-Tam-Bửu-Giam-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Mộng-Lien-Đinh-Thi-Thảo-Nguyễn-Gia-Tuyển.txt
 ┃ ┃ ┣ 📜Mộng-Lien-Đinh-Thi-Thảo-Nguyễn-Gia-Tuyển.xlsx
 ┃ ┃ ┣ 📜Nữ-Tử-Tu-Tri-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Nữ-Tử-Tu-Tri-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Phương-Hoa-Tan-Truyện-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Phương-Hoa-Tan-Truyện-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Phật-Thuyết-Đại-Thanh-Mạt-Kiếp-Chan-Kinh-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Phật-Thuyết-Đại-Thanh-Mạt-Kiếp-Chan-Kinh-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Thanh-Tổ-Kệ-Diễn-Quốc-Am-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Thanh-Tổ-Kệ-Diễn-Quốc-Am-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Thien-Nam-Ngữ-Lục-Thơ-Nom.xlsx
 ┃ ┃ ┣ 📜Thien-Nam-Toan-Quốc-Diễn-Am-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Thien-Nam-Toan-Quốc-Diễn-Am-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Thập-Giới-Co-Hồn-Quốc-Ngữ-Văn-Le-Thanh-Tong.txt
 ┃ ┃ ┣ 📜Thập-Giới-Co-Hồn-Quốc-Ngữ-Văn-Le-Thanh-Tong.xlsx
 ┃ ┃ ┣ 📜Truyện-Vua-Le-Thai-Tổ-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Truyện-Vua-Le-Thai-Tổ-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜Tổng-Tập-Văn-Học-Nom-Thơ-Nom-Han-Luật-Nguyễn-Ta-Nhi.txt
 ┃ ┃ ┣ 📜Văn-Tế-Tướng-Sĩ-Trận-Vong-Maurice-Durand.txt
 ┃ ┃ ┣ 📜Văn-Tế-Tướng-Sĩ-Trận-Vong-Maurice-Durand.xlsx
 ┃ ┃ ┣ 📜~$Di-Chuc-Văn-Nguyễn-Khuyến.xlsx
 ┃ ┃ ┣ 📜Đi-Chợ-Tinh-Tiền-Diễn-Nom.txt
 ┃ ┃ ┣ 📜Đi-Chợ-Tinh-Tiền-Diễn-Nom.xlsx
 ┃ ┃ ┣ 📜Đại-Nam-Quốc-Tuý-Maurice-Durand.txt
 ┃ ┃ ┗ 📜Đại-Nam-Quốc-Tuý-Maurice-Durand.xlsx
 ┃ ┣ 📂file_html
 ┃ ┃ ┣ 📜1547-Truyền-Kỳ-Mạn-Lục-Nguyễn-Dữ.html
 ┃ ┃ ┣ 📜1898-Quảng-Tập-Viem-Văn-Edmond-Nordemann.html
 ┃ ┃ ┣ 📜1950-Cung-Oan-Ngam-Khuc-Dẫn-Giải-Va-Chu-Thich-Ton-Thất-Lương.html
 ┃ ┃ ┣ 📜1952-Gia-Huấn-Ca-Nguyễn-Trai-Đinh-Gia-Thuyết-Chu-Thich.html
 ┃ ┃ ┣ 📜1958-Giai-Nhan-Kỳ-Ngộ-Phan-Chau-Trinh.html
 ┃ ┃ ┣ 📜1958-Thien-Nam-Ngữ-Lục-Tập-1-Nguyễn-Lương-Ngọc-Đinh-Gia-Khanh.html
 ┃ ┃ ┣ 📜Ba-Huyện-Thanh-Quan-Lam-Trau-Diễn-Nom.html
 ┃ ┃ ┣ 📜Bai-Hat-Đĩ-Diễn-Nom.html
 ┃ ┃ ┣ 📜Bai-Tựa-Đại-Nam-Quốc-Ngữ.html
 ┃ ┃ ┣ 📜Bạch-Van-Am-Quốc-Ngữ-Nguyễn-Bỉnh-Khiem.html
 ┃ ┃ ┣ 📜Bạch-Van-Thi-Tập-Maurice-Durand.html
 ┃ ┃ ┣ 📜Cac-Bai-Tuyệt-Cu-Trong-Quốc-Am-Thi-Tập-Nguyễn-Đinh-Hoa-Le-Văn-Đặng.html
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Diễn-Ca-Nguyễn-Văn-Xuan.html
 ┃ ┃ ┣ 📜Chinh-Phụ-Ngam-Han-Việt.html
 ┃ ┃ ┣ 📜Cung-Oan-Ngam-Khuc-Nguyễn-Gia-Thiều-Le-Văn-Đặng-Diễn-Nom.html
 ┃ ┃ ┣ 📜Cung-Oan-Thi-Maurice-Durand.html
 ┃ ┃ ┣ 📜Di-Chuc-Văn-Nguyễn-Khuyến.html
 ┃ ┃ ┣ 📜Giao-Tử-Phu-Mạc-Đĩnh-Chi.html
 ┃ ┃ ┣ 📜Hồ-Xuan-Hương-Thi-Tập-Le-Văn-Đặng-Diễn-Nom.html
 ┃ ┃ ┣ 📜Le-Triều-Nguyễn-Tướng-Cong-Gia-Huấn-Ca-Maurice-Durand.html
 ┃ ┃ ┣ 📜Ma-Thanh-Tan-Truyện-Lý-Hồng-Phượng.html
 ┃ ┃ ┣ 📜Minh-Tam-Bửu-Giam-Diễn-Nom.html
 ┃ ┃ ┣ 📜Mộng-Lien-Đinh-Thi-Thảo-Nguyễn-Gia-Tuyển.html
 ┃ ┃ ┣ 📜Nữ-Tử-Tu-Tri-Diễn-Nom.html
 ┃ ┃ ┣ 📜Phương-Hoa-Tan-Truyện-Maurice-Durand.html
 ┃ ┃ ┣ 📜Phật-Thuyết-Đại-Thanh-Mạt-Kiếp-Chan-Kinh-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thanh-Tổ-Kệ-Diễn-Quốc-Am-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thien-Nam-Ngữ-Lục-Thơ-Nom.html
 ┃ ┃ ┣ 📜Thien-Nam-Toan-Quốc-Diễn-Am-Maurice-Durand.html
 ┃ ┃ ┣ 📜Thập-Giới-Co-Hồn-Quốc-Ngữ-Văn-Le-Thanh-Tong.html
 ┃ ┃ ┣ 📜Truyện-Vua-Le-Thai-Tổ-Maurice-Durand.html
 ┃ ┃ ┣ 📜Tổng-Tập-Văn-Học-Nom-Thơ-Nom-Han-Luật-Nguyễn-Ta-Nhi.html
 ┃ ┃ ┣ 📜Văn-Tế-Tướng-Sĩ-Trận-Vong-Maurice-Durand.html
 ┃ ┃ ┣ 📜Đi-Chợ-Tinh-Tiền-Diễn-Nom.html
 ┃ ┃ ┗ 📜Đại-Nam-Quốc-Tuý-Maurice-Durand.html
 ┃ ┗ 📂images
 ┃ ┃ ┣ 📜1-118a9141d2.jpg
 ┃ ┃ ┣ 📜1-27ea5bac31.jpg
 ┃ ┃ ┣ 📜1-2c7667b8f1.jpg
 ┃ ┃ ┣ 📜1-31837694ee.jpg
 ┃ ┃ ┣ 📜1-47603f3b2e.jpg
 ┃ ┃ ┣ 📜1-51059560b7.jpg
 ┃ ┃ ┣ 📜1-564617c697.jpg
 ┃ ┃ ┣ 📜1-7b36f001fc.jpg
 ┃ ┃ ┣ 📜1-81f26b6c3d.jpg
 ┃ ┃ ┣ 📜1-820783579c.jpg
 ┃ ┃ ┣ 📜1-8f74590ccb.jpg
 ┃ ┃ ┣ 📜1-9ada7370b9.jpg
 ┃ ┃ ┣ 📜1-9bb68f9ace.jpg
 ┃ ┃ ┣ 📜1-a58d5af9a6.jpg
 ┃ ┃ ┣ 📜1-bfadffd0cf.jpg
 ┃ ┃ ┣ 📜1-da36cf1a36.jpg
 ┃ ┃ ┣ 📜1-dcdf70a73e.jpg
 ┃ ┃ ┣ 📜1-edcd788fb0.jpg
 ┃ ┃ ┣ 📜1-f57a94c2ed.jpg
 ┃ ┃ ┣ 📜1-f57ec2e85e.jpg
 ┃ ┃ ┣ 📜1-f8a873282d.jpg
 ┃ ┃ ┣ 📜2-0a7eecda66.jpg
 ┃ ┃ ┣ 📜2-229d58a27e.jpg
 ┃ ┃ ┣ 📜2-4c3b3c5416.jpg
 ┃ ┃ ┣ 📜2-5bac81c363.jpg
 ┃ ┃ ┣ 📜2-64596c342c.jpg
 ┃ ┃ ┣ 📜2-85f60d32e9.jpg
 ┃ ┃ ┣ 📜2-8f9f732fdd.jpg
 ┃ ┃ ┣ 📜2-9c6486b618.jpg
 ┃ ┃ ┣ 📜2-9de0be3e28.jpg
 ┃ ┃ ┣ 📜2-9de3d2a0df.jpg
 ┃ ┃ ┣ 📜2-a062ff655f.jpg
 ┃ ┃ ┣ 📜2-b902d8a7ee.jpg
 ┃ ┃ ┣ 📜2-c6fb105968.jpg
 ┃ ┃ ┣ 📜2-c97f8ad59a.jpg
 ┃ ┃ ┣ 📜2-d3064353de.jpg
 ┃ ┃ ┣ 📜2-daccb94428.jpg
 ┃ ┃ ┣ 📜2-f02a0ce456.jpg
 ┃ ┃ ┣ 📜2-ff987cf688.jpg
 ┃ ┃ ┣ 📜3-175373fe62.jpg
 ┃ ┃ ┣ 📜3-27ec3b7be3.jpg
 ┃ ┃ ┣ 📜3-3940a8b888.jpg
 ┃ ┃ ┣ 📜3-3d75f10e62.jpg
 ┃ ┃ ┣ 📜3-55985e950f.jpg
 ┃ ┃ ┣ 📜3-6e9e6492d8.jpg
 ┃ ┃ ┣ 📜3-73e23d7588.jpg
 ┃ ┃ ┣ 📜3-86cae9b550.jpg
 ┃ ┃ ┣ 📜3-a89f8e86e1.jpg
 ┃ ┃ ┣ 📜3-b260abde1f.jpg
 ┃ ┃ ┣ 📜3-b2694710c1.jpg
 ┃ ┃ ┣ 📜3-bb7f4adeb4.jpg
 ┃ ┃ ┣ 📜3-c7faa8d2bd.jpg
 ┃ ┃ ┣ 📜3-c89480ea74.jpg
 ┃ ┃ ┣ 📜3-c9053c9a55.jpg
 ┃ ┃ ┣ 📜3-c95be79d66.jpg
 ┃ ┃ ┗ 📜3-f81615bbf7.jpg
 ┣ 📂SourceCode
 ┃ ┣ 📜NLP_Project-2.ipynb
 ┃ ┗ 📜NLP_Project.ipynb
 ┗ 📜README.md
```

*README được viết bởi [Duyen Nguyen](https://github.com/thuduyen07) và [Triet Dang](https://github.com/trietdang5599)*
