from module.protocol.network.message import Message


class AccessoryPreviewMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5
        self.look = {"type": "EntityLook", "value": ""}
