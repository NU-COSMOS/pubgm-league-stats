import pandas as pd

from team import Team

def main():
    excel_name = 'sample.xlsx'
    excel = pd.ExcelFile(excel_name)
    
    # ポイントルールの読み込み
    rule = excel.parse("Rule")
    rank_points = {}
    for _, row in rule.iterrows():
        if row["Rank"] != "kill":
            rank_points[row["Rank"]] = row["Point"]
        else:
            kill_point = row["Point"]

    # 各チームデータの読み込み
    tags = excel.sheet_names
    tags.remove("Rule")
    teams = {}
    for tag in tags:
        team_sheet = excel.parse(tag)
        teams[tag] = Team(team_sheet, tag)


if __name__ == "__main__":
    main()