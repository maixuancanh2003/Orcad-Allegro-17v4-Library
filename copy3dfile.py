import os

# Đường dẫn thư mục nguồn và thư mục đích
source_folder = r"D:\Allegro\Project\CanhMai\Lib\Schematic_And_FootPrint"
destination_folder = r"C:\Cadence\SPB_17.4\share\local\pcb\step"

# Hàm đếm số lượng file .step và .stp trong một thư mục
def count_step_files(folder_path):
    return sum(
        1 for root, dirs, files in os.walk(folder_path) for file in files if file.lower().endswith(('.step', '.stp'))
    )

# Đếm số file trước khi copy
source_file_count = count_step_files(source_folder)
destination_file_count_before = count_step_files(destination_folder)

# Thực hiện copy các file như trong yêu cầu
import shutil
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith(('.step', '.stp')):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy2(source_file, destination_file)
            print(f"Đã copy: {source_file} -> {destination_file}")

# Đếm số file sau khi copy
destination_file_count_after = count_step_files(destination_folder)

print(f"Số lượng file .step và .stp trong thư mục nguồn: {source_file_count}")
print(f"Số lượng file trong thư mục đích trước khi copy: {destination_file_count_before}")
print(f"Số lượng file trong thư mục đích sau khi copy: {destination_file_count_after}")
