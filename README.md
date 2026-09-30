# DNA Sequence Utility

A small interactive Python program for basic DNA sequence checks and operations. It uses only Python's built-in features and requires no third-party packages.

## Requirements

- Python 3
- No external libraries

## Run the program

Open a terminal in this folder and run:

```powershell
python "DNA Sequence Utility.py"
```

## Features

- Enter a DNA sequence and check whether its characters are limited to A, T, G, and C.
- Count the sequence length and each nucleotide, and calculate GC content as a percentage of the total length.
- Compare two equal-length sequences by position and report the matching-base count and percentage identity.
- Find the complementary strand, reverse complement, or RNA transcription produced by replacing T with U.
- Navigate between input and validation, analysis, and operations using the text menus.

Input is converted to uppercase when entered. The program stores one sequence at a time; it does not save results to a file.

## Menu overview

The main menu groups actions into input and validation, DNA analysis, and DNA operations. Each group has a submenu with an option to return to the main menu. Select the exit option from the main menu to close the program.

## Notes

The validity check is separate from sequence entry, so the program records input even if it contains characters other than A, T, G, or C. Some operations can therefore produce misleading output for invalid sequences. See [REPORT.md](REPORT.md) for implementation details and limitations.