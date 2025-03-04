import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def split_pdf(pdf_path, ranges):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    for i, page_range in enumerate(ranges):
        pdf_writer = PyPDF2.PdfWriter()
        start, end = page_range
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = 'C:\\Users\\micha\\Documents\\' + f'output_{i + 1}.pdf'
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


def open_pdf(ranges_label, pages_label):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_reader = PyPDF2.PdfReader(file_path)
        num_pages = len(pdf_reader.pages)
        pages_label.config(text=f"Number of pages: {num_pages}")
        ranges = get_page_ranges(num_pages)
        if ranges:
            split_pdf(file_path, ranges)
            messagebox.showinfo("PDF Split", f"PDFs saved to Documents")
        else:
            messagebox.showerror("Error", "Invalid page ranges")