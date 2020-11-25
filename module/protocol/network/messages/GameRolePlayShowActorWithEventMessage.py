from module.protocol.network.message import Message


class GameRolePlayShowActorWithEventMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1817
        self.actorEventId = {"type": "uint", "value": ""}
