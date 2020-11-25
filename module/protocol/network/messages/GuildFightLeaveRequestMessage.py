from module.protocol.network.message import Message


class GuildFightLeaveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3803
        self.taxCollectorId = {"type": "Number", "value": ""}
        self.characterId = {"type": "Number", "value": ""}
