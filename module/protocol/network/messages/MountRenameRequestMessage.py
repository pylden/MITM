from module.protocol.network.message import Message


class MountRenameRequestMessage(Message):
    def __init__(self):
        self.id = 9887
        self.name = {"type": "String", "value": ""}
