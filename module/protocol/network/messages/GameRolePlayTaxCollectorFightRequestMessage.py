from module.protocol.network.message import Message


class GameRolePlayTaxCollectorFightRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8446
