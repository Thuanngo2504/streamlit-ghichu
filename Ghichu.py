import streamlit as st
import os
import random
from backgrounds import backgrounds  # Import danh sách hình nền từ backgrounds.py

# Chọn ngẫu nhiên một hình nền từ danh sách
background_image = random.choice(backgrounds)

# Chèn CSS để thêm background từ hình ảnh trong thư mục
st.markdown(f"""
    <style>
    .main {{
        background-image: url('{background_image}');
        background-size: cover;
        background-position: center center;
        height: 100vh;
    }}
    </style>
    """, unsafe_allow_html=True)

# Tạo giao diện chính
st.title("Ứng dụng Ghi Chú")
st.subheader("Quản lý ghi chú của bạn dễ dàng với Streamlit!")

# Tạo thư mục lưu trữ ghi chú nếu chưa có
if not os.path.exists("notes"):
    os.makedirs("notes")

# Form để tạo ghi chú mới
st.header("Tạo Ghi Chú Mới")
note_title = st.text_input("Tiêu đề ghi chú")
note_content = st.text_area("Nội dung ghi chú")

if st.button("Lưu Ghi Chú"):
    if note_title and note_content:
        # Lưu ghi chú vào file
        with open(f"notes/{note_title}.txt", "w", encoding="utf-8") as f:
            f.write(note_content)
        st.success(f"Ghi chú '{note_title}' đã được lưu!")
    else:
        st.error("Vui lòng nhập đầy đủ tiêu đề và nội dung.")

# Hiển thị danh sách ghi chú
st.header("Danh Sách Ghi Chú")
notes = os.listdir("notes")
if notes:
    for note in notes:
        with st.expander(note):
            with open(f"notes/{note}", "r", encoding="utf-8") as f:
                st.write(f.read())
else:
    st.info("Chưa có ghi chú nào. Hãy thêm ghi chú mới!")

# Tùy chọn xóa ghi chú
st.header("Xóa Ghi Chú")
delete_note = st.selectbox("Chọn ghi chú để xóa", options=notes if notes else ["Không có ghi chú"])
if st.button("Xóa Ghi Chú"):
    if delete_note != "Không có ghi chú":
        os.remove(f"notes/{delete_note}")
        st.warning(f"Ghi chú '{delete_note}' đã bị xóa!")
    else:
        st.info("Không có ghi chú nào để xóa.")
