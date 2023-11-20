import sys
import os

# Add the full path to the directory containing your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "modeling")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import your modules
from unstructured_analysis import analyze_unstructured_data  # Import the unstructured analysis module
from modeling.structured_analysis import analyze_structured_data  # Import the structured analysis module
from modeling.unstructured_analysis import analyze_unstructured_data  # Import the unstructured analysis module
from pdf_analysis import structured_scrap
## from modeling.statistics import some_statistics_function  # Import other modules as needed

from pdf_analysis import unstructured_scrap


def save_results_to_text_file(results, output_folder):
    # Create or open a text file in the specified output folder
    output_file_path = os.path.join(output_folder, "analysis_results.txt")
    
    with open(output_file_path, 'w') as file:
        # Write the results to the file
        file.write("Analysis Result:\n")
        file.write(str(results))

    print(f"Results saved to: {output_file_path}")


def normalize_path(path):
    # Convert Windows path separators to Unix if needed
    return os.path.normpath(path)

if __name__ == "__main__":
    # Example usage
    input_str ="C:\\Users\\grub\\Documents\\ALEKI\\My Gits - Local\\Data Science - Project Using various formtas\\data_science_project\\sample_data\\dangers-of-vaping.pdf"
    pdf_path = normalize_path(input_str)
    raw = unstructured_scrap(pdf_path)
     
    # Specify the folder where you want to save the results
    output_folder = normalize_path("results")
    os.makedirs(output_folder, exist_ok=True)
 

    # Example usage of unstructured analysis
    unstructured_data = "This is some unstructured text data."
    unstructured_result = analyze_unstructured_data(raw)
    print("\nUnstructured Analysis Result:")
    print(unstructured_result)

       
    save_results_to_text_file(unstructured_result, output_folder)
    print("\nAnalysis Result:")
 