import matplotlib.pyplot as plt
import pandas as pd

# Emotional symptoms dataset
emotional_df = pd.DataFrame({
    "Symptom": ["Sadness - Not at all", "Sadness - Several days",
                "Crying - Never", "Crying - Sometimes", "Crying - Severally"],
    "No_Depression": [73, 2, 73, 1, 0],
    "Depression": [40, 7, 28, 8, 8]
})

# Behavioral dataset
behavior_df = pd.DataFrame({
    "Symptom": ["Interest - Not at all", "Interest - Several days", "Interest - >Half days",
                "Friends - Never", "Friends - Severally"],
    "No_Depression": [71, 1, 3, 68, 0],
    "Depression": [34, 10, 3, 31, 5]
})

# Suicide indicators
suicide_df = pd.DataFrame({
    "Indicator": ["Suicidal Thoughts (Yes)", "Suicide Attempt (Yes)"],
    "No_Depression": [2, 1],
    "Depression": [8, 1]
})

paths = []

def create_chart(df, xcol, ycols, title, filename):
    plt.figure(figsize=(10, 6))
    x = range(len(df[xcol]))
    for col in ycols:
        plt.bar([i + (0.2 if col == ycols[1] else 0) for i in x], df[col], width=0.2, label=col)
    plt.xticks([i+0.1 for i in x], df[xcol], rotation=45, ha='right')
    plt.title(title)
    plt.legend()
    path = f"/mnt/data/{filename}"
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    return path

paths.append(create_chart(emotional_df, "Symptom", ["No_Depression", "Depression"],
                          "Emotional Symptoms by Depression Status", "emotional_symptoms.png"))

paths.append(create_chart(behavior_df, "Symptom", ["No_Depression", "Depression"],
                          "Behavioral Symptoms by Depression Status", "behavioral_symptoms.png"))

paths.append(create_chart(suicide_df, "Indicator", ["No_Depression", "Depression"],
                          "Suicide Indicators by Depression Status", "suicide_indicators.png"))

paths
