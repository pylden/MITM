from module.protocol.network.message import Message


class GameContextDestroyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5443
