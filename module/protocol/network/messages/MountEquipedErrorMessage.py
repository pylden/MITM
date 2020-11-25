from module.protocol.network.message import Message


class MountEquipedErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6900
