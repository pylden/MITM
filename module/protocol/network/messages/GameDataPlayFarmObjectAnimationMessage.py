from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameDataPlayFarmObjectAnimationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2642
        self.vars.append({"name": "cellId", "type": "Vector.<uint>", "value": ""})
