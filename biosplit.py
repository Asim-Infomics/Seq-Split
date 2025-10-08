#!/usr/bin/env python3
"""
BioSplit — A simple, safe, and interactive file splitter for bioinformatics data.
Supports FASTA, FASTQ, and any text-based sequence format.

Usage (automatic):
    python biosplit.py input_file --sequences 250

Usage (interactive):
    python biosplit.py
"""

import os
import argparse

def detect_delimiter(file_path):
    """Detect delimiter automatically, or ask user if unknown."""
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                print("Detected FASTA format (>)")
                return '>'
            elif line.startswith('@'):
                print("Detected FASTQ format (@)")
                return '@'

    # If no standard delimiter found, ask user
    custom = input("\nCould not auto-detect delimiter. Please enter the delimiter (e.g. >, @, LOCUS, etc.): ").strip()
    if not custom:
        raise ValueError("Delimiter cannot be empty.")
    print(f"Using custom delimiter: '{custom}'")
    return custom


def split_file(file_path, sequences_per_file):
    """Split the file safely without losing data."""
    delimiter = detect_delimiter(file_path)
    file_base = os.path.splitext(os.path.basename(file_path))[0]
    file_ext = os.path.splitext(file_path)[1]

    with open(file_path, 'r') as f:
        lines = f.readlines()

    seq_indices = [i for i, line in enumerate(lines) if line.startswith(delimiter)]
    total_sequences = len(seq_indices)

    if total_sequences == 0:
        print("No sequences detected. Exiting.")
        return

    print(f"\nTotal sequences found: {total_sequences}")
    print(f"Splitting into files with {sequences_per_file} sequences each...")

    output_folder = f"{file_base}_splits"
    os.makedirs(output_folder, exist_ok=True)
    split_count = 0

    for start in range(0, total_sequences, sequences_per_file):
        end = start + sequences_per_file
        seq_start = seq_indices[start]
        seq_end = seq_indices[end] if end < total_sequences else len(lines)
        chunk_lines = lines[seq_start:seq_end]

        output_file = os.path.join(output_folder, f"{file_base}_part{split_count+1}{file_ext}")
        with open(output_file, 'w') as out:
            out.writelines(chunk_lines)

        split_count += 1
        print(f"Created: {output_file}")

    print(f"\n✅ Completed successfully! {split_count} files saved in folder '{output_folder}'.")


def interactive_mode():
    """Handle user interaction when no CLI args are given."""
    file_path = input("Enter path to input file: ").strip()
    while not os.path.isfile(file_path):
        print("Invalid file path. Please try again.")
        file_path = input("Enter path to input file: ").strip()

    sequences_per_file = input("Enter number of sequences per split file (e.g. 250): ").strip()
    while not sequences_per_file.isdigit() or int(sequences_per_file) <= 0:
        print("Please enter a valid positive integer.")
        sequences_per_file = input("Enter number of sequences per split file: ").strip()

    split_file(file_path, int(sequences_per_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split large bioinformatics sequence files safely.")
    parser.add_argument("input_file", nargs="?", help="Path to the input file (FASTA/FASTQ or custom format)")
    parser.add_argument("--sequences", type=int, help="Number of sequences per split file")

    args = parser.parse_args()

    if args.input_file:
        sequences = args.sequences if args.sequences else 250
        split_file(args.input_file, sequences)
    else:
        interactive_mode()

