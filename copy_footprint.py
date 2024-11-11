import os
import shutil

# Source and destination folder paths
source_folder = r"D:\Allegro\Project\CanhMai\Lib\Schematic_And_FootPrint"
destination_folder = r"C:\Cadence\SPB_17.4\share\pcb\pcb_lib\symbols"

# Function to count the number of files with specific extensions
def count_files(folder, extensions):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                count += 1
    return count

# Count the number of files before copying
extensions = ('.pad', '.psm', '.dra', '.ssm')
source_file_count = count_files(source_folder, extensions)
destination_file_count_before = count_files(destination_folder, extensions)

print(f"Number of valid files in the source folder: {source_file_count}")
print(f"Number of valid files in the destination folder before copying: {destination_file_count_before}")

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Traverse all subfolders and files in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Check if the file has an extension of .PAD, .psm, .pad, or .DRA
        if file.lower().endswith(extensions):
            # Full path of the source file
            source_file = os.path.join(root, file)
            # Full path of the destination file
            destination_file = os.path.join(destination_folder, file)
            
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")

# Count the number of files after copying
destination_file_count_after = count_files(destination_folder, extensions)

print(f"Number of valid files in the destination folder after copying: {destination_file_count_after}")
print("File copying completed.")
