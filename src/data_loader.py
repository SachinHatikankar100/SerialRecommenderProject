import pandas as pd

class SerialDataLoader:

    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv


    def load_and_process(self):
        df = pd.read_csv(self.original_csv,encoding="utf-8",on_bad_lines='skip').dropna()

        requiredColumns = {"Name","genres","overview"}

        missing = requiredColumns - set(df.columns)
        if missing:
            raise ValueError("Required column is missing in CSV file")

        df["combined_data"] = (
            "Title"+df["Name"]+" Overview "+df["overview"]+" genre "+df["genres"]
        )

        df[["combined_data"]].to_csv(self.processed_csv,index=False,encoding="utf-8")
        return self.processed_csv