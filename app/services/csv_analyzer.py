import pandas as pd

def analyze_csv(csv_path: str) -> str:
    df = pd.read_csv(csv_path)

    summary = []

    summary.append(f"Rows: {len(df)}, Columns: {len(df.columns)}")

    numeric_cols = df.select_dtypes(include="number")

    if not numeric_cols.empty:
        desc = numeric_cols.describe().round(2)
        summary.append("Numeric statistics:")
        summary.append(desc.to_string())

    return "\n".join(summary)
