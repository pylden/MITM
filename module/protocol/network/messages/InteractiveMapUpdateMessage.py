from module.protocol.network.message import Message


class InteractiveMapUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7734
        self.interactiveElements = {"type": "Vector.<InteractiveElement>", "value": ""}
