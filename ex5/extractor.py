import sys
import re
import json

#open a given file
with open(sys.argv[1], "r", encoding="utf-8") as f: #実行するときにpython extractor.py "sample.html"のようにファイル名を""で囲むこと
    str1 = f.read()
    
#get author name
dic1 = {}
reg1 = "<h1 .*" + ">" + "([^>]*)" + "</h1>"
match1 = re.search(reg1, str1)
dic1["author"] = match1.group(1)

#get text
str2 = re.sub("<br>", "\n", str1)
list1 = re.findall("</p>", str2)
str_text = ""

for i in range(len(list1)):
    i += 1
    str_i = str(i)
    reg2 = "<p pno=" + str_i + ">" + "([^>]*\n)" + "</p>"
    match2 = re.search(reg2, str2)
    str_match = match2.group(1)
    str_text += str_match

dic1["text"] = str_text
print(dic1)

#dump dic1
with open("out.json", "w", encoding="utf-8") as f2:
    json.dump(dic1, f2)