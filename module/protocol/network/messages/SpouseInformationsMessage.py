from module.protocol.network.message import Message


class SpouseInformationsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7590
        self.spouse = {"type": "FriendSpouseInformations", "value": ""}
