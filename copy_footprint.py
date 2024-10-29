import os
import shutil

# Đường dẫn thư mục nguồn và thư mục đích
source_folder = r"D:\Allegro\Project\CanhMai\Lib\Schematic_And_FootPrint"
destination_folder = r"C:\Cadence\SPB_17.4\share\pcb\pcb_lib\symbols"

# Hàm đếm số lượng file với các đuôi cụ thể
def count_files(folder, extensions):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                count += 1
    return count

# Đếm số file trước khi copy
extensions = ('.pad', '.psm', '.dra','.ssm')
source_file_count = count_files(source_folder, extensions)
destination_file_count_before = count_files(destination_folder, extensions)

print(f"Số file hợp lệ trong thư mục nguồn: {source_file_count}")
print(f"Số file hợp lệ trong thư mục đích trước khi copy: {destination_file_count_before}")

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(destination_folder, exist_ok=True)

# Duyệt qua tất cả các thư mục con và file trong thư mục nguồn
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Kiểm tra nếu file có đuôi .PAD, .psm, .pad, .DRA
        if file.lower().endswith(extensions):
            # Đường dẫn đầy đủ của file nguồn
            source_file = os.path.join(root, file)
            # Đường dẫn đầy đủ của file đích
            destination_file = os.path.join(destination_folder, file)
            
            # Thực hiện copy file
            shutil.copy2(source_file, destination_file)
            print(f"Đã copy: {source_file} -> {destination_file}")

# Đếm số file sau khi copy
destination_file_count_after = count_files(destination_folder, extensions)

print(f"Số file hợp lệ trong thư mục đích sau khi copy: {destination_file_count_after}")
print("Hoàn tất việc copy các file.")
