# DNA Sequence Utility: Project Report

## Summary

This project is a command-line Python program for basic DNA sequence handling. It presents a main menu with three groups: input and validation, DNA analysis, and DNA operations. A fourth option exits the program.

## Features and implementation

### Input and validation

The program stores the current sequence in the `dna` variable. When a sequence is entered, it is converted to uppercase. Validation checks each character against `ATGC` and reports whether the sequence is valid.

### Basic analysis

The program uses string counts to calculate the number of A, T, G, and C bases and reports the string length. GC content is computed as:

```text
(G count + C count) / sequence length * 100
```

Sequence comparison requires equal lengths. It compares bases at matching indexes, counts equal positions, and divides that count by the sequence length to calculate percent identity.

### DNA operations

- **Complement:** maps A to T, T to A, G to C, and C to G while preserving order.
- **Reverse complement:** reverses the complement string.
- **Transcription:** replaces T with U. This treats the entered sequence as the coding strand.

## Structure and approach

All behavior is currently implemented in `DNA Sequence Utility.py`. The main loop displays the top-level menu; nested loops manage each submenu. The current sequence is shared across these menus in one variable, and each operation is implemented in its corresponding menu branch. No external libraries are required.

## Limitations

- Entering a sequence does not automatically validate it; validation is a separate menu action.
- Analysis and sequence operations only check whether a sequence was entered, not whether it is valid DNA. Invalid characters may make counts, GC percentage, or derived sequences misleading.
- The second sequence in a comparison is not checked for valid DNA characters.
- The program stores only one current sequence and has no file import, export, or persistent history.
- There are no automated tests in the current project.
- Transcription is a simple T-to-U replacement and does not model strand orientation or RNA processing.

## Suggested improvements

Validate sequences at entry and before every operation, move computations into reusable functions, and add automated tests for valid input, invalid input, empty input, comparison, and strand operations. File input and result export could be added later if needed.

## Manual checks

1. Enter `ATGC` and validate it; the program should report a valid sequence.
2. Analyze `ATGC`; expect one of each base, length 4, and GC content 50%.
3. Find the complement of `ATGC`; expect `TACG`.
4. Find the reverse complement of `ATGC`; expect `GCAT`.
5. Transcribe `ATGC`; expect `AUGC`.
6. Compare `ATGC` with `ATGA`; expect 3 matching bases and 75% identity.