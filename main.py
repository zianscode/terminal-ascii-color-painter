import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.image_loader import load_and_resize_image
from utils.animation import artistic_animation, show_loading_message, show_completion_message

def main():
    try:
        print("=" * 70)
        print("TERMINAL ASCII COLOR PAINTER - FIXED 3:4")
        print("=" * 70)
        
        image = load_and_resize_image()
        
        show_loading_message(image.size[0], image.size[1])
        
        artistic_animation(image)
        
        show_completion_message()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nPastikan ada folder 'images/' dengan file gambar di dalamnya")
        
    except Exception as e:
        print(f"Error tidak terduga: {e}")

if __name__ == "__main__":
    main()