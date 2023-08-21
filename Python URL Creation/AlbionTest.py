import csv

MAX_TOTAL_LENGTH = 4096

def process_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.readlines()

        # Process the content and create a list of lists for CSV
        processed_rows = []
        current_row = []

        for line in content:
            # Example: Splitting the line into items and adding commas
            items = line.strip().split('\t')  # Replace '\t' with your delimiter
            items_with_commas = [item + "," for item in items]

            # Calculate the length of the data set with the URL prefix and suffix
            data_set_length = (
                sum(len(item) for item in items_with_commas) +
                len("https://west.albion-online-data.com/api/v1/stats/prices/") +
                len(".json?locations=4,7,8,301,1002,1006,1012,1301,2002,2004,2301,3002,3003,3005,3008,3301,4002,4006,4300,4301&qualities=1,2,3,4,5")
            )

            if sum(len(item) for item in current_row) + data_set_length <= MAX_TOTAL_LENGTH:
                current_row.extend(items_with_commas)
            else:
                processed_rows.append(''.join(current_row))
                current_row = items_with_commas

        # Add the last data set
        if current_row:
            processed_rows.append(''.join(current_row))

        with open(output_file_path, 'w', newline='') as output_file:
            for row in processed_rows:
                url_prefix = "https://west.albion-online-data.com/api/v1/stats/prices/"
                url_suffix = ".json?locations=4,7,8,301,1002,1006,1012,1301,2002,2004,2301,3002,3003,3005,3008,3301,4002,4006,4300,4301&qualities=1,2,3,4,5"
                full_row = f"{url_prefix}{row}{url_suffix}"
                output_file.write(full_row + '\n')

        print(f"Processed content written to {output_file_path} in CSV format")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_path = "Data.txt"      # Provide the path to your input file
    output_path = "Finished.txt"    # Provide the desired path for the output CSV file
    process_file(input_path, output_path)
