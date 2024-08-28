import os
import shutil

# 다운로드 폴더 경로
download_folder = r'c:\Users\student\Downloads'

# 파일을 이동할 폴더 경로
folders = {
    'images': ['*.jpg', '*.jpeg', '*.webp'],
    'data': ['*.csv', '*.xlsx'],
    'docs': ['*.txt', '*.doc', '*.pdf'],
    'archive': ['*.zip']
}

# 각 폴더가 없으면 생성
for folder in folders:
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동 함수
def move_files(file_patterns, destination_folder):
    for pattern in file_patterns:
        for file_name in os.listdir(download_folder):
            if file_name.lower().endswith(tuple(pattern.replace('*', '').split())):
                source = os.path.join(download_folder, file_name)
                destination = os.path.join(destination_folder, file_name)
                shutil.move(source, destination)
                print(f"Moved: {file_name} -> {destination_folder}")

# 파일 이동 수행
for folder, patterns in folders.items():
    destination_folder = os.path.join(download_folder, folder)
    move_files(patterns, destination_folder)
