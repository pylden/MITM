import os
import re
from collections import OrderedDict


path = "./ressources/AS/scripts/com/ankamagames/dofus/network/messages"
filelist = []
f = open("./example.py", "r")
file_example = f.read()
f.close()
dicto = {}
listt = []
datatypes = {}
extends = {}

for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root, file))
for name in filelist:
    with open(name, "r") as f:
        read = f.read()
        id = re.findall("protocolId:uint = ([0-9]+)", read)[0]
        if (id):
            classname = re.findall(r"public class (\S+)", read)[0]
            listt.append(classname)
            dicto[int(id)] = classname
            vars = re.findall(r"public var (\S+):(\S+)[ |;]", read)
            write_class = file_example.replace("IDMESSAGE", id).replace("CLASSNAME", classname)
            for var in vars:
                write_class += "        self.%s = {\"type\": \"%s\", \"value\": \"\"}\n" % (var[0], var[1])
                datatypes[var[1]] = ""

            extends = re.findall(r"extends (\S+)", read)
            implements = re.findall(r"implements (.*)\n", read)[0].split(', ')
            if len(implements) > 1:

                print(name)
                print(implements)
            # wc = open("./module/protocol/network/messages/%s.py" % classname, 'w')
            # wc.write(write_class)
            # wc.close
# dicto = dict(OrderedDict(sorted(dicto.items(), key=lambda t: t[0])))
# print(dicto)
# for key, val in enumerate(dicto.items()):
#     print("%d: %s.%s, " % (val[0], val[1], val[1]))
#
#print(str(sorted(listt))[1:-1])