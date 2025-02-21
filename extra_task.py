import requests
import json
import tkinter as tk
from PIL import Image, ImageTk
import io
import threading


WHITE = "#ffffff"
BLACK = "#000000"


def get_image():

    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    # print(data)

    img = data['image']
    res_img = requests.get(img)                         # Use requests to get photos from website
    img_main = res_img.content                         
  
    img_convert = Image.open(io.BytesIO(img_main))      # Convert binary data to a PIL image object
    return img_convert


def new_image():
    threading.Thread(target=update_image).start()       # Use threading to call update_image


def new_image():
    new_img = get_image()                               # To get new photo
    img_tk = ImageTk.PhotoImage(new_img)                # Convert it to an image object that tkinter can use
    label.config(image=img_tk)                          
    label.image = img_tk                                # Keep the reference to the image


if __name__ == '__main__':

    root = tk.Tk()
    root.title("New")
    root.geometry("{}x{}".format(800, 600))

    # Load initial image
    img = get_image()
    img_tk = ImageTk.PhotoImage(img)

    # Create and place the image label
    label = tk.Label(root, image=img_tk)
    label.pack()

    change = tk.Button(root, text="Change photos", font=("Cambria", 15), bg=BLACK, fg=WHITE, command=new_image)
    change.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()



# from PIL import Image

# try:
#     img = Image.new('RGB', (100, 100), color = 'red')
#     img.show()
#     print("Pillow hoạt động đúng.")
# except Exception as e:
#     print(f"Lỗi: {e}")


