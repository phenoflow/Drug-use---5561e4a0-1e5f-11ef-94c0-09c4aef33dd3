# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"T8520","system":"readv2"},{"code":"1T63.","system":"readv2"},{"code":"1T50.","system":"readv2"},{"code":"E2563","system":"readv2"},{"code":"1T61.","system":"readv2"},{"code":"Eu141","system":"readv2"},{"code":"Eu1A1","system":"readv2"},{"code":"R10B0","system":"readv2"},{"code":"1T5..","system":"readv2"},{"code":"1T53.","system":"readv2"},{"code":"1T6..","system":"readv2"},{"code":"1T60.","system":"readv2"},{"code":"SL850","system":"readv2"},{"code":"1T51.","system":"readv2"},{"code":"Eu147","system":"readv2"},{"code":"F14","system":"readv2"},{"code":"F144","system":"readv2"},{"code":"F140","system":"readv2"},{"code":"F143","system":"readv2"},{"code":"F148","system":"readv2"},{"code":"F147","system":"readv2"},{"code":"F142","system":"readv2"},{"code":"F141","system":"readv2"},{"code":"T405","system":"readv2"},{"code":"R782","system":"readv2"},{"code":"F145","system":"readv2"},{"code":"F146","system":"readv2"},{"code":"F149","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-cocain---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-cocain---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-cocain---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
