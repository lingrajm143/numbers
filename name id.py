raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_id05_present = "ID05" in unique_users
print(is_id05_present)

print("Original log count:", len(raw_logs))
print("Unique user count:", len(unique_users))

print("Unique Users:", unique_users)
