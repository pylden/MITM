from module.protocol.network.message import Message


class AbstractGameActionFightTargetedAbilityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4295
