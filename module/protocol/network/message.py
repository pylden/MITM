class Message:
    def __init__(self, buffer_reader, len_type, length):
        self.buffer_reader = buffer_reader
        self.len_type = len_type
        self.length = length

    def parse_content(self):
        pass

    def get_message_size(self):
        return 2 + self.len_type + self.length

    def __repr__(self):
        return "{0} : {1}".format(self.id, type(self).__name__)