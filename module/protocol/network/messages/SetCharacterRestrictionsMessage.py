from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SetCharacterRestrictionsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5009
        self.actorId = {"type": "Number", "value": ""}
        self.restrictions = {"type": "ActorRestrictionsInformations", "value": ""}
