from module.protocol.network.message import Message


class MountRenamedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7458
        self.mountId = {"type": "int", "value": ""}
        self.name = {"type": "String", "value": ""}
