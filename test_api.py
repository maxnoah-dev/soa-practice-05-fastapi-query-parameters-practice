"""
File test API cho Unit 7: Query Parameters
Chạy file này để test tất cả các endpoint
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_exercise_1():
    """Test Exercise 1: Filtering Numbers"""
    print("=== BÀI TẬP 1: LỌC SỐ ===")
    
    # Test case 1: Normal range
    response = requests.get(f"{BASE_URL}/filter?min=3&max=7")
    print(f"GET /filter?min=3&max=7")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: Single number
    response = requests.get(f"{BASE_URL}/filter?min=5&max=5")
    print(f"GET /filter?min=5&max=5")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: Error case
    response = requests.get(f"{BASE_URL}/filter?min=10&max=5")
    print(f"GET /filter?min=10&max=5 (Error case)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_exercise_2():
    """Test Exercise 2: Search Products"""
    print("=== BÀI TẬP 2: TÌM KIẾM SẢN PHẨM ===")
    
    # Test case 1: Search with keyword
    response = requests.get(f"{BASE_URL}/search?keyword=lap")
    print(f"GET /search?keyword=lap")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: Search with different keyword
    response = requests.get(f"{BASE_URL}/search?keyword=phone")
    print(f"GET /search?keyword=phone")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: No keyword (return all)
    response = requests.get(f"{BASE_URL}/search")
    print(f"GET /search (no keyword)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_exercise_3():
    """Test Exercise 3: Product Discount Calculation"""
    print("=== BÀI TẬP 3: TÍNH GIẢM GIÁ SẢN PHẨM ===")
    
    # Test case 1: With discount
    response = requests.get(f"{BASE_URL}/products/1?discount=10")
    print(f"GET /products/1?discount=10")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: No discount
    response = requests.get(f"{BASE_URL}/products/2")
    print(f"GET /products/2 (no discount)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: High discount
    response = requests.get(f"{BASE_URL}/products/3?discount=50")
    print(f"GET /products/3?discount=50")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_exercise_4():
    """Test Exercise 4: Paginated Blog Posts"""
    print("=== BÀI TẬP 4: PHÂN TRANG BÀI VIẾT BLOG ===")
    
    # Test case 1: Normal pagination
    response = requests.get(f"{BASE_URL}/users/3/posts?limit=2&offset=1")
    print(f"GET /users/3/posts?limit=2&offset=1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: Default parameters
    response = requests.get(f"{BASE_URL}/users/1/posts")
    print(f"GET /users/1/posts (default limit=5, offset=0)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: User not found
    response = requests.get(f"{BASE_URL}/users/999/posts")
    print(f"GET /users/999/posts (user not found)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_exercise_5():
    """Test Exercise 5: Flight Search"""
    print("=== BÀI TẬP 5: TÌM KIẾM CHUYẾN BAY ===")
    
    # Test case 1: With date and price filter
    response = requests.get(f"{BASE_URL}/flights/NYC/LAX?date=2025-09-15&max_price=400")
    print(f"GET /flights/NYC/LAX?date=2025-09-15&max_price=400")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: Only date filter
    response = requests.get(f"{BASE_URL}/flights/NYC/LAX?date=2025-09-16")
    print(f"GET /flights/NYC/LAX?date=2025-09-16")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: No filters
    response = requests.get(f"{BASE_URL}/flights/CHI/MIA")
    print(f"GET /flights/CHI/MIA (no filters)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_exercise_6():
    """Test Exercise 6: Movie Ticket Booking"""
    print("=== BÀI TẬP 6: ĐẶT VÉ XEM PHIM ===")
    
    # Test case 1: Normal request
    response = requests.get(f"{BASE_URL}/cinemas/2/movies/10/showtimes?date=2025-09-14&limit=2")
    print(f"GET /cinemas/2/movies/10/showtimes?date=2025-09-14&limit=2")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 2: Different cinema and movie
    response = requests.get(f"{BASE_URL}/cinemas/1/movies/20/showtimes?date=2025-09-14")
    print(f"GET /cinemas/1/movies/20/showtimes?date=2025-09-14")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test case 3: Invalid date format
    response = requests.get(f"{BASE_URL}/cinemas/1/movies/10/showtimes?date=invalid-date")
    print(f"GET /cinemas/1/movies/10/showtimes?date=invalid-date (invalid date)")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def main():
    """Chạy tất cả các test"""
    print("BAT DAU TEST API QUERY PARAMETERS")
    print("=" * 50)
    print()
    
    try:
        # Test server connection
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("Khong the ket noi den server!")
            print("Hay chay: python main.py")
            return
        
        print("Ket noi server thanh cong!")
        print()
        
        # Run all tests
        test_exercise_1()
        test_exercise_2()
        test_exercise_3()
        test_exercise_4()
        test_exercise_5()
        test_exercise_6()
        
        print("HOAN THANH TAT CA CAC TEST!")
        
    except requests.exceptions.ConnectionError:
        print("Loi ket noi!")
        print("Hay dam bao server dang chay: python main.py")
    except Exception as e:
        print(f"Loi: {e}")

if __name__ == "__main__":
    main()
