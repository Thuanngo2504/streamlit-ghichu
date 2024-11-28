# backgrounds.py

import os

# Lấy danh sách tất cả hình ảnh trong thư mục 'images'
image_folder = "images"
backgrounds = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
