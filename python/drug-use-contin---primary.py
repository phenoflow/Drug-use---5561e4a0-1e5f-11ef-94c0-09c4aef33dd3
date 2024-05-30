# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"E2461","system":"readv2"},{"code":"E2401","system":"readv2"},{"code":"E2561","system":"readv2"},{"code":"E25y1","system":"readv2"},{"code":"E2451","system":"readv2"},{"code":"E2411","system":"readv2"},{"code":"E2591","system":"readv2"},{"code":"13cC.","system":"readv2"},{"code":"E2421","system":"readv2"},{"code":"E2441","system":"readv2"},{"code":"E2551","system":"readv2"},{"code":"E2471","system":"readv2"},{"code":"E2571","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-contin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-contin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-contin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
