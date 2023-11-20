import os
import fitz  # PyMuPDF
import pandas as pd
from modeling.structured_analysis import analyze_structured_data
from modeling.unstructured_analysis import analyze_unstructured_data

def structured_scrap(pdf_path):
    # Convert Windows path separators to Unix if needed
    pdf_path = os.path.normpath(pdf_path)

    doc = fitz.open(pdf_path)
    num_pages = doc.page_count

    # Initialize an empty DataFrame to store the extracted data
    extracted_data = pd.DataFrame()

    for page_num in range(num_pages):
        page = doc[page_num]
        text_content = page.get_text()

        # Assuming the tabular data is separated by newline and tab characters
        rows = [row.split('\t') for row in text_content.split('\n') if row]

        # Determine the number of columns dynamically
        num_columns = max(len(row) for row in rows)

        # Extracted data is added to the DataFrame
        page_data = pd.DataFrame(rows, columns=[f'Column{i}' for i in range(1, num_columns + 1)])
        extracted_data = pd.concat([extracted_data, page_data], ignore_index=True)

    doc.close()

    return clean_and_format_data(extracted_data)

def analyze_structured(pdf_path, continuous_columns=None, categorical_column=None):
    cleaned_data = structured_scrap(pdf_path)
    return analyze_structured_data(cleaned_data, continuous_columns=continuous_columns, categorical_column=categorical_column)

def analyze_unstructured(pdf_path):
    unstructured_text = extract_unstructured_text(pdf_path)
    return analyze_unstructured_data(unstructured_text)

def clean_and_format_data(raw_data):
    # Placeholder function for cleaning and formatting data
    # Implement your logic to clean and format the raw_data
    # This can include handling missing values, converting data types, etc.

    # Replace empty strings with NaN
    cleaned_data = raw_data.applymap(lambda x: None if x == '' else x)

    # Convert all columns to float, ignoring non-numeric values
    cleaned_data = cleaned_data.apply(pd.to_numeric, errors='ignore')

    return cleaned_data

def extract_unstructured_text(pdf_path):
 # Assuming the extracted data is already in string format
    # Replace this with your actual logic for extracting unstructured text from the PDF
    extracted_data = unstructured_scrap(pdf_path)
 
    return extracted_data




def unstructured_scrap(pdf_path):
# Convert Windows path separators to Unix if needed
    pdf_path = os.path.normpath(pdf_path)

    doc = fitz.open(pdf_path)
    num_pages = doc.page_count

    # Initialize an empty string to store the extracted text
    extracted_text = ""

    for page_num in range(num_pages):
        page = doc[page_num]
        text_content = page.get_text()

        # Append the text content to the extracted_text string
        extracted_text += text_content + " "

    doc.close()

    return extracted_text


