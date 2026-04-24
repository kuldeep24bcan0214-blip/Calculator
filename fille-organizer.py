import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
}

def organize_files(path):
    files = os.listdir(path)
    total_files = len(files)

    moved_count = 0
    processed = 0
    category_count = {key: 0 for key in file_types}

    log = []

    for folder in file_types.keys():
        os.makedirs(os.path.join(path, folder), exist_ok=True)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue

        moved = False

        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):

                destination = os.path.join(path, folder, file)

                # Unique naming
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(destination):
                    destination = os.path.join(path, folder, f"{base}_{i}{ext}")
                    i += 1

                shutil.move(file_path, destination)

                category_count[folder] += 1
                moved_count += 1
                log.append(f"{file} → {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)

            base, ext = os.path.splitext(file)
            i = 1
            while os.path.exists(destination):
                destination = os.path.join(other_folder, f"{base}_{i}{ext}")
                i += 1

            shutil.move(file_path, destination)
            moved_count += 1
            log.append(f"{file} → Others")

        processed += 1
        progress_bar['value'] = (processed / total_files) * 100
        status_label.config(text=f"Processing: {file}")
        root.update_idletasks()

    # Save log file
    with open(os.path.join(path, "organizer_log.txt"), "w") as f:
        for line in log:
            f.write(line + "\n")

    return moved_count, category_count


def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)


def start_organizing():
    path = folder_path.get()

    if not path:
        messagebox.showerror("Error", "Please select a folder!")
        return

    progress_bar['value'] = 0
    status_label.config(text="Starting...")

    total, category_count = organize_files(path)

    result_text = f"Total files organized: {total}\n\n"
    for k, v in category_count.items():
        result_text += f"{k}: {v}\n"

    status_label.config(text="Done ✅")
    messagebox.showinfo("Success", result_text)


# roots
root = tk.Tk()
root.title("Ultimate File Organizer")
root.geometry("500x350")
root.configure(bg="#39bcbe")

folder_path = tk.StringVar()

title = tk.Label(root, text="📂 File Organizer", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=10)

entry = tk.Entry(root, textvariable=folder_path, width=50, bg="#2d2d2d", fg="white", insertbackground="white")
entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse Folder", command=select_folder, bg="#007acc", fg="white")
browse_btn.pack(pady=5)

organize_btn = tk.Button(root, text="Start Organizing", command=start_organizing, bg="#28a745", fg="white")
organize_btn.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="Status: Waiting...", bg="#2cb0cb", fg="white")
status_label.pack(pady=5)

root.mainloop()