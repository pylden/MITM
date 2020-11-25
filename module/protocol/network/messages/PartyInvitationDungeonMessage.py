from module.protocol.network.message import Message


class PartyInvitationDungeonMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7694
        self.dungeonId = {"type": "uint", "value": ""}
