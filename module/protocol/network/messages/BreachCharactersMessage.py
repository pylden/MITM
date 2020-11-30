from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachCharactersMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5583
        self.characters = {"type": "Vector.<Number>", "value": ""}
