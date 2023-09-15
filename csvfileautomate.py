import os
import re
import csv

def search_files(root_dir, pattern):
    matching_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:  # Open in binary mode
                    content = f.read()
                    try:
                        decoded_content = content.decode('utf-8')
                        if re.search(pattern, decoded_content):
                            matching_files.append(file_path)
                    except UnicodeDecodeError:
                        pass  
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return matching_files

def generate_csv(report_filename, matching_files, pattern):
    with open(report_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Pattern Search Report', pattern])
        csv_writer.writerow(['File Paths'])
        csv_writer.writerow([])  # Empty row

        for file_path in matching_files:
            csv_writer.writerow([file_path])

if __name__ == "__main__":
    folder_path = input("Enter the folder path to search in: ")
    search_pattern = input("Enter the pattern to search for: ")
    report_filename = "search_report.csv"

    if os.path.exists(folder_path):
        matching_files = search_files(folder_path, search_pattern)

        if matching_files:
            generate_csv(report_filename, matching_files, search_pattern)
            print(f"Search report generated: {report_filename}")
        else:
            print("No matching files found.")
    else:
        print("Folder not found.")
