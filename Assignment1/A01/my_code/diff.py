import codecs

# Paths to the files
file1 = "Assignment_Solutions\\A01_Part5\\2_my_sort_simulation\\sort_1.txt"
file2 = "D:\\G Downlaods\\A01\\my_results\\A01_Part5\\2_my_sort_simulation\\sort_1.txt"

# Read the first 20 lines from each file
with codecs.open(file1, "r", encoding="utf-8") as f1, codecs.open(file2, "r", encoding="utf-8") as f2:
    lines1 = [line.strip() for line in f1.readlines()[:20]]
    lines2 = [line.strip() for line in f2.readlines()[:20]]

# Print first 20 lines from file 1
print("First 20 lines from expected file:")
for i, line in enumerate(lines1):
    print(f"{i+1}. {line}")

print("\nFirst 20 lines from your file:")
for i, line in enumerate(lines2):
    print(f"{i+1}. {line}")

# Show key differences in content
print("\nKey differences in entries with count > 1:")
counts_gt_1_file1 = [line for line in lines1 if line.endswith(", 2)") or line.endswith(", 3)") or line.endswith(", 4)")]
counts_gt_1_file2 = [line for line in lines2 if line.endswith(", 2)") or line.endswith(", 3)") or line.endswith(", 4)")]

print("Expected file has these entries with count > 1:")
for line in counts_gt_1_file1:
    print(f"  {line}")

print("\nYour file has these entries with count > 1:")
for line in counts_gt_1_file2:
    print(f"  {line}")