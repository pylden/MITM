from module.protocol.network.message import Message


class PauseDialogMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6004
        self.dialogType = {"type": "uint", "value": ""}
