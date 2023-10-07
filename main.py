import pandas as pd

from team import Team


def make_kill_rank(teams: list[Team], top_n: int=10) -> list[dict[str, str, int]]:
    """合計キル数上位n人を求める"""
    kill_rank = []

    # 各チームのメンバーをフラットなリストにする
    all_members = [m for t in teams for m in t.members]

    # キル数でソート
    all_members.sort(key=lambda m: m.total_kills, reverse=True)

    # 上位n人を取得
    top_players = all_members[:top_n]

    # 辞書形式に変換
    kill_rank = [{"Team": player.team, "Name": player.name, "Kill": player.total_kills} for player in top_players]

    return kill_rank

def make_team_rank(teams: list[Team]):
    """チームランキングの作成"""
    teams.sort(key=lambda t: t.total_pt, reverse=True)

    for t in teams:
        print(t.team_name, t.total_pt)

    return teams


def main():
    excel_name = 'sample.xlsx'
    excel = pd.ExcelFile(excel_name)
    
    # ポイントルールの読み込み
    rule = excel.parse("Rule")
    rank_pts = {}
    for _, row in rule.iterrows():
        if row["Rank"] != "kill":
            rank_pts[row["Rank"]] = row["Point"]
        else:
            kill_pt = row["Point"]

    # 各チームデータの読み込み
    tags = excel.sheet_names
    tags.remove("Rule")
    teams = []
    for tag in tags:
        team_sheet = excel.parse(tag)
        teams.append(Team(team_sheet, tag, rank_pts, kill_pt))

    team_rank = make_team_rank(teams)

    kill_rank = make_kill_rank(teams)


if __name__ == "__main__":
    main()