from module.protocol.network.message import Message


class PartyInvitationDungeonRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3567
        self.dungeonId = {"type": "uint", "value": ""}
