from module.protocol.network.message import Message


class GuildMotdSetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2776
        self.content = {"type": "String", "value": ""}
