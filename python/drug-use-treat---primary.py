# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"8HHd.","system":"readv2"},{"code":"9HC6.","system":"readv2"},{"code":"9HC4.","system":"readv2"},{"code":"9HC5.","system":"readv2"},{"code":"9NX2.","system":"readv2"},{"code":"9HC7.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-treat---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-treat---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-treat---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
