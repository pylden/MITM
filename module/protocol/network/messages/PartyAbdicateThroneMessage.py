from module.protocol.network.message import Message


class PartyAbdicateThroneMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 793
        self.playerId = {"type": "Number", "value": ""}
