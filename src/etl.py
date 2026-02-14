import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
OUT_PATH = Path("data/processed/churn_clean.parquet")

def run_etl():
    df = pd.read_csv(RAW_PATH)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    df["churn_flag"] = df["churn"].map({"Yes": 1, "No": 0})

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT_PATH, index=False)

    print("Saved:", OUT_PATH.as_posix())

if __name__ == "__main__":
    run_etl()
