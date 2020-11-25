from module.protocol.network.message import Message


class PortalDialogCreationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4988
        self.type = {"type": "uint", "value": ""}
