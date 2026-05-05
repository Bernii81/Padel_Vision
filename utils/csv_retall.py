import pandas as pd

df = pd.read_csv("Data-Set/padel-data-labels/labels/2022_BCN_FinalM_1_pose.csv")
filtrat = df[(df["seconds"] >= 15) & (df["seconds"] <= 120)]
filtrat.to_csv("segment_15_120.csv", index=False)
print(f"Files originals: {len(df)}")
print(f"Files filtrades: {len(filtrat)}")