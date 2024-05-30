# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"Eu1A7","system":"readv2"},{"code":"1TG..","system":"readv2"},{"code":"Eu1..","system":"readv2"},{"code":"F19","system":"readv2"},{"code":"F194","system":"readv2"},{"code":"F199","system":"readv2"},{"code":"F195","system":"readv2"},{"code":"F191","system":"readv2"},{"code":"F197","system":"readv2"},{"code":"F192","system":"readv2"},{"code":"F193","system":"readv2"},{"code":"F190","system":"readv2"},{"code":"F196","system":"readv2"},{"code":"F198","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-psychoact---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-psychoact---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-psychoact---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
