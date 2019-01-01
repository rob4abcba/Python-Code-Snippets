import csv #RL For comparison, see how read, write, parse a non-CSV file in other video.
#RL csv module handles if someone puts a comma in their name and handles newlines.

with open('names.csv', 'r') as csv_file: #RL Context manager. Open CSV file in same directory as this .py file.  #RL We choose the to call this file "csv_file"
    csv_reader = csv.DictReader(csv_file) #RL We choose to call this variable/object "csv_reader".  Use csv.DictReader method.

    #next(csv_reader) #If want to loop over the 1st line of names.csv since it's just the header fields.

    with open('new_names.csv', 'w') as new_file: # 5:45 This time 'w' for write mode. Variable 'new_file'
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t') # 5:50 Choose variable name 'csv_writer'. Use DictWriter method of the CSV module. 

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
