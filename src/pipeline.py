import subprocess
import sys

scripts = [
    "src/collect_data.py",
    "src/sentiment_analysis.py",
    "src/rule_engine.py",
    "src/recommend.py",
    "src/export_dashboard.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"Error in {script}, stopping pipeline")
        break
    print(f"{script} completed successfully")

print("\nPipeline complete")