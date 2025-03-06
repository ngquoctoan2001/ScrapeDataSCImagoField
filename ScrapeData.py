import requests
from bs4 import BeautifulSoup

# Địa chỉ URL của trang web bạn muốn cào dữ liệu
url = "https://www.scimagojr.com/journalrank.php"

# Thêm header để giả lập trình duyệt
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Gửi yêu cầu HTTP với header
response = requests.get(url, headers=headers)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Phân tích HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm tất cả các thẻ <div> chứa <ul> với class 'dropdown-options dropdown-element'
    div_tags = soup.find_all('div', class_='dropdown')
    
    # Kiểm tra xem có đủ div không và chọn div thứ 2 (index 1)
    if len(div_tags) >= 2:
        second_div = div_tags[1]  # Lấy div thứ hai
        
        # Tìm thẻ <ul> trong div thứ hai
        ul_tag = second_div.find('ul', class_='dropdown-options dropdown-element')
        
        if ul_tag:  # Kiểm tra xem thẻ <ul> có tồn tại không
            # Lấy tất cả các thẻ <li> trong <ul>
            li_tags = ul_tag.find_all('li')
            for li in li_tags:
                # Tìm thẻ <a> trong mỗi <li>
                a_tag = li.find('a')
                if a_tag:  # Kiểm tra xem thẻ <a> có tồn tại không
                    # Lấy nội dung văn bản của thẻ <a>
                    text = a_tag.text.strip()
                    # Chỉ in nội dung văn bản
                    print(text)
        else:
            print("Không tìm thấy thẻ <ul> trong div thứ hai.")
    else:
        print("Không đủ thẻ <div> để chọn div thứ hai.")
else:
    print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")