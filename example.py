from module.protocol.network.message import Message


class classname(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(buffer_reader, len_type, length)
        self.id = idMessage
