import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pdf_reader import open_pdf

# Function to create the GUI for the program
def create_gui():
    root = tk.Tk()
    root.title("PDF Splitter")

    label = tk.Label(root, text="Select a PDF file to split:")
    label.pack(padx=50, pady=10)

    pages_label = tk.Label(root, text="Number of pages: ")
    pages_label.pack(pady=10)

    ranges_label = tk.Label(root, text="Current ranges: ")
    ranges_label.pack(pady=10)

    open_button = tk.Button(root, text="Open PDF", command=lambda: open_pdf(ranges_label, pages_label))
    open_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()