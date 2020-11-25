from module.protocol.network.message import Message


class GameActionFightTeleportOnSameMapMessage(Message):
    def __init__(self):
        self.id = 2698
