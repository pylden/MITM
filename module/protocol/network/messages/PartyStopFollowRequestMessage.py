from module.protocol.network.message import Message


class PartyStopFollowRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9497
        self.playerId = {"type": "Number", "value": ""}
