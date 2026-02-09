
import os
import random
from datetime import datetime, timedelta

# ===== CONFIG =====
DAYS_BACK = 30          # Isi 30 hari ke belakang
MIN_COMMITS = 8         # Minimal commit per hari (full hijau)
MAX_COMMITS = 15        # Maksimal commit per hari
FILE_NAME = "full_green_log.txt"
# ==================

def run():
    print("🚀 Generating FULL GREEN contribution...")
    
    for d in range(1, DAYS_BACK + 1):
        commit_count = random.randint(MIN_COMMITS, MAX_COMMITS)

        for _ in range(commit_count):
            random_minutes = random.randint(0, 1440)
            commit_date = datetime.now() - timedelta(days=d, minutes=random_minutes)
            formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

            with open(FILE_NAME, "a") as f:
                f.write(f"Massive update at {formatted_date}\n")

            os.system("git add .")
            os.system(
                f'GIT_AUTHOR_DATE="{formatted_date}" '
                f'GIT_COMMITTER_DATE="{formatted_date}" '
                f'git commit -m "feat: major improvement"'
            )

    print("✅ FULL GREEN selesai! Sekarang jalankan:")
    print("git push origin main")

if __name__ == "__main__":
    run()
