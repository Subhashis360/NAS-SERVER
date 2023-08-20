import tkinter as tk
from tkinter import filedialog
import requests

root = tk.Tk()

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        files = {'file': open(file_path, 'rb')}
        response = requests.post('http://localhost:5000/upload', files=files)
        print(response.text)

def download_file():
    filename = filedialog.askstring("Download File", "Enter filename:")
    if filename:
        response = requests.get(f'http://localhost:5000/download/{filename}')
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully")

upload_button = tk.Button(root, text="Upload File", command=upload_file)
download_button = tk.Button(root, text="Download File", command=download_file)

upload_button.pack()
download_button.pack()

root.mainloop()