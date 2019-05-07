# newsfx
> Dự án đang trong quá trình thực hiện

## Bắt đầu nhanh
### Cài đặt
```
pip install newsfx
```

### Thực hiện
```python
import newsfx
data = newsfx('https://vnexpress.net/thoi-su/nguoi-dan-un-un-tro-lai-sai-gon-ha-noi-sau-ky-nghi-le-3917122.html')
print(data) # return dictionary
```

## Trang tin hỗ trợ

| news site          | title | published_date | summary | content | author | top_image |
|--------------------|:-----:|----------------|---------|---------|--------|-----------|
| VnExpress          | ✔️   |                |         |         |        |           |
| Tuổi Trẻ Online    | ✔️   |                |         |         |        |           |
| Thanh Niên         |       |                |         |         |        |           |
| Tiền Phong         |       |                |         |         |        |           |
| Lao Động           |       |                |         |         |        |           |
| Báo mới            |       |                |         |         |        |           |
| Người Lao Động     |       |                |         |         |        |           |
| Nhân Dân           |       |                |         |         |        |           |
| Đời Sống Pháp Luật |       |                |         |         |        |           |
| Vietnamnet         |       |                |         |         |        |           |
| Zing News          |       |                |         |         |        |           |
| Dân Trí            |       |                |         |         |        |           |
| Nhịp Sống Số       |       |                |         |         |        |           |
| Tri Thức Trẻ       |       |                |         |         |        |           |
| Vietnam Plus       |       |                |         |         |        |           |


## TODO
- [ ] Tự động nhận dạng url đầu vào
- [ ] Định dạng kết quả trả về trong dictionary

|     Tên    	| Kiểu trả về 	|                 Mô tả                 	| Hỗ trợ 	|
|------------	|-------------	|---------------------------------------	|:------:	|
| title      	|    string   	| Tiêu đề bài viết                      	|        	|
| html       	|    string   	| Code html bài viết                    	|        	|
| text       	|    string   	| Nội dung bài viết chưa được xử lý     	|        	|
| clean_text 	|    string   	| Nội dung bài viết đã được xử lý       	|        	|
| author     	|     list    	| Tác giả bài viết                      	|        	|
| published  	|     date    	| Ngày đăng bài viết                    	|        	|
| top_image  	|    string   	| Hình ảnh đặc trưng của bài viết       	|        	|
| images     	|     list    	| Danh sách hình ảnh có trong bài viết  	|        	|
| keywords   	|     list    	| Từ khóa bài viết (có sẵn từ bài viết) 	|        	|
