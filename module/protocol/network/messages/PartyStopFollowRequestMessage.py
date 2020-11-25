from module.protocol.network.message import Message


class PartyStopFollowRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9497
        self.playerId = {"type": "Number", "value": ""}
