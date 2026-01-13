from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

OUT_PATH = Path("data/raw/patient_timeseries.csv")

def generate(n_patients: int = 200, n_weeks: int = 12, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    rows = []
    for pid in range(1, n_patients + 1):
        age = int(rng.integers(18, 80))
        sex = rng.choice(["F", "M"])
        height_cm = int(rng.integers(150, 200))
        baseline_weight = float(rng.normal(82, 15))
        baseline_sbp = float(rng.normal(128, 14))
        baseline_dbp = float(rng.normal(82, 10))
        baseline_hba1c = float(np.clip(rng.normal(5.8, 0.9), 4.5, 11.5))
        baseline_steps = float(np.clip(rng.normal(6500, 2200), 500, 16000))
        baseline_sleep = float(np.clip(rng.normal(7.0, 1.0), 4.0, 9.5))

        # patient-specific drift
        weight_trend_per_week = float(rng.normal(-0.10, 0.25))  # kg/week
        sbp_trend_per_week = float(rng.normal(-0.2, 0.6))
        steps_trend_per_week = float(rng.normal(80, 180))

        for week in range(n_weeks):
            noise_w = rng.normal(0, 0.6)
            noise_bp = rng.normal(0, 3.0)
            noise_steps = rng.normal(0, 900)
            noise_sleep = rng.normal(0, 0.4)
            noise_hba1c = rng.normal(0, 0.05)

            weight_kg = float(np.clip(baseline_weight + week * weight_trend_per_week + noise_w, 45, 180))
            sbp = float(np.clip(baseline_sbp + week * sbp_trend_per_week + noise_bp, 90, 200))
            dbp = float(np.clip(baseline_dbp + week * (sbp_trend_per_week * 0.4) + noise_bp * 0.4, 55, 120))
            steps = float(np.clip(baseline_steps + week * steps_trend_per_week + noise_steps, 0, 25000))
            sleep_h = float(np.clip(baseline_sleep + noise_sleep, 3.5, 10.5))
            hba1c = float(np.clip(baseline_hba1c + noise_hba1c, 4.2, 12.5))

            rows.append({
                "patient_id": f"P{pid:04d}",
                "week": week,
                "age": age,
                "sex": sex,
                "height_cm": height_cm,
                "weight_kg": round(weight_kg, 1),
                "sbp": round(sbp, 0),
                "dbp": round(dbp, 0),
                "hba1c": round(hba1c, 2),
                "steps": int(round(steps)),
                "sleep_h": round(sleep_h, 1),
            })

    return pd.DataFrame(rows)

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate(n_patients=200, n_weeks=12, seed=7)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df):,} rows to {OUT_PATH}")

if __name__ == "__main__":
    main()
