from module.protocol.network.message import Message


class MountInformationRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5729
        self.id = {"type": "Number", "value": ""}
        self.time = {"type": "Number", "value": ""}
