from module.protocol.network.message import Message


class PartyCannotJoinErrorMessage(Message):
    def __init__(self):
        self.id = 4290
