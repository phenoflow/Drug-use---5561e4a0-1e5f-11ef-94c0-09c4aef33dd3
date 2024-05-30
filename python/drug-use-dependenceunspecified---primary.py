# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"L1830","system":"readv2"},{"code":"E2481","system":"readv2"},{"code":"E245.","system":"readv2"},{"code":"Eu152","system":"readv2"},{"code":"L2550","system":"readv2"},{"code":"E249z","system":"readv2"},{"code":"Eu1A2","system":"readv2"},{"code":"E244z","system":"readv2"},{"code":"U206z","system":"readv2"},{"code":"Eu162","system":"readv2"},{"code":"E2490","system":"readv2"},{"code":"E2493","system":"readv2"},{"code":"E2402","system":"readv2"},{"code":"E2470","system":"readv2"},{"code":"E2491","system":"readv2"},{"code":"E247z","system":"readv2"},{"code":"8BAX.","system":"readv2"},{"code":"U205z","system":"readv2"},{"code":"Eu132","system":"readv2"},{"code":"E240.","system":"readv2"},{"code":"E245z","system":"readv2"},{"code":"E242z","system":"readv2"},{"code":"E246.","system":"readv2"},{"code":"E248z","system":"readv2"},{"code":"L1834","system":"readv2"},{"code":"E2483","system":"readv2"},{"code":"E2550","system":"readv2"},{"code":"E2423","system":"readv2"},{"code":"E248.","system":"readv2"},{"code":"E2482","system":"readv2"},{"code":"E2400","system":"readv2"},{"code":"L183.","system":"readv2"},{"code":"Eu192","system":"readv2"},{"code":"E2492","system":"readv2"},{"code":"E24..","system":"readv2"},{"code":"SyuFD","system":"readv2"},{"code":"L183z","system":"readv2"},{"code":"Eu112","system":"readv2"},{"code":"E2420","system":"readv2"},{"code":"E240z","system":"readv2"},{"code":"8BAd.","system":"readv2"},{"code":"Eu182","system":"readv2"},{"code":"E242.","system":"readv2"},{"code":"E2480","system":"readv2"},{"code":"E241.","system":"readv2"},{"code":"U1A5z","system":"readv2"},{"code":"Eu142","system":"readv2"},{"code":"8HHL.","system":"readv2"},{"code":"8I2N.","system":"readv2"},{"code":"E2570","system":"readv2"},{"code":"U1A6z","system":"readv2"},{"code":"SL500","system":"readv2"},{"code":"E24A.","system":"readv2"},{"code":"8BA9.","system":"readv2"},{"code":"E2460","system":"readv2"},{"code":"E246z","system":"readv2"},{"code":"E2560","system":"readv2"},{"code":"E247.","system":"readv2"},{"code":"E24z.","system":"readv2"},{"code":"E249.","system":"readv2"},{"code":"T409","system":"readv2"},{"code":"T406","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-dependenceunspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-dependenceunspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-dependenceunspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
