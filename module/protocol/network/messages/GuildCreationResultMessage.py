from module.protocol.network.message import Message


class GuildCreationResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3699
        self.result = {"type": "uint", "value": ""}
