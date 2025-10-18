# ProPartners Landing Page - Streamlit Version

## Mô tả
Landing page cho ProPartners - International Affiliate & Marketing được chuyển đổi từ React sang Streamlit.

## Cài đặt và Chạy

### 1. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 2. Chạy ứng dụng
```bash
streamlit run app.py
```

### 3. Truy cập
Mở trình duyệt và truy cập: `http://localhost:8501`

## Tính năng

### ✅ Đã implement:
- **🌐 Multilingual Support**: Hỗ trợ tiếng Anh và tiếng Việt với language switcher
- **Responsive Design**: Tương thích đa thiết bị
- **Navigation Bar**: Fixed navbar với smooth navigation và language toggle
- **Hero Section**: Với thống kê và CTA buttons  
- **Services Section**: 6 dịch vụ cốt lõi với cards layout
- **Why Us Section**: Lý do chọn ProPartners với KPI stats
- **Regions Section**: Khu vực trọng điểm
- **Process Section**: 4 bước quy trình hợp tác
- **Case Studies**: 3 case study tiêu biểu
- **Compliance Section**: 6 nguyên tắc tuân thủ
- **Contact Form**: Form liên hệ với validation (đa ngôn ngữ)
- **Footer**: Thông tin bản quyền và links

### 🎨 Styling:
- Custom CSS giống Tailwind design gốc
- Smooth transitions và hover effects
- Mobile-first responsive design
- Modern card layouts với shadows

### 📝 Form Handling:
- Streamlit form widgets
- Client-side validation
- Success/error messages
- Structured data collection

## Cấu trúc file
```
Landing Page/
├── app.py              # Main Streamlit application
├── content.py          # Multilingual content dictionary
├── requirements.txt    # Python dependencies  
└── README.md          # Documentation
```

## 🌐 Multilingual Features

### Language Support:
- **English (EN)** - Default language 🇺🇸
- **Vietnamese (VI)** - Localized content 🇻🇳

### Language Switcher:
- Located in top-right corner of navbar
- Displays current language flag and code
- Click to toggle between EN/VI
- Uses Streamlit session state for persistence

### Content Management:
All content is stored in `content.py` with structured dictionary:
```python
CONTENT = {
    "en": { ... },  # English content
    "vi": { ... }   # Vietnamese content
}
```

## Customization

### Thêm/sửa sections:
Mỗi section được tách thành function riêng trong `app.py`:
- `render_hero()`
- `render_services()`  
- `render_contact_form()`
- etc.

### Styling:
Tất cả CSS được định nghĩa trong function `load_css()` ở đầu file `app.py`.

### Form processing:
Modify function `render_contact_form()` để tích hợp với email service, database, v.v.

## Deployment Options

### Streamlit Cloud:
1. Push code lên GitHub
2. Connect với Streamlit Cloud
3. Deploy tự động

### Local Server:
```bash
streamlit run app.py --server.port 8501
```

### Docker:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## So sánh với React version

### ✅ Advantages of Streamlit:
- **Nhanh hơn**: Không cần build process
- **Đơn giản hơn**: Python-only, không cần HTML/CSS/JS
- **Form handling**: Built-in widgets và validation
- **Deployment**: Dễ deploy hơn với Streamlit Cloud

### ⚠️ Limitations:
- **Performance**: Chậm hơn React cho complex interactions
- **Customization**: Hạn chế hơn trong việc customize UI
- **SEO**: Không tốt bằng static HTML/React
- **Animation**: Hạn chế trong complex animations

## Next Steps

1. **Backend Integration**: Tích hợp form với email/database
2. **Analytics**: Thêm Google Analytics
3. **SEO**: Thêm meta tags và structured data
4. **Performance**: Optimize loading và caching
5. **Content Management**: Tách content ra separate files