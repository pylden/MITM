path = "./ressources/AS/scripts/com/ankamagames/dofus/network/messages"
filelist = []
f = open("./example.py", "r")
file_example = f.read()
f.close()
for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root, file))
for name in filelist:
    with open(name, "r") as f:
        read = f.read()
        id = re.findall("protocolId:uint = ([0-9]+)", read)[0]
        if (id):
            classname = re.findall(r"public class (\S+)", read)[0]
            vars = re.findall(r"public var (\S+):(\S+) = \"\";", read)
            write_class = file_example.replace("classname", classname).replace("idMessage", id)
            for var in vars:
                write_class += "        self.%s = {\"type\": \"%s\", \"value\": \"\"}\n" % (var[0], var[1])
            if vars:
                print(classname)
            wc = open("./module/protocol/network/messages/%s.py" % classname, 'w')
            wc.write(write_class)
            wc.close