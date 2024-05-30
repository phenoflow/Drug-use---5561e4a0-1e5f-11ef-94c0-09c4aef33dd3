# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"U2062","system":"readv2"},{"code":"U2061","system":"readv2"},{"code":"U2052","system":"readv2"},{"code":"1V3K.","system":"readv2"},{"code":"U2051","system":"readv2"},{"code":"U1A52","system":"readv2"},{"code":"U1A51","system":"readv2"},{"code":"U1A62","system":"readv2"},{"code":"1V3H.","system":"readv2"},{"code":"U1A61","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-obtains---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-obtains---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-obtains---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
