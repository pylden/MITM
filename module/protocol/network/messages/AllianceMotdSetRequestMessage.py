from module.protocol.network.message import Message


class AllianceMotdSetRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6658
        self.content = {"type": "String", "value": ""}
