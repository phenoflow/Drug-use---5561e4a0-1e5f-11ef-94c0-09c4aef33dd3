# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"1V3..","system":"readv2"},{"code":"13cQ.","system":"readv2"},{"code":"1V...","system":"readv2"},{"code":"1V6..","system":"readv2"},{"code":"F116","system":"readv2"},{"code":"F186","system":"readv2"},{"code":"F189","system":"readv2"},{"code":"F151","system":"readv2"},{"code":"F181","system":"readv2"},{"code":"F129","system":"readv2"},{"code":"F18","system":"readv2"},{"code":"F115","system":"readv2"},{"code":"F158","system":"readv2"},{"code":"F167","system":"readv2"},{"code":"F165","system":"readv2"},{"code":"F125","system":"readv2"},{"code":"F12","system":"readv2"},{"code":"F164","system":"readv2"},{"code":"F150","system":"readv2"},{"code":"F132","system":"readv2"},{"code":"F183","system":"readv2"},{"code":"F138","system":"readv2"},{"code":"F153","system":"readv2"},{"code":"F154","system":"readv2"},{"code":"F13","system":"readv2"},{"code":"F119","system":"readv2"},{"code":"F11","system":"readv2"},{"code":"F139","system":"readv2"},{"code":"F114","system":"readv2"},{"code":"F134","system":"readv2"},{"code":"F123","system":"readv2"},{"code":"F135","system":"readv2"},{"code":"F187","system":"readv2"},{"code":"F184","system":"readv2"},{"code":"F162","system":"readv2"},{"code":"F168","system":"readv2"},{"code":"F16","system":"readv2"},{"code":"F185","system":"readv2"},{"code":"F188","system":"readv2"},{"code":"F126","system":"readv2"},{"code":"F130","system":"readv2"},{"code":"F113","system":"readv2"},{"code":"F120","system":"readv2"},{"code":"F182","system":"readv2"},{"code":"F159","system":"readv2"},{"code":"F117","system":"readv2"},{"code":"F163","system":"readv2"},{"code":"F111","system":"readv2"},{"code":"F137","system":"readv2"},{"code":"F160","system":"readv2"},{"code":"F118","system":"readv2"},{"code":"F152","system":"readv2"},{"code":"F161","system":"readv2"},{"code":"F128","system":"readv2"},{"code":"F127","system":"readv2"},{"code":"F166","system":"readv2"},{"code":"F155","system":"readv2"},{"code":"F124","system":"readv2"},{"code":"F112","system":"readv2"},{"code":"F169","system":"readv2"},{"code":"F156","system":"readv2"},{"code":"F131","system":"readv2"},{"code":"F133","system":"readv2"},{"code":"F15","system":"readv2"},{"code":"F136","system":"readv2"},{"code":"F121","system":"readv2"},{"code":"F122","system":"readv2"},{"code":"F110","system":"readv2"},{"code":"F157","system":"readv2"},{"code":"F180","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drug-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drug-use-behaviour---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drug-use-behaviour---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drug-use-behaviour---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
