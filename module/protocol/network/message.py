class Message:
    def __init__(self, id, len_type, length, content):
        self.id = id
        self.len_type = len_type
        self.len = length
        self.content = content

    def __repr__(self):
        return "Id: {0}\nLength Type: {1}\nLength: {2}\nContent: {3}".format(
            self.id, self.len_type, self.len, self.content)

    def get_message_size(self):
        return 2 + self.len_type + self.len
