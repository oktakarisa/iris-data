import subprocess
import os

# path to src
src_dir = os.path.join(os.path.dirname(__file__), "src")

# scripts in order
scripts = [
    "problem1_data_acquisition.py",
    "problem2_combine_data.py",
    "problem3_check_data.py",
    "problem4_dataset_research.py",
    "problem5_extract_features.py",
    "problem6_visualization.py",
    "problem7_feature_relationships.py",
    "problem8_analysis_interpretation.py",
]

print("=== Running Iris Data Analysis ===")
for script in scripts:
    script_path = os.path.join(src_dir, script)
    print(f"\n--- Running {script} ---")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
print("\n=== All scripts executed ===")
