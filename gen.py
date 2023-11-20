import os

def create_project_structure():
    # Create the main project folder
    project_folder = "data_science_project"
    os.makedirs(project_folder, exist_ok=True)
    
    # List of subfolders
    folders = [
        "data_scraping_pdf",
        "data_scraping_website",
        "data_analysis_csv_excel_txt_json",
        "machine_learning_task"
    ]

    # Create subfolders inside the main project folder
    for folder in folders:
        folder_path = os.path.join(project_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Create sample files inside each subfolder
        create_sample_files(folder_path)

def create_sample_files(folder_path):
    # You can customize this function based on your specific needs
    sample_file_names = ["data.txt"]

    for file_name in sample_file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as file:
            # Writing some sample content to the files
            file.write("Sample data for {}".format(file_name))

if __name__ == "__main__":
    create_project_structure()
