from module.protocol.network.message import Message


class GuildInvitationByNameMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4298
        self.name = {"type": "String", "value": ""}
