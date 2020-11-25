from module.protocol.network.message import Message


class AllianceMotdSetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6658
        self.content = {"type": "String", "value": ""}
