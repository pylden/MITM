from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagRoomUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4575
        self.action = {"type": "uint", "value": ""}
        self.roomsPreview = {"type": "Vector.<HavenBagRoomPreviewInformation>", "value": ""}
