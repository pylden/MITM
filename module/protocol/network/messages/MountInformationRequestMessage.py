from module.protocol.network.message import Message


class MountInformationRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5729
        self.id = {"type": "Number", "value": ""}
        self.time = {"type": "Number", "value": ""}
