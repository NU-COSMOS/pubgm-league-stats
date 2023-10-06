import pandas as pd

from member import Member

class Team:
    def __init__(self, sheet: pd.DataFrame, tag: str=None) -> None:
        # チームデータのエクセルシート
        self.sheet = sheet
        # チームタグ
        self.tag = tag
        # チーム名
        self.team_name = self.sheet.columns[0]
        # チームメンバー全員のインスタンスを作成
        self.members = self.members()
        

    def members(self) -> list[Member]:
        """チームメンバーのインスタンスを作成"""
        members = []
        for _, row in self.sheet.iterrows():
            if row[self.team_name] == "順位":
                break
            members.append(Member(row))

        return members