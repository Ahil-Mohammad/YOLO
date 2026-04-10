import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO
from collections import Counter

model = YOLO('yolo11m.pt') 

def generate_smart_description(found_objects):
    """Turns a list of objects into a natural sentence."""
    if not found_objects:
        return "I've looked closely, but I don't see any familiar objects here."
    
    counts = Counter(found_objects)
    
    parts = []
    for obj, count in counts.items():
        name = f"{count} {obj}{'s' if count > 1 else ''}"
        parts.append(name)
    
    if len(parts) > 1:
        desc = ", ".join(parts[:-1]) + " and " + parts[-1]
    else:
        desc = parts[0]
        
    return f"This image contains {desc}."

def upload_and_detect():
    file_path = filedialog.askopenfilename()
    if not file_path: return

    results = model(file_path)[0]
    
    res_plotted = results.plot()
    img_rgb = Image.fromarray(res_plotted[:, :, ::-1])
    img_rgb.thumbnail((500, 500))
    
    tk_img = ImageTk.PhotoImage(img_rgb)
    image_label.config(image=tk_img)
    image_label.image = tk_img

    names = results.names
    found = [names[int(c)] for c in results.boxes.cls.tolist()]
    
    final_text = generate_smart_description(found)
    result_text.set(final_text)

root = tk.Tk()
root.title("AI Vision")
root.geometry("600x750")
root.configure(bg="#f0f0f0")

tk.Label(root, text="AI Scene Interpreter", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=15)

btn = tk.Button(root, text="Select Image to Analyze", command=upload_and_detect, 
                font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10)
btn.pack(pady=10)

image_label = tk.Label(root, bg="#f0f0f0")
image_label.pack(pady=10)

result_text = tk.StringVar(value="Upload an image to begin...")
desc_label = tk.Label(root, textvariable=result_text, font=("Arial", 13, "italic"), 
                      wraplength=500, bg="#f0f0f0", fg="#333")
desc_label.pack(pady=20)
root.mainloop()
