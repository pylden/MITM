from module.protocol.network.message import Message


class GameRolePlayPlayerFightRequestMessage(Message):
    def __init__(self):
        self.id = 8916
