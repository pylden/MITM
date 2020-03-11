class Packet:
    def __init__(self, packet_id, len_type, length, msg):
        self.id = packet_id
        self.len_type = len_type
        self.len = length
        self.msg = msg

    def __repr__(self):
        return "Id: {0}\nLength Type: {1}\nLength: {2}\nMessage: {3}".format(self.id, self.len_type, self.len, self.msg)

    def get_packet_size(self):
        return 2 + self.len_type + self.len
