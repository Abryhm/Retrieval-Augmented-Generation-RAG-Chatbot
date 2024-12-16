import os
import json
import pandas as pd

def combine_data(json_path, csv_folder, output_json):
    """
    Combines JSON data and CSV tables into a single JSON file.

    Parameters:
        json_path (str): Path to the JSON file containing textual content.
        csv_folder (str): Path to the folder containing CSV files.
        output_json (str): Path for the output combined JSON file.
    """
    # Load JSON data
    try:
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)
        print(f"Loaded JSON data from {json_path}")
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return

    # Process all CSV files in the folder
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]
    tables = []
    if not csv_files:
        print(f"No CSV files found in {csv_folder}.")
    else:
        for csv_file in csv_files:
            try:
                table_path = os.path.join(csv_folder, csv_file)
                table = pd.read_csv(table_path)
                tables.append({"table_name": csv_file, "table_data": table.to_dict(orient="records")})
                print(f"Loaded table from {csv_file}")
            except Exception as e:
                print(f"Error loading CSV file {csv_file}: {e}")

    # Combine JSON data and tabular content
    combined_data = {
        "textual_content": json_data,
        "tabular_content": tables,
    }

    # Save the combined data to the output JSON file
    try:
        with open(output_json, "w") as output_file:
            json.dump(combined_data, output_file, indent=4)
        print(f"Combined data saved to {output_json}")
    except Exception as e:
        print(f"Error saving combined data: {e}")

# Example usage
combine_data("structured_data.json", "netsol_financial_tables", "final_data.json")
