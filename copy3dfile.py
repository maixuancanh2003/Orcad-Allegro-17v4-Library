import os

# Source and destination folder paths
source_folder = r"D:\Allegro\Project\CanhMai\Lib\Schematic_And_FootPrint"
destination_folder = r"C:\Cadence\SPB_17.4\share\local\pcb\step"

# Function to count the number of .step and .stp files in a folder
def count_step_files(folder_path):
    return sum(
        1 for root, dirs, files in os.walk(folder_path) for file in files if file.lower().endswith(('.step', '.stp'))
    )

# Count the number of files before copying
source_file_count = count_step_files(source_folder)
destination_file_count_before = count_step_files(destination_folder)

# Perform file copy as per requirements
import shutil
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith(('.step', '.stp')):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")

# Count the number of files after copying
destination_file_count_after = count_step_files(destination_folder)

print(f"Number of .step and .stp files in the source folder: {source_file_count}")
print(f"Number of files in the destination folder before copying: {destination_file_count_before}")
print(f"Number of files in the destination folder after copying: {destination_file_count_after}")
