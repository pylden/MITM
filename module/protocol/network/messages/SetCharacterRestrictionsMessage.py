from module.protocol.network.message import Message


class SetCharacterRestrictionsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5009
        self.actorId = {"type": "Number", "value": ""}
        self.restrictions = {"type": "ActorRestrictionsInformations", "value": ""}
