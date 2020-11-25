from module.protocol.network.message import Message


class GameRolePlayGameOverMessage(Message):
    def __init__(self):
        self.id = 2037
