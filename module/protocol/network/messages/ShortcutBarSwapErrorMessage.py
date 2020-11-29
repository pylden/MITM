from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarSwapErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8919
        self.vars.append({"name": "error", "type": "uint", "value": ""})
