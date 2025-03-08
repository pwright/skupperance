#!/usr/bin/env python3

import os
import difflib
import argparse
from pathlib import Path

DOCS_DIR = "docs"
OUTPUT_DIR = "docs/diffs"  # Directory to store diff reports

def get_subdirectories(base_dir):
    """Get all subdirectories inside the base directory."""
    return [d.name for d in Path(base_dir).iterdir() if d.is_dir()]

def get_files_in_subdir(subdir):
    """Get all Markdown files in a given subdirectory."""
    return {f.name for f in Path(DOCS_DIR, subdir).glob("*.md")}

def compare_files(file1, file2):
    """Compare two files and return differences as a list of strings."""
    with open(file1, 'r', encoding="utf-8") as f1, open(file2, 'r', encoding="utf-8") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    diff = list(difflib.unified_diff(f1_lines, f2_lines, fromfile=str(file1), tofile=str(file2), lineterm=""))
    return diff if diff else None

def generate_report(subdir1, subdir2):
    """Generate a Markdown report comparing files in two subdirectories."""
    files1 = get_files_in_subdir(subdir1)
    files2 = get_files_in_subdir(subdir2)

    common_files = files1 & files2
    identical_files = []
    different_files = []

    output_file = Path(OUTPUT_DIR, f"{subdir1}-{subdir2}.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

    with output_file.open("w", encoding="utf-8") as out:
        out.write(f"# 📄 Comparison: `{subdir1}` vs `{subdir2}`\n\n")

        # Summary Table
        out.write("| Category       | Count |\n")
        out.write("|---------------|------:|\n")

        # Identical files
        if common_files:
            for file in sorted(common_files):
                file1 = Path(DOCS_DIR, subdir1, file)
                file2 = Path(DOCS_DIR, subdir2, file)

                if compare_files(file1, file2) is None:
                    identical_files.append(file)

            out.write(f"| ✅ Identical Files | {len(identical_files)} |\n")

        # Different files
        different_files = sorted(common_files - set(identical_files))
        out.write(f"| ⚠️ Different Files | {len(different_files)} |\n\n")

        # Identical files list
        if identical_files:
            out.write("## ✅ Identical Files\n\n")
            for file in identical_files:
                out.write(f"- `{file}`\n")
            out.write("\n")

        # Differences section
        if different_files:
            out.write("## ⚠️ Differences\n\n")
            for file in different_files:
                file1 = Path(DOCS_DIR, subdir1, file)
                file2 = Path(DOCS_DIR, subdir2, file)

                diff = compare_files(file1, file2)
                if diff:
                    out.write(f"### 🔍 `{file}`\n\n")
                    out.write(f"**{subdir1}** vs **{subdir2}**\n\n")
                    out.write("```diff\n")
                    out.write("\n".join(diff))
                    out.write("\n```\n\n")
    
    return identical_files, different_files, output_file

def main():
    parser = argparse.ArgumentParser(description="Compare Markdown files in subdirectories.")
    parser.add_argument("dirs", nargs="*", help="Optional: specify two directories to compare.")
    args = parser.parse_args()

    subdirs = get_subdirectories(DOCS_DIR)

    if args.dirs:
        if len(args.dirs) != 2:
            print("Error: Please specify exactly two directories for comparison.")
            return
        comparisons = [tuple(args.dirs)]
    else:
        comparisons = [(a, b) for i, a in enumerate(subdirs) for b in subdirs[i + 1:]]

    for subdir1, subdir2 in comparisons:
        print(f"Comparing {subdir1} vs {subdir2}...")
        identical_files, different_files, report_path = generate_report(subdir1, subdir2)
        
        print(f"Report saved: {report_path}")
        print(f"Identical files: {len(identical_files)}, Different files: {len(different_files)}\n")

if __name__ == "__main__":
    main()
