from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4834
        self.permissions = {"type": "uint", "value": ""}
