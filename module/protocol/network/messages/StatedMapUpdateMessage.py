from module.protocol.network.message import Message


class StatedMapUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7849
        self.statedElements = {"type": "Vector.<StatedElement>", "value": ""}
