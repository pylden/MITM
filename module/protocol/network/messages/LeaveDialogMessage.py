from module.protocol.network.message import Message


class LeaveDialogMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9843
        self.dialogType = {"type": "uint", "value": ""}
