from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountRidingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9431
        self.isRiding = {"type": "Boolean", "value": ""}
        self.isAutopilot = {"type": "Boolean", "value": ""}
