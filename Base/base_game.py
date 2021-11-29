class BaseGame:

    players = 0

    def reset(self):
        """
        重置游戏
        """
        raise NotImplementedError

    def step(self, player=0):
        """
        player 进行一步动作
        """
        raise NotImplementedError

    def flush(self):
        """
        刷新并处理游戏状态
        """
        raise NotImplementedError

    def is_end(self):
        """
        检测是否触发终止条件
        """
        raise NotImplementedError

    def end(self):
        """
        结束处理
        """
        raise NotImplementedError
