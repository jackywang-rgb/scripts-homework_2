import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx"],
    "Compressed": [".zip", ".7z"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Cad": [".stl", ".f3z"],
    "application":[".stl",".f3z"],
    "cad":[".stl",".f3z",".sldprt",".sldasm",".slddrw",".igs",".iges",".step",".stp",".x_t",".x_b"],
    "Other": []
}

# 資料夾路徑
downloadpath = os.path.expanduser("D:/系統/下載/downloads")

# 遍歷 Download 資料夾內的所有檔案
for filename in os.listdir(downloadpath):
    file_path = os.path.join(downloadpath, filename) 
    # 跳過資料夾，只處理檔案
    if os.path.isdir(file_path):
        continue

    # 避免大小寫差異
    ext = os.path.splitext(filename)[1].lower()

    # 判斷檔案分類
    moved = False
    for folder, extensions in file_types.items():
        if ext in extensions:
            target_folder = os.path.join(downloadpath, folder)
            moved = True
            break
    if not moved:
        target_folder = os.path.join(downloadpath, "Other")

    # 目標資料夾不存在就建立
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

  

    shutil.move(file_path, os.path.join(target_folder, filename))  
    print(f"移動：{filename} → {target_folder}")
