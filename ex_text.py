from unstructured.partition.pdf import partition_pdf
import json

# Define the file path to your PDF
pdf_file_path = "NetSol_Financial Statement_2024_Part 1.pdf"

# Process the PDF
def process_pdf(pdf_path):
    # Extract elements (text, tables, etc.) from the PDF
    elements = partition_pdf(filename=pdf_path)

    structured_data = []
    for element in elements:
        if hasattr(element, 'text'):
            structured_data.append({
                "type": element.__class__.__name__,
                "content": element.text,
            })
        else:
            structured_data.append({
                "type": element.__class__.__name__,
                "content": "Non-text element (e.g., image, table)",
            })

    return structured_data

# Extract and save data
extracted_data = process_pdf(pdf_file_path)

# Save as JSON
with open("structured_data.json", "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print("Extraction complete. Data saved to structured_data.json.")