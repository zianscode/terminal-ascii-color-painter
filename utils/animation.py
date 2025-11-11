import time
import random
import sys

def typing_animation(image_data):
    from utils.char_mapper import pixel_to_char
    
    pixels = image_data.load()
    width, height = image_data.size
    
    print("\033[2J\033[H")
    
    print("Sedang melukis gambar...")
    print("Mohon tunggu sebentar...")
    print(f"Dimensi: {width} x {height} karakter\n")
    time.sleep(0.1)
    
    printed_chars = [[' ' for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            char = pixel_to_char(r, g, b)
            
            printed_chars[y][x] = char
            
            current_line = ""
            for cx in range(width):
                if cx <= x: 
                    r_current, g_current, b_current = pixels[cx, y]
                    current_line += f"\033[38;2;{r_current};{g_current};{b_current}m{printed_chars[y][cx]}\033[0m"
                else:  
                    current_line += " "
            
            print(f"\033[{y + 5};H{current_line}", end="")
            sys.stdout.flush()
            
            delay_time = random.uniform(0.015, 0.00005)
            time.sleep(delay_time)
        
        if y % 3 == 0:
            time.sleep(0.0001)
    
    return printed_chars

def show_loading_message(image_width, image_height):
    print(f"Memulai animasi... ({image_width}x{image_height})")
    print("Pastikan terminal Anda cukup lebar!")
    time.sleep(0.1)

def show_completion_message():
    print("\n" + "=" * 60)
    print("Lukisan ASCII selesai!")
    print("=" * 60)