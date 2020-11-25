from module.protocol.network.message import Message


class MountEquipedErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6900
        self.errorType = {"type": "uint", "value": ""}
