from module.protocol.network.message import Message


class NewMailMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7617
        self.sendersAccountId = {"type": "Vector.<uint>", "value": ""}
