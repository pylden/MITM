from module.protocol.network.message import Message


class DebtsUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3503
