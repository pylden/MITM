from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountInformationInPaddockRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2919
        self.mapRideId = {"type": "int", "value": ""}
