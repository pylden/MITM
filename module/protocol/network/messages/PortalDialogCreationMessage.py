from module.protocol.network.message import Message


class PortalDialogCreationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4988
        self.type = {"type": "uint", "value": ""}
