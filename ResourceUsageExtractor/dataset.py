import pandas as pd

# File paths
resource_file = r"C:\Users\khush\OneDrive\Desktop\ProjectData\minimal_resource_usage.csv"
task_file = r"C:\Users\khush\OneDrive\Desktop\ProjectData\task_events\part-00000-of-00500.csv\part-00000-of-00500.csv"
job_file = r"C:\Users\khush\OneDrive\Desktop\ProjectData\job_events\part-00000-of-00500.csv\part-00000-of-00500.csv"

# Load Resource Usage Data
resource_df = pd.read_csv(resource_file, delimiter=",", header=0)

# Load Task Events Data with proper column names
task_columns = ["time", "missing_info", "job_id", "task_index", "machine_id", 
                "event_type", "user", "scheduling_class", "priority", "cpu_request", 
                "memory_request", "disk_request", "different_machine"]
task_df = pd.read_csv(task_file, delimiter=",", header=None, names=task_columns)

# Load Job Events Data with proper column names
job_columns = ["time", "missing_info", "job_id", "event_type", "user", "scheduling_class",
               "job_name", "logical_job_name"]
job_df = pd.read_csv(job_file, delimiter=",", header=None, names=job_columns)

# Merge Resource Usage with Task Events on 'job_id' and 'task_index'
combined_df = pd.merge(resource_df, task_df, on=['job_id', 'task_index'], how='inner')

# Merge with Job Events on 'job_id' and 'time'
combined_df = pd.merge(combined_df, job_df, on=['job_id', 'time'], how='inner')

# Save the final combined dataset
output_path = r"C:\Users\khush\OneDrive\Desktop\ProjectData\combined_dataset.csv"
combined_df.to_csv(output_path, index=False)

print("✅ Combined dataset saved at:", output_path)
print(combined_df.head())  # Display the first few rows
