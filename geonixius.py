import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("GEONIXIUS")
root.geometry("1200x750")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="GEONIXIUS",
    font=("Segoe UI", 28, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Geospatial Survey Engineering Suite",
    font=("Segoe UI", 12),
    fg="#94a3b8",
    bg="#0f172a"
)
subtitle.pack()

frame = tk.Frame(root, bg="#111827")
frame.pack(fill="both", expand=True, padx=20, pady=20)

modules = [
    "Bowditch",
    "Least Square",
    "Waterpass",
    "GNSS Baseline"
]

for item in modules:
    btn = tk.Button(
        frame,
        text=item,
        font=("Segoe UI", 12, "bold"),
        bg="#1e293b",
        fg="white",
        relief="flat",
        height=2
    )
    btn.pack(fill="x", padx=20, pady=10)

def start():
    messagebox.showinfo("GEONIXIUS", "System Ready")

run_btn = tk.Button(
    root,
    text="Start Processing",
    command=start,
    font=("Segoe UI", 12, "bold"),
    bg="#22c55e",
    fg="black",
    relief="flat"
)
run_btn.pack(pady=20)

root.mainloop()
