from module.protocol.network.message import Message


class MountReleasedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3002
        self.mountId = {"type": "int", "value": ""}
