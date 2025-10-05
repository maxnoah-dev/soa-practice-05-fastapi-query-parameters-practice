# Bài Tập Unit 7: Query Parameters với FastAPI

Dự án này thực hiện 6 bài tập về Query Parameters trong FastAPI, bao gồm các khái niệm cơ bản đến nâng cao về xử lý tham số truy vấn.

## Cài Đặt

1. Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

2. Chạy ứng dụng:
```bash
python main.py
```

3. Truy cập tài liệu API:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

4. Test API (tùy chọn):
```bash
python test_api.py
```

## Chi Tiết Bài Tập

### 1. Lọc Số (`/filter`)
- **Tham số**: `min` (bắt buộc), `max` (bắt buộc)
- **Chức năng**: Trả về danh sách số từ min đến max (bao gồm cả hai đầu)
- **Ví dụ**: `GET /filter?min=3&max=7` → `{"numbers": [3, 4, 5, 6, 7]}`
- **Kiến thức**: Tham số bắt buộc, validation đầu vào

### 2. Tìm Kiếm Sản Phẩm (`/search`)
- **Tham số**: `keyword` (tùy chọn)
- **Chức năng**: Tìm kiếm sản phẩm theo từ khóa (không phân biệt hoa thường)
- **Ví dụ**: `GET /search?keyword=lap` → trả về sản phẩm có tên chứa "lap"
- **Kiến thức**: Tham số tùy chọn, tìm kiếm không phân biệt hoa thường

### 3. Tính Giảm Giá Sản Phẩm (`/products/{product_id}`)
- **Tham số đường dẫn**: `product_id`
- **Tham số truy vấn**: `discount` (tùy chọn, mặc định=0)
- **Chức năng**: Tính giá cuối cùng sau khi áp dụng giảm giá
- **Ví dụ**: `GET /products/1?discount=10` → giá gốc 1200, giảm 10%, còn 1080
- **Kiến thức**: Kết hợp path parameter và query parameter, validation phạm vi

### 4. Phân Trang Bài Viết Blog (`/users/{user_id}/posts`)
- **Tham số đường dẫn**: `user_id`
- **Tham số truy vấn**: `limit` (mặc định=5), `offset` (mặc định=0)
- **Chức năng**: Trả về danh sách bài viết có phân trang
- **Ví dụ**: `GET /users/3/posts?limit=2&offset=1` → bỏ qua 1 bài, lấy 2 bài tiếp theo
- **Kiến thức**: Phân trang, slice dữ liệu

### 5. Tìm Kiếm Chuyến Bay (`/flights/{origin}/{destination}`)
- **Tham số đường dẫn**: `origin`, `destination`
- **Tham số truy vấn**: `date` (tùy chọn), `max_price` (tùy chọn)
- **Chức năng**: Lọc chuyến bay theo tuyến đường, ngày, giá tối đa
- **Ví dụ**: `GET /flights/NYC/LAX?date=2025-09-15&max_price=400`
- **Kiến thức**: Lọc dữ liệu phức tạp, validation định dạng ngày

### 6. Đặt Vé Xem Phim (`/cinemas/{cinema_id}/movies/{movie_id}/showtimes`)
- **Tham số đường dẫn**: `cinema_id`, `movie_id`
- **Tham số truy vấn**: `date` (bắt buộc), `limit` (mặc định=5)
- **Chức năng**: Xem lịch chiếu phim tại rạp cụ thể
- **Ví dụ**: `GET /cinemas/2/movies/10/showtimes?date=2025-09-14&limit=2`
- **Kiến thức**: Tham số bắt buộc trong query, xử lý dữ liệu phức tạp

## Khái Niệm Chính

- **Tham số bắt buộc vs tùy chọn**: Sử dụng giá trị mặc định để tạo tham số tùy chọn
- **Validation kiểu dữ liệu**: FastAPI tự động validate và chuyển đổi kiểu dữ liệu
- **Path vs Query Parameters**: Phân biệt tham số đường dẫn và tham số truy vấn
- **Xử lý lỗi**: Trả về mã trạng thái HTTP và thông báo lỗi phù hợp
- **Lọc dữ liệu**: Sử dụng tham số truy vấn để lọc kết quả
- **Phân trang**: Triển khai limit và offset cho phản hồi có phân trang
- **Validation ngày tháng**: Kiểm tra định dạng ngày trong tham số truy vấn
