import json
from collections import defaultdict

# Load your JSON file
with open("habit_tracker_simulation_5users_30days.json", "r") as file:
    data = json.load(file)

# Nested dictionary: user -> habit -> stats
results = defaultdict(lambda: defaultdict(lambda: {
    "days_completed": 0,
    "days_skipped": 0
}))

# Process each entry
for entry in data:
    user = entry["user"]
    for log in entry["daily_log"]:
        habit = log["habit"]
        completed = log["completed"]

        if completed:
            results[user][habit]["days_completed"] += 1
        else:
            results[user][habit]["days_skipped"] += 1

# Calculate success rate
final_output = {}

for user, habits in results.items():
    final_output[user] = {}
    for habit, stats in habits.items():
        completed = stats["days_completed"]
        skipped = stats["days_skipped"]
        total = completed + skipped
        success_rate = (completed / total) * 100 if total else 0.0
        final_output[user][habit] = {
            "days_completed": completed,
            "days_skipped": skipped,
            "success_rate": round(success_rate, 2)
        }

# Output result
print(json.dumps(final_output, indent=2))
