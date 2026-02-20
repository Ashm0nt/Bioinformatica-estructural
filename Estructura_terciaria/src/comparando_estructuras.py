#!/usr/bin/env python3

from prog3_1 import core
import pandas as pd
import numpy as np
import sys
import os

def get_files_list(dir: str = "results") -> tuple[str]:
    if not os.path.isdir(dir):
        msg = "[FILES] The given path don't correspond to a file: {dir}"
        raise ValueError(msg)
    return [os.path.join(dir, f) for f in sorted(os.listdir(dir))]

def get_info_from_prog() -> np.ndarray:
    return

def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "./data"
    outfile = sys.argv[2] if len(sys.argv) > 2 else "./results/output.csv"

    if not os.path.isdir(data_dir):
        msg = f"[DATA] The given path don't correspond to a file: {data_dir}"
        raise ValueError(msg)

    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    files = get_files_list(data_dir)
    pdb_files = []

    for file in files:
        if file.endswith(".pdb"):
            pdb_files.append(file)
        elif file.endswith(".faa"):
            fasta = file

    number_files = len(pdb_files)
    number_rows = number_files * (number_files - 1) // 2

    columns = ["Residuos_1", "Residuos_2", "Alineados", "RMSD", "Identidad"]
    number_columns = len(columns)

    if not number_files:
        msg = f"[FILES] No PDB files found in the given path: {data_dir}"
        raise ValueError(msg)

    table = np.zeros((number_rows, number_columns), dtype=np.float64)
    column_names = []

    row = 0
    for i in range(number_files-1):
        pdb_file_1 = pdb_files[i]
        for j in range(i+1, number_files):
            pdb_file_2 = pdb_files[j]

            print(f"Comparing {pdb_file_1} and {pdb_file_2}...")
            results = np.array(core(pdb_file_1, pdb_file_2, fasta, os.path.dirname(outfile), ""))
            name = f"{os.path.splitext(os.path.basename(pdb_file_1))[0]}_{os.path.splitext(os.path.basename(pdb_file_2))[0]}"
            column_names.append(name)
            print(f"Results: {results}\n")
            print("-" * 50)
            
            for k in range(number_columns):
                table[row, k] = results[k]
            row += 1

    pd.DataFrame(table, columns=columns, index=column_names).to_csv(outfile, sep=",", index=True)
    print(f"Comparison completed. Results saved at: {outfile}\n")

    return

if __name__ == "__main__":
    main()