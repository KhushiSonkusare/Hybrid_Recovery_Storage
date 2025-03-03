import pandas as pd


df = pd.read_csv("final_dataset.csv")  

high_access_threshold = df['access_frequency'].quantile(0.7)
low_access_threshold = df['access_frequency'].quantile(0.3)

high_data_size_threshold = df['data_size_indicator'].quantile(0.7)
low_data_size_threshold = df['data_size_indicator'].quantile(0.3)


def assign_strategy(row):
    if row['access_frequency'] >= high_access_threshold and row['latency_sensitivity'] == 1 and row['read_write_ratio'] > 0.7:
        return 0  # Replication
    elif row['data_size_indicator'] >= high_data_size_threshold and row['access_frequency'] <= low_access_threshold and row['read_write_ratio'] < 0.3:
        return 1  # Erasure Coding
    else:
        return 0 if row['read_write_ratio'] >= 0.5 else 1  

# Apply function to dataset
df['storage_strategy'] = df.apply(assign_strategy, axis=1)

df.to_csv("final_labeled_dataset.csv", index=False)

print("✅ Dataset labeled and saved as final_labeled_dataset.csv")