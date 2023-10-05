import pandas as pd

class Team:
    def __init__(self, sheet: pd.DataFrame, tag: str=None) -> None:
        self.sheet = sheet
        self.tag = tag