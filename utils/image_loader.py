import os
from PIL import Image

def load_and_resize_image():
    images_dir = "images"
    
    if not os.path.exists(images_dir):
        raise FileNotFoundError(f"Folder 'images' tidak ditemukan")
    
    image_files = []
    for file in os.listdir(images_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_files.append(file)
    
    if not image_files:
        raise FileNotFoundError(f"Tidak ada file gambar di folder 'images'")
    
    image_path = os.path.join(images_dir, image_files[0])
    print(f"Menggunakan gambar: {image_files[0]}")
    
    try:
        image = Image.open(image_path)
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        original_width, original_height = image.size
        
        new_width = 90  
        new_height = 40 
        
        print(f"Ukuran asli: {original_width}x{original_height}")
        print(f"Ukuran fixed: {new_width}x{new_height} (3:4)")
        
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return resized_image
        
    except Exception as e:
        raise Exception(f"Error memuat gambar: {str(e)}")