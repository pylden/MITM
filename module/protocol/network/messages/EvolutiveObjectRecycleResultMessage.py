from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EvolutiveObjectRecycleResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6221
        self.recycledItems = {"type": "Vector.<RecycledItem>", "value": ""}
