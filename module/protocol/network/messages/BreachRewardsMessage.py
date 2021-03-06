from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachRewardsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7436
        self.rewards = {"type": "Vector.<BreachReward>", "value": ""}
