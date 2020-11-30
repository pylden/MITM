from module.protocol.network.messages.UpdateLifePointsMessage import UpdateLifePointsMessage


class LifePointsRegenEndMessage(UpdateLifePointsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        UpdateLifePointsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3437
        self.lifePointsGained = {"type": "uint", "value": ""}
