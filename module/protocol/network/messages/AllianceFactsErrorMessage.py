from module.protocol.network.message import Message


class AllianceFactsErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2007
        self.allianceId = {"type": "uint", "value": ""}
