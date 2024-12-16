from tabula import read_pdf

def extract_tables_by_page(pdf_path, output_csv_path, start_page, end_page):
    """
    Extract tables from a PDF file page by page and save them as CSV files.

    Parameters:
        pdf_path (str): Path to the PDF file.
        output_csv_path (str): Base path for saving extracted tables.
        start_page (int): Starting page number.
        end_page (int): Ending page number.
    """
    for page in range(start_page, end_page + 1):
        print(f"Processing page {page}...")
        try:
            tables = read_pdf(pdf_path, pages=str(page), multiple_tables=True, lattice=True)
            if tables:
                for idx, table in enumerate(tables):
                    output_path = f"{output_csv_path}_page_{page}_table_{idx + 1}.csv"
                    table.to_csv(output_path, index=False)
                    print(f"Table {idx + 1} from page {page} saved to {output_path}")
            else:
                print(f"No tables found on page {page}.")
        except Exception as e:
            print(f"Error processing page {page}: {e}")

    print("Table extraction completed.")

# Run table extraction
pdf_file_path = "NetSol_Financial Statement_2024_Part 1.pdf"  # Update with your PDF path
extract_tables_by_page(pdf_file_path, "netsol_financial_tables", 1, 136)
