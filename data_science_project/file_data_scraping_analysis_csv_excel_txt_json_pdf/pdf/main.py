# main.py
from pdf_analysis import pdf_scraping_and_analysis

if __name__ == "__main__":
    # Example usage
    pdf_path = "data_science_project/data_scraping_pdf/sample.pdf"
    result = pdf_scraping_and_analysis(pdf_path)
    print("\nAnalysis Result:")
    print(result)
