class NetworkMessage:
    def __init__(self, buffer_reader, len_type, length, count=None):
        self.buffer_reader = buffer_reader
        self.len_type = len_type
        self.length = length
        self.count = count

    def populate(self):
        for key, var in enumerate(self.vars):
            try:
                self.vars[key]["value"] = self.buffer_reader.read_value(var)
                # print("Read: %s => %s" % (self.vars[key]["name"], self.vars[key]["value"]))
            except AttributeError:
                print("Don't know how to read %s" % var["type"])

    def get_message_size(self):
        return 2 + self.len_type + self.length + (0 if self.count is None else 4)

    def __repr__(self):
        return "{0} : {1} => {2}\n{3}".format(
            self.id,
            type(self).__name__,
            self.length,
            [{key: self.__dict__[key]} for x, key in enumerate(self.__dict__) if
             key not in ['buffer_reader', 'len_type', 'length', 'count', 'id']]
       )

    def deserialize(self):
        print("Not implemented yet for {0} => {1}".format(self.id, type(self).__name__))

    def serialize(self):
        print("Not implemented yet for {0} => {1}".format(self.id, type(self).__name__))