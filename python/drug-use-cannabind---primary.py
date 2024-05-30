# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"E2431","system":"readv2"},{"code":"E2430","system":"readv2"},{"code":"Eu126","system":"readv2"},{"code":"Eu125","system":"readv2"},{"code":"1T80.","system":"readv2"},{"code":"T8410","system":"readv2"},{"code":"1T81.","system":"readv2"},{"code":"E2521","system":"readv2"},{"code":"E243.","system":"readv2"},{"code":"E252z","system":"readv2"},{"code":"Eu127","system":"readv2"},{"code":"Eu122","system":"readv2"},{"code":"1T8..","system":"readv2"},{"code":"13cE.","system":"readv2"},{"code":"E252.","system":"readv2"},{"code":"E2523","system":"readv2"},{"code":"Eu124","system":"readv2"},{"code":"1T82.","system":"readv2"},{"code":"E2520","system":"readv2"},{"code":"Eu121","system":"readv2"},{"code":"E2433","system":"readv2"},{"code":"E243z","system":"readv2"},{"code":"E2522","system":"readv2"},{"code":"Eu120","system":"readv2"},{"code":"Eu12z","system":"readv2"},{"code":"Eu123","system":"readv2"},{"code":"Eu12y","system":"readv2"},{"code":"1T83.","system":"readv2"},{"code":"SL960","system":"readv2"},{"code":"E2432","system":"readv2"},{"code":"T407","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-cannabind---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-cannabind---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-cannabind---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
