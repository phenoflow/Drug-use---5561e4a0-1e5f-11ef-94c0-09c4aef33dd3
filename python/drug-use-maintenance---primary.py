# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"U4056","system":"readv2"},{"code":"U4061","system":"readv2"},{"code":"U4054","system":"readv2"},{"code":"U4062","system":"readv2"},{"code":"U4064","system":"readv2"},{"code":"8B231","system":"readv2"},{"code":"U406y","system":"readv2"},{"code":"U4063","system":"readv2"},{"code":"8BE0.","system":"readv2"},{"code":"U4057","system":"readv2"},{"code":"U206.","system":"readv2"},{"code":"U4052","system":"readv2"},{"code":"U4051","system":"readv2"},{"code":"8BE..","system":"readv2"},{"code":"8B230","system":"readv2"},{"code":"8B2Q.","system":"readv2"},{"code":"U4067","system":"readv2"},{"code":"8BE1.","system":"readv2"},{"code":"U405z","system":"readv2"},{"code":"U4053","system":"readv2"},{"code":"U4065","system":"readv2"},{"code":"8B2M.","system":"readv2"},{"code":"U406z","system":"readv2"},{"code":"U4055","system":"readv2"},{"code":"U405y","system":"readv2"},{"code":"U4066","system":"readv2"},{"code":"8B2P.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-maintenance---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-maintenance---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-maintenance---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
