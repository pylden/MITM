from module.protocol.network.message import Message


class InteractiveMapUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7734
        self.interactiveElements = {"type": "Vector.<InteractiveElement>", "value": ""}
