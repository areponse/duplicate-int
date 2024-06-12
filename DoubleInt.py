# Link https://github.com/areponse/duplicate-int

import os
import sys

def process_file(input_file_path, output_dir):
    duplicates = {}
    duplicate_count = 0
    file_extension = os.path.splitext(input_file_path)[1].lower()

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            if validate_line(line.strip()):
                integers = parse_line(line.strip())
                for integer in integers:
                    if is_proper_number(integer) and is_in_range(integer):
                        if integer in duplicates:
                            duplicates[integer] += 1
                        else:
                            duplicates[integer] = 1

    duplicate_items = [k for k, v in duplicates.items() if v > 1]

    sorted_items = merge_sort(duplicate_items)

    output_file_path = os.path.join(output_dir, os.path.basename(input_file_path)[:-4] + "_results.txt")
    print(f"Output file path: {output_file_path}")

    with open(output_file_path, 'w') as output_file:
        for item in sorted_items:
            output_file.write(str(item) + '\n')

def validate_line(line):
    if line.strip() == '':
        return False
    parts = line.split()
    if len(parts) != 1:
        return False
    if '--' in line:
        return False
    return True

def parse_line(line):
    integers = []
    for part in split_line(line):
        if is_valid_integer(part):
            integers.append(int(part))
    return integers

def split_line(line):
    return line.split()

def is_valid_integer(part):
    return part.strip().isdigit() or (part.strip().startswith('-') and part.strip().count('-') == 1 and part.strip().lstrip('-').isdigit())

def is_proper_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_in_range(num):
    return -1023 <= num <= 1023

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_dir = 'sample_results/'

    if not os.path.exists(input_file_path):
        print("Error: Input file not found.")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process_file(input_file_path, output_dir)
    print("File processed successfully.")
