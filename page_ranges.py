import tkinter
from tkinter import simpledialog, messagebox


def get_page_ranges(num_pages):
    ranges = []
    while True:
        range_str = simpledialog.askstring("Page ranges", "Enter a page range (e.g. 1-5) or 'q' to finish:")
        if range_str.lower() == 'q':
            break
        try:
            start, end = map(int, range_str.split('-'))
            if start < 1 or end > num_pages or start > end:
                raise ValueError
            ranges.append((start, end))
        except ValueError:
            messagebox.showerror("Error", "Invalid page range or out of bounds")
    return ranges
