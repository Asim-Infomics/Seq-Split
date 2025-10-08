# Seq-Split
**BioSplit** — a simple, safe, and interactive command-line tool for splitting large bioinformatics sequence files without losing data.   It automatically detects sequence delimiters (FASTA `>`, FASTQ `@`, or custom) and allows users to split large datasets into manageable parts. 
---

## ✨ Features

- **Automatic format detection** — detects FASTA (`>`) or FASTQ (`@`) automatically.  
- **Custom delimiter support** — if unknown, it asks the user for a delimiter (e.g. `LOCUS`).  
- **Loss-free splitting** — guarantees no data truncation or header loss.  
- **Research-friendly** — perfect for tools that can’t handle large input files.  
- **Interactive and CLI modes** — works both with command arguments or via prompts.  

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/biosplit.git
cd biosplit
Install dependencies (none required beyond Python 3):

bash
Copy code
pip install -r requirements.txt
🚀 Usage
1. Automatic mode
bash
Copy code
python biosplit.py input_file --sequences 250
input_file: path to your FASTA, FASTQ, or text-based bioinformatics file.

--sequences: number of sequences per split file (default = 250).

Example:

bash
Copy code
python biosplit.py /home/ai/Documents/proteins.fasta --sequences 250
This creates a folder:

markdown
Copy code
proteins_splits/
    ├── proteins_part1.fasta
    ├── proteins_part2.fasta
    ├── ...
2. Interactive mode
Simply run without arguments:

bash
Copy code
python biosplit.py
You’ll be asked to enter:

The path to your file

Number of sequences per file

 Example Output
vbnet
Copy code
Detected FASTA format (>)
Total sequences found: 2570
Splitting into files with 250 sequences each...
Created: proteins_part1.fasta
Created: proteins_part2.fasta
...
✅ Completed successfully! 11 files saved in folder 'proteins_splits'.
 Requirements
Python ≥ 3.7

Works on Linux, macOS, and Windows.

No third-party libraries required.

📂 Output Structure
Each output file:

Contains complete sequences.

Retains headers and integrity.

Ends exactly where the next file begins (no overlap).

🧑‍💻 Author
Asim Mehmood
🧬 Developed for researchers handling large bioinformatics datasets.

🪪 License
MIT License © 2025 Asim Mehmood

yaml
Copy code
