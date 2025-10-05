from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Query Parameters Practice", version="1.0.0")

# Exercise 1: Filtering Numbers
@app.get("/filter")
async def filter_numbers(min: int, max: int):
    """
    Filter numbers between min and max (inclusive).
    Query parameters:
    - min: minimum value (required)
    - max: maximum value (required)
    """
    if min > max:
        raise HTTPException(status_code=400, detail="min cannot be greater than max")
    
    numbers = list(range(min, max + 1))
    return {"numbers": numbers}

# Exercise 2: Search Products
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 500}
]

@app.get("/search")
async def search_products(keyword: Optional[str] = None):
    """
    Search products by keyword.
    Query parameters:
    - keyword: search term (optional, case-insensitive)
    """
    if keyword is None:
        return products
    
    keyword_lower = keyword.lower()
    filtered_products = [
        product for product in products 
        if keyword_lower in product["name"].lower()
    ]
    return filtered_products

# Exercise 3: Product Discount Calculation
products_dict = {
    1: {"name": "Laptop", "price": 1200},
    2: {"name": "Phone", "price": 800},
    3: {"name": "Tablet", "price": 500}
}

@app.get("/products/{product_id}")
async def get_product_with_discount(product_id: int, discount: int = 0):
    """
    Get product with optional discount.
    Path parameters:
    - product_id: product identifier
    Query parameters:
    - discount: discount percentage (optional, default=0)
    """
    if product_id not in products_dict:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if discount < 0 or discount > 100:
        raise HTTPException(status_code=400, detail="Discount must be between 0 and 100")
    
    product = products_dict[product_id]
    original_price = product["price"]
    final_price = original_price * (1 - discount / 100)
    
    return {
        "id": product_id,
        "name": product["name"],
        "original_price": original_price,
        "discount": discount,
        "final_price": round(final_price, 2)
    }

# Exercise 4: Paginated Blog Posts by User
# Sample blog posts data - Dữ liệu mẫu cho bài tập 4
blog_posts = {
    1: [
        {"id": 1, "title": "Học FastAPI cơ bản", "content": "Hướng dẫn tạo API với FastAPI"},
        {"id": 2, "title": "Query Parameters trong FastAPI", "content": "Cách sử dụng query parameters"},
        {"id": 3, "title": "Validation dữ liệu", "content": "Validate input với Pydantic"},
        {"id": 4, "title": "Error Handling", "content": "Xử lý lỗi trong FastAPI"},
        {"id": 5, "title": "API Documentation", "content": "Tạo tài liệu API tự động"}
    ],
    2: [
        {"id": 1, "title": "Python Tips & Tricks", "content": "Mẹo hay khi lập trình Python"},
        {"id": 2, "title": "Database Design", "content": "Thiết kế cơ sở dữ liệu hiệu quả"},
        {"id": 3, "title": "RESTful API Design", "content": "Nguyên tắc thiết kế REST API"}
    ],
    3: [
        {"id": 1, "title": "Bài viết đầu tiên", "content": "Nội dung bài viết đầu tiên của user 3"},
        {"id": 2, "title": "Bài viết thứ hai", "content": "Nội dung bài viết thứ hai của user 3"},
        {"id": 3, "title": "Bài viết thứ ba", "content": "Nội dung bài viết thứ ba của user 3"},
        {"id": 4, "title": "Bài viết thứ tư", "content": "Nội dung bài viết thứ tư của user 3"},
        {"id": 5, "title": "Bài viết thứ năm", "content": "Nội dung bài viết thứ năm của user 3"},
        {"id": 6, "title": "Bài viết thứ sáu", "content": "Nội dung bài viết thứ sáu của user 3"}
    ]
}

@app.get("/users/{user_id}/posts")
async def get_user_posts(user_id: int, limit: int = 5, offset: int = 0):
    """
    Get paginated blog posts for a user.
    Path parameters:
    - user_id: user identifier
    Query parameters:
    - limit: maximum number of posts to return (default=5)
    - offset: number of posts to skip (default=0)
    """
    if user_id not in blog_posts:
        raise HTTPException(status_code=404, detail="User not found")
    
    if limit < 0 or offset < 0:
        raise HTTPException(status_code=400, detail="limit and offset must be non-negative")
    
    user_posts = blog_posts[user_id]
    start_index = offset
    end_index = offset + limit
    paginated_posts = user_posts[start_index:end_index]
    
    return {
        "user_id": user_id,
        "posts": paginated_posts
    }

# Exercise 5: Flight Search by Route and Filters
# Sample flights data - Dữ liệu mẫu cho bài tập 5
flights_data = [
    {"flight_id": 101, "origin": "NYC", "destination": "LAX", "date": "2025-09-15", "price": 350},
    {"flight_id": 102, "origin": "NYC", "destination": "LAX", "date": "2025-09-15", "price": 450},
    {"flight_id": 103, "origin": "NYC", "destination": "LAX", "date": "2025-09-16", "price": 300},
    {"flight_id": 104, "origin": "NYC", "destination": "LAX", "date": "2025-09-16", "price": 500},
    {"flight_id": 201, "origin": "LAX", "destination": "NYC", "date": "2025-09-15", "price": 380},
    {"flight_id": 202, "origin": "LAX", "destination": "NYC", "date": "2025-09-16", "price": 320},
    {"flight_id": 301, "origin": "CHI", "destination": "MIA", "date": "2025-09-15", "price": 280},
    {"flight_id": 302, "origin": "CHI", "destination": "MIA", "date": "2025-09-16", "price": 290},
    {"flight_id": 401, "origin": "SFO", "destination": "SEA", "date": "2025-09-15", "price": 200},
    {"flight_id": 402, "origin": "SFO", "destination": "SEA", "date": "2025-09-16", "price": 180}
]

@app.get("/flights/{origin}/{destination}")
async def search_flights(
    origin: str, 
    destination: str, 
    date: Optional[str] = None, 
    max_price: Optional[int] = None
):
    """
    Search flights by route with optional filters.
    Path parameters:
    - origin: departure airport code
    - destination: arrival airport code
    Query parameters:
    - date: flight date in YYYY-MM-DD format (optional)
    - max_price: maximum price filter (optional)
    """
    # Filter by origin and destination
    filtered_flights = [
        flight for flight in flights_data 
        if flight["origin"] == origin.upper() and flight["destination"] == destination.upper()
    ]
    
    # Filter by date if provided
    if date:
        try:
            # Validate date format
            datetime.strptime(date, "%Y-%m-%d")
            filtered_flights = [
                flight for flight in filtered_flights 
                if flight["date"] == date
            ]
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    # Filter by max_price if provided
    if max_price is not None:
        if max_price < 0:
            raise HTTPException(status_code=400, detail="max_price must be non-negative")
        filtered_flights = [
            flight for flight in filtered_flights 
            if flight["price"] <= max_price
        ]
    
    return filtered_flights

# Exercise 6: Movie Ticket Booking System
# Sample showtimes data - Dữ liệu mẫu cho bài tập 6
showtimes_data = {
    (1, 10): [  # cinema_id=1, movie_id=10 (Avengers)
        {"time": "10:00", "available_seats": 50, "date": "2025-09-14"},
        {"time": "14:00", "available_seats": 30, "date": "2025-09-14"},
        {"time": "18:00", "available_seats": 25, "date": "2025-09-14"},
        {"time": "22:00", "available_seats": 40, "date": "2025-09-14"},
        {"time": "10:00", "available_seats": 45, "date": "2025-09-15"},
        {"time": "14:00", "available_seats": 20, "date": "2025-09-15"}
    ],
    (2, 10): [  # cinema_id=2, movie_id=10 (Avengers)
        {"time": "14:00", "available_seats": 45, "date": "2025-09-14"},
        {"time": "17:30", "available_seats": 20, "date": "2025-09-14"},
        {"time": "21:00", "available_seats": 35, "date": "2025-09-14"},
        {"time": "12:00", "available_seats": 50, "date": "2025-09-15"},
        {"time": "16:00", "available_seats": 30, "date": "2025-09-15"}
    ],
    (1, 20): [  # cinema_id=1, movie_id=20 (Spider-Man)
        {"time": "11:00", "available_seats": 60, "date": "2025-09-14"},
        {"time": "15:00", "available_seats": 40, "date": "2025-09-14"},
        {"time": "19:00", "available_seats": 55, "date": "2025-09-14"},
        {"time": "13:00", "available_seats": 35, "date": "2025-09-15"},
        {"time": "17:00", "available_seats": 45, "date": "2025-09-15"}
    ],
    (2, 20): [  # cinema_id=2, movie_id=20 (Spider-Man)
        {"time": "12:30", "available_seats": 40, "date": "2025-09-14"},
        {"time": "16:30", "available_seats": 25, "date": "2025-09-14"},
        {"time": "20:30", "available_seats": 50, "date": "2025-09-14"}
    ],
    (3, 30): [  # cinema_id=3, movie_id=30 (Batman)
        {"time": "09:00", "available_seats": 70, "date": "2025-09-14"},
        {"time": "13:00", "available_seats": 55, "date": "2025-09-14"},
        {"time": "17:00", "available_seats": 40, "date": "2025-09-14"},
        {"time": "21:00", "available_seats": 60, "date": "2025-09-14"}
    ]
}

@app.get("/cinemas/{cinema_id}/movies/{movie_id}/showtimes")
async def get_movie_showtimes(
    cinema_id: int, 
    movie_id: int, 
    date: str, 
    limit: int = 5
):
    """
    Get available showtimes for a movie in a cinema.
    Path parameters:
    - cinema_id: cinema identifier
    - movie_id: movie identifier
    Query parameters:
    - date: show date in YYYY-MM-DD format (required)
    - limit: maximum number of showtimes to return (optional, default=5)
    """
    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit must be non-negative")
    
    # Check if cinema/movie combination exists
    key = (cinema_id, movie_id)
    if key not in showtimes_data:
        raise HTTPException(status_code=404, detail="No showtimes found for this cinema and movie combination")
    
    # Filter by date
    available_showtimes = [
        showtime for showtime in showtimes_data[key] 
        if showtime["date"] == date
    ]
    
    # Apply limit
    limited_showtimes = available_showtimes[:limit]
    
    # Remove date from response as it's already in the request
    response_showtimes = [
        {"time": showtime["time"], "available_seats": showtime["available_seats"]}
        for showtime in limited_showtimes
    ]
    
    return {
        "cinema_id": cinema_id,
        "movie_id": movie_id,
        "date": date,
        "showtimes": response_showtimes
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Query Parameters Practice API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
