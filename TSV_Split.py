import csv

def separate_column(input_file, column_index, output_file, row_limit=None, ignore_first_row=False, stop_value=None):
    with open(input_file, 'r', newline='') as f_input, open(output_file, 'w', newline='') as f_output:
        reader = csv.reader(f_input, delimiter='\t')
        
        # Skip the first row if ignore_first_row is True
        if ignore_first_row:
            next(reader)
            
        rows_processed = 0
        for row in reader:
            # Stop processing after row_limit rows
            if row_limit and rows_processed >= row_limit:
                break
            
            column_value = row[column_index].rstrip('\r\n')

            if stop_value is not None and float(row[1]) < stop_value:
                print(f"Stopping program because column 1 exceeds {stop_value}")
                return
                
            if rows_processed == 0:
                f_output.write(column_value)
            else:
                f_output.write(' ' + column_value)
                
            rows_processed += 1
            print(rows_processed, row[1])
            
def separate_rows(input_file, column_index, output_file, row_limit=None, ignore_first_row=False, stop_value=None):
    with open(input_file, 'r', newline='') as f_input, open(output_file, 'w', newline='') as f_output:
        reader = csv.reader(f_input, delimiter='\t')
        
        # Skip the first row if ignore_first_row is True
        if ignore_first_row:
            next(reader)
            
        rows_processed = 0
        for row in reader:
            # Stop processing after row_limit rows
            if row_limit and rows_processed >= row_limit:
                break
            
            column_value = row[column_index].rstrip('\r\n')

            if stop_value is not None and float(row[1]) < stop_value:
                print(f"Stopping program because column 1 exceeds {stop_value}")
                return
                
            f_output.write(column_value + "\n")
                
            rows_processed += 1
            print(rows_processed, row[1])
            
            
input_file = "bitcoin_addresses_and_balance_LATEST.tsv"

output_file = "wallets.txt"
column_index = 0
row_limit = 50000000
ignore_first_row = True
stop_value = 2000000

separate_rows(input_file, column_index, output_file, row_limit, ignore_first_row, stop_value)
#separate_rows(input_file, column_index, output_file, row_limit, ignore_first_row)

