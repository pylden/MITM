from module.protocol.network.message import Message


class GameRolePlayShowActorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9281
        self.informations = {"type": "GameRolePlayActorInformations", "value": ""}
