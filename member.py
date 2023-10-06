import pandas as pd

class Member:
    def __init__(self, data: pd.Series) -> None:
        self.data = data
        # IGN
        self.name = self.data.iloc[0]
        # 所属チーム名
        self.team = self.data.index[0]
        # これまでのキル
        self.kill_history = self.data.iloc[1:]
        # 合計キル数
        self.total_kills = int(self.kill_history.sum())
        # 出場試合数
        self.num_games = len(self.kill_history) - self.kill_history.isna().sum()
        # 平均キル数
        self.kill_rate = round(self.total_kills / self.num_games, 2)