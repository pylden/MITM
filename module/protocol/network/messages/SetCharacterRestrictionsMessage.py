from module.protocol.network.message import Message


class SetCharacterRestrictionsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5009
        self.actorId = {"type": "Number", "value": ""}
        self.restrictions = {"type": "ActorRestrictionsInformations", "value": ""}
