import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog

class PdfLibrary:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Library")
        self.pdf_files = []

        self.add_button = tk.Button(self.root, text="Add PDF", command=self.add_pdf)
        self.add_button.pack(pady=10)

        self.pdf_listbox = tk.Listbox(self.root, width=50, height=10)
        self.pdf_listbox.pack(pady=10)

        self.view_button = tk.Button(self.root, text="View PDF", command=self.view_pdf)
        self.view_button.pack(pady=10)

    def add_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_files.append(file_path)
            self.pdf_listbox.insert(tk.END, file_path)

    def view_pdf(self):
        selected_file = self.pdf_listbox.get(tk.ACTIVE)
        if selected_file:
            os.startfile(selected_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = PdfLibrary(root)
    root.mainloop()
