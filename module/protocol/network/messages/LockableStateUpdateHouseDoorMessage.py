from module.protocol.network.message import Message


class LockableStateUpdateHouseDoorMessage(Message):
    def __init__(self):
        self.id = 3227
