# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"13c4.","system":"readv2"},{"code":"13cN.","system":"readv2"},{"code":"E02y2","system":"readv2"},{"code":"1V1..","system":"readv2"},{"code":"E02y1","system":"readv2"},{"code":"8BAt.","system":"readv2"},{"code":"9NN1.","system":"readv2"},{"code":"13c1.","system":"readv2"},{"code":"1V06.","system":"readv2"},{"code":"1V64.","system":"readv2"},{"code":"13c3.","system":"readv2"},{"code":"146E.","system":"readv2"},{"code":"13c9.","system":"readv2"},{"code":"1V00.","system":"readv2"},{"code":"djcD.","system":"readv2"},{"code":"E02z.","system":"readv2"},{"code":"9HC9.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
