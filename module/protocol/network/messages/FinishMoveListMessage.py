from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FinishMoveListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6941
        self.vars.append({"name": "finishMoves", "type": "Vector.<FinishMoveInformations>", "value": ""})
