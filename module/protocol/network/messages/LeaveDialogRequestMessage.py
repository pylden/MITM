from module.protocol.network.message import Message


class LeaveDialogRequestMessage(Message):
    def __init__(self):
        self.id = 2225
