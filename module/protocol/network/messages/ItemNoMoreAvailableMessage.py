from module.protocol.network.message import Message


class ItemNoMoreAvailableMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2884
