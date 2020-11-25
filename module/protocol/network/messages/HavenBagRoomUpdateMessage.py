from module.protocol.network.message import Message


class HavenBagRoomUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4575
        self.action = {"type": "uint", "value": ""}
        self.roomsPreview = {"type": "Vector.<HavenBagRoomPreviewInformation>", "value": ""}
