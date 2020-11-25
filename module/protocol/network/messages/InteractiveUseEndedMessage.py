from module.protocol.network.message import Message


class InteractiveUseEndedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 785
        self.elemId = {"type": "uint", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
