from module.protocol.network.message import Message


class MountHarnessColorsUpdateRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5586
        self.useHarnessColors = {"type": "Boolean", "value": ""}
