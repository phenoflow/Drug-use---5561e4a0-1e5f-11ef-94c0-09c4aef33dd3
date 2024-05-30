# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"Eu18z","system":"readv2"},{"code":"Eu13z","system":"readv2"},{"code":"Eu14z","system":"readv2"},{"code":"Eu16z","system":"readv2"},{"code":"8H7x.","system":"readv2"},{"code":"ZV6D7","system":"readv2"},{"code":"Eu15z","system":"readv2"},{"code":"677T.","system":"readv2"},{"code":"Eu11z","system":"readv2"},{"code":"Z715","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-counsel---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-counsel---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-counsel---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
