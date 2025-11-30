import time
import random
import sys
import numpy as np

def get_brightness_map(image_data):
    pixels = image_data.load()
    width, height = image_data.size
    
    brightness_map = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            brightness = (r + g + b) / 3
            brightness_map.append((x, y, brightness))
    
    return brightness_map

def detect_edges_and_important_areas(image_data):
    pixels = image_data.load()
    width, height = image_data.size
    
    important_pixels = []
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            brightness = (r + g + b) / 3
            
            edge_score = 0
            neighbors = [
                (x-1, y), (x+1, y), (x, y-1), (x, y+1),
                (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)
            ]
            
            for nx, ny in neighbors:
                if 0 <= nx < width and 0 <= ny < height:
                    nr, ng, nb = pixels[nx, ny]
                    neighbor_brightness = (nr + ng + nb) / 3
                    edge_score += abs(brightness - neighbor_brightness)
            
            priority = edge_score
            priority += random.uniform(0, 30)
            
            important_pixels.append((x, y, priority))
    
    important_pixels.sort(key=lambda p: p[2], reverse=True)
    
    return important_pixels

def artistic_animation(image_data):
    from utils.char_mapper import pixel_to_char
    
    pixels = image_data.load()
    width, height = image_data.size
    
    print("\033[2J\033[H")
    print("=" * 70)
    print("MELUKIS GAMBAR")
    print(f"Dimensi: {width} x {height} karakter")
    print("=" * 70)
    print()
    
    canvas_start_line = 6
    
    print("╔" + "═" * width + "╗")
    for y in range(height):
        print("║" + " " * width + "║")
    print("╚" + "═" * width + "╝")
    
    time.sleep(0.3)
    
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    drawn = [[False for _ in range(width)] for _ in range(height)]
    
    important_pixels = detect_edges_and_important_areas(image_data)
    
    phase1_count = int(len(important_pixels) * 0.30)
    
    for i in range(phase1_count):
        x, y, _ = important_pixels[i]
        
        if not drawn[y][x]:
            r, g, b = pixels[x, y]
            char = pixel_to_char(r, g, b)
            canvas[y][x] = char
            drawn[y][x] = True
            
            if i % 8 == 0 or i == phase1_count - 1:
                render_canvas_with_frame(canvas, pixels, width, height, canvas_start_line)
                time.sleep(0.15)
    
    phase2_count = int(len(important_pixels) * 0.70)
    
    for i in range(phase1_count, phase2_count):
        x, y, _ = important_pixels[i]
        
        if not drawn[y][x]:
            r, g, b = pixels[x, y]
            char = pixel_to_char(r, g, b)
            canvas[y][x] = char
            drawn[y][x] = True
            
            if i % 12 == 0 or i == phase2_count - 1:
                render_canvas_with_frame(canvas, pixels, width, height, canvas_start_line)
                time.sleep(0.15)
    
    remaining_pixels = []
    
    for y in range(height):
        for x in range(width):
            if not drawn[y][x]:
                remaining_pixels.append((x, y))
    
    random.shuffle(remaining_pixels)
    
    for i, (x, y) in enumerate(remaining_pixels):
        r, g, b = pixels[x, y]
        char = pixel_to_char(r, g, b)
        canvas[y][x] = char
        drawn[y][x] = True
        
        if i % 18 == 0 or i == len(remaining_pixels) - 1:
            render_canvas_with_frame(canvas, pixels, width, height, canvas_start_line)
            time.sleep(0.15)
    
    render_canvas_with_frame(canvas, pixels, width, height, canvas_start_line)
    
    return canvas

def render_canvas_with_frame(canvas, pixels, width, height, start_line):
    for y in range(height):
        print(f"\033[{start_line + y};H║", end="")
        
        line = ""
        for x in range(width):
            char = canvas[y][x]
            if char != ' ':
                r, g, b = pixels[x, y]
                line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            else:
                line += " "
        
        print(line + "║")
    
    sys.stdout.flush()

def show_loading_message(image_width, image_height):
    print(f"Mempersiapkan canvas... ({image_width}x{image_height})")
    print("Pastikan terminal Anda cukup lebar!")
    time.sleep(0.5)

def show_completion_message():
    print("=" * 70)
    print("Lukisan ASCII selesai!")
    print("Dibuat dengan teknik artistic rendering")
    print("=" * 70)