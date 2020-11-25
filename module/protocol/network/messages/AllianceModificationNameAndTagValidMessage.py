from module.protocol.network.message import Message


class AllianceModificationNameAndTagValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8421
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
