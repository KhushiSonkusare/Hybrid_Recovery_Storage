import os
import pandas as pd

# 📌 Define the folder path containing the files
folder_path = r"C:\Users\khush\OneDrive\Desktop\ProjectData\part-00000-of-00500.csv"

# 📌 Define column names (modify as per your requirements)
columns = [
    "start_time", "end_time", "job_id", "task_index", "machine_id",
    "cpu_usage", "memory_usage", "disk_io_time", "disk_space_used",
    "max_disk_io_time", "cycles_per_instruction", "memory_accesses_per_instruction",
    "sampled_cpu_usage", "assignments", "page_cache_memory", "major_page_faults",
    "mean_disk_io_time", "cpu_wait_time", "network_io_time", "unknown_metric"
]

# 📌 List to store extracted data
data = []

# 📌 Process only the first 1000 files for minimal dataset
file_count = 0
max_files = 1000  # Change this value if you need more or fewer files

for filename in os.listdir(folder_path):
    if file_count >= max_files:
        break  # Stop after processing the required number of files

    try:
        # Extract values by splitting the filename on commas
        values = filename.split(",")

        # Ensure correct number of values before adding
        if len(values) == len(columns):
            data.append(values)
            file_count += 1
        else:
            print(f"⚠️ Skipping file (incorrect format): {filename}")

    except Exception as e:
        print(f"❌ Error processing file {filename}: {e}")

# 📌 Convert to DataFrame
df = pd.DataFrame(data, columns=columns)

# 📌 Save to CSV
output_file = os.path.join(folder_path, "minimal_resource_usage.csv")
df.to_csv(output_file, index=False)

print(f"✅ Data extraction complete! Saved as {output_file}")
