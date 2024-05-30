# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"U1A63","system":"readv2"},{"code":"SL96z","system":"readv2"},{"code":"SL96.","system":"readv2"},{"code":"U1A50","system":"readv2"},{"code":"U2064","system":"readv2"},{"code":"SL50z","system":"readv2"},{"code":"U1A55","system":"readv2"},{"code":"U205y","system":"readv2"},{"code":"U206y","system":"readv2"},{"code":"U2060","system":"readv2"},{"code":"U1A60","system":"readv2"},{"code":"U2065","system":"readv2"},{"code":"U2057","system":"readv2"},{"code":"U1A53","system":"readv2"},{"code":"U1A67","system":"readv2"},{"code":"U406.","system":"readv2"},{"code":"U1A5y","system":"readv2"},{"code":"U2054","system":"readv2"},{"code":"U205.","system":"readv2"},{"code":"SL501","system":"readv2"},{"code":"U2055","system":"readv2"},{"code":"SyuFB","system":"readv2"},{"code":"SyuFC","system":"readv2"},{"code":"U1A64","system":"readv2"},{"code":"SL50.","system":"readv2"},{"code":"U2067","system":"readv2"},{"code":"U1A6y","system":"readv2"},{"code":"U2053","system":"readv2"},{"code":"SL972","system":"readv2"},{"code":"U4050","system":"readv2"},{"code":"U2063","system":"readv2"},{"code":"U1A6.","system":"readv2"},{"code":"U1A57","system":"readv2"},{"code":"SL970","system":"readv2"},{"code":"U4060","system":"readv2"},{"code":"U1A54","system":"readv2"},{"code":"U1A65","system":"readv2"},{"code":"U1A5.","system":"readv2"},{"code":"U405.","system":"readv2"},{"code":"SL502","system":"readv2"},{"code":"U2050","system":"readv2"},{"code":"Y12","system":"readv2"},{"code":"Y129","system":"readv2"},{"code":"X622","system":"readv2"},{"code":"Y121","system":"readv2"},{"code":"X629","system":"readv2"},{"code":"X625","system":"readv2"},{"code":"X428","system":"readv2"},{"code":"Y128","system":"readv2"},{"code":"X42","system":"readv2"},{"code":"X424","system":"readv2"},{"code":"X621","system":"readv2"},{"code":"T403","system":"readv2"},{"code":"Y125","system":"readv2"},{"code":"X426","system":"readv2"},{"code":"X628","system":"readv2"},{"code":"Y123","system":"readv2"},{"code":"Y122","system":"readv2"},{"code":"X427","system":"readv2"},{"code":"Y126","system":"readv2"},{"code":"X620","system":"readv2"},{"code":"X62","system":"readv2"},{"code":"X627","system":"readv2"},{"code":"T401","system":"readv2"},{"code":"Y120","system":"readv2"},{"code":"X422","system":"readv2"},{"code":"X624","system":"readv2"},{"code":"X425","system":"readv2"},{"code":"X429","system":"readv2"},{"code":"Y124","system":"readv2"},{"code":"Y127","system":"readv2"},{"code":"X626","system":"readv2"},{"code":"X423","system":"readv2"},{"code":"T404","system":"readv2"},{"code":"X421","system":"readv2"},{"code":"X623","system":"readv2"},{"code":"X420","system":"readv2"},{"code":"T402","system":"readv2"},{"code":"T40","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-poison---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-poison---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-poison---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
