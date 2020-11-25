from module.protocol.network.message import Message


class AccessoryPreviewMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5
        self.look = {"type": "EntityLook", "value": ""}
