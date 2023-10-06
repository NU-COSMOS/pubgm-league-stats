import pandas as pd

from member import Member

class Team:
    def __init__(self, sheet: pd.DataFrame, tag: str, rank_pts: dict[int], kill_pt: int) -> None:
        # 順位ポイント
        self.rank_pts = rank_pts
        # キルポイント
        self.kill_pt = kill_pt
        # チームデータのエクセルシート
        self.sheet = sheet
        # チームタグ
        self.tag = tag
        # チーム名
        self.team_name = self.sheet.columns[0]
        # チームメンバー全員のインスタンスを作成
        self.members = [Member(row) for _, row in self.sheet.iterrows() if row[self.team_name] != "順位"]
        # 合計キル数
        self.total_kills = sum(m.total_kills for m in self.members)
        # 順位ポイント合計
        self.total_rank_pt = self.calc_total_rank_pt()
        # キルポイント合計
        self.total_kill_pt = self.total_kills * kill_pt
        # 合計獲得ポイント
        self.total_pt = self.total_rank_pt + self.total_kill_pt

    def calc_total_rank_pt(self):
        """順位ポイントの合計"""
        total_rank_pt = 0

        for _, row in self.sheet.iterrows():
            if row[self.team_name] == "順位":
                ranks = row[1:]  # チームの順位が格納されている部分
                rank_pts = [self.rank_pts[rank] for rank in ranks if rank in self.rank_pts]
                total_rank_pt += sum(rank_pts)
        
        return total_rank_pt