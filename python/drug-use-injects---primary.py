# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"djcw.","system":"readv2"},{"code":"1V30.","system":"readv2"},{"code":"1V34.","system":"readv2"},{"code":"djcH.","system":"readv2"},{"code":"1V37.","system":"readv2"},{"code":"djct.","system":"readv2"},{"code":"1V31.","system":"readv2"},{"code":"djcv.","system":"readv2"},{"code":"djcu.","system":"readv2"},{"code":"djcz.","system":"readv2"},{"code":"djcx.","system":"readv2"},{"code":"1V38.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-injects---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-injects---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-injects---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
