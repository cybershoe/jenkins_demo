import os
import glob
from subprocess import check_output

bigipaddr = "10.1.1.4"

p = check_output(["git", "log", "--name-status", "-1"])

print("List of services to Add/Modify/Remove")
for line in p.splitlines():
    parse = line.split("\t")
    if len(parse) >= 2:
        if parse[1].endswith(".json.deploy"):
            print(parse)

for line in p.splitlines():
    if len(parse) >= 2:
        if parse[1].endswith(".json.deploy"):
            if parse[0] == "M":
                os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + parse[1])
            elif parse[0] == "A":
                os.system("./scripts/deploy_iapp_bigip.py " + bigipaddr + " " + parse[1])
            elif parse[0] == "D":
                os.system("./scripts/delete_iapp_bigip.py " + bigipaddr + " " + "-n" + " " + parse[1].split(".")[0])