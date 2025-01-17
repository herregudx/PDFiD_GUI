import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filename:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, filename)

def run_pdfid():
    pdf_file = entry_file.get()
    if pdf_file:
        pdfid_path = os.path.join(os.path.dirname(__file__), "pdfid.py")  # pdfid.py directory
        if not os.path.exists(pdfid_path):
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, "Error: pdfid.py not found. Please place it in the same folder as this script.")
            return
        
        try:
            result = subprocess.run(["python", pdfid_path, pdf_file], capture_output=True, text=True, shell=True)
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, result.stdout + result.stderr)
        except Exception as e:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, f"Error: {e}")

# Main window
root = tk.Tk()
root.title("PDFiD GUI")
root.geometry("500x600")

# File selection
frame_top = tk.Frame(root)
frame_top.pack(pady=10, padx=10, fill=tk.X)

entry_file = tk.Entry(frame_top, width=50)
entry_file.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

btn_browse = tk.Button(frame_top, text="Browse", command=browse_file)
btn_browse.pack(side=tk.RIGHT, padx=5)

# Run button
btn_run = tk.Button(root, text="Run PDFiD", command=run_pdfid)
btn_run.pack(pady=5)

# Output text box
text_output = scrolledtext.ScrolledText(root, height=20)
text_output.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)

root.mainloop()
