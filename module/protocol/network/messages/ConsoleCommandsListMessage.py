from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1923
        self.aliases = {"type": "Vector.<String>", "value": ""}
        self.args = {"type": "Vector.<String>", "value": ""}
        self.descriptions = {"type": "Vector.<String>", "value": ""}
