import warnings

import matplotlib.pyplot as plt
import numpy as np


def count_nucleotides(dna: str) -> dict:
    num_of_nucleotides = {i: dna.count(i) for i in ["A", "C", "G", "T"]}
    return num_of_nucleotides


def translate_from_dna_to_rna(dna: str) -> str:
    rna = (
        dna.replace("A", "U")
        .replace("T", "A")
        .replace("G", "X")
        .replace("C", "G")
        .replace("X", "C")
    )

    return rna


def translate_rna_to_protein(rna: str) -> str:
    if len(rna) % 3 != 0:
        warnings.warn("Partial codon, len(sequence) not a multiple of three.")

    protein = ""
    length = (len(rna) // 3) * 3
    for i in range(0, length, 3):
        st = rna[i : i + 3]
        protein += rna_to_protein_table[st]
    return protein


def read_dna_fasta(file) -> dict:
    """ returning dictionary with gene: dna pairs """
    dna_sequences = file.readlines()

    index = 1
    string = ""
    all_dna = {}
    name = dna_sequences[0].strip()
    for line in dna_sequences[1:]:
        if not line.startswith(">"):
            string += line.strip()
            if index == len(dna_sequences) - 1:
                all_dna[name] = string
        else:
            all_dna[name] = string
            string = ""
            name = line.strip()
        index += 1
    return all_dna


def read_rna_codon_table(file) -> dict:
    voc = {}
    for line in file.readlines():
        arr_of_simbols = line.strip().split()
        for ind in range(0, len(arr_of_simbols) - 1, 2):
            voc[arr_of_simbols[ind]] = arr_of_simbols[ind + 1]
    return voc


# this is necessary for histograma
def autolabel(rects):
    """ Attach a text label above each bar in *rect*, displaying its height """
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


with open("files/dna.fasta") as data:
    all_dna = read_dna_fasta(data)

with open("files/rna_codon_table.txt") as inf:
    rna_to_protein_table = read_rna_codon_table(inf)

iteration = 0  # needs for saving number of nucleotides
with open("files/nucleotides.txt", "w") as inf_1, open(
    "files/RNA.txt", "w"
) as inf_2, open("files/protein.txt", "w") as inf_3:
    for key, value in all_dna.items():
        nucleotides = count_nucleotides(value)

        if iteration == 0:
            dna_one_means = [i for i in nucleotides.values()]
        else:
            dna_second_means = [i for i in nucleotides.values()]

        inf_1.write(key + "\n")
        inf_1.write(str(nucleotides) + "\n")
        inf_1.write("\n")

        rna = translate_from_dna_to_rna(value)

        inf_2.write(key + "\n")
        inf_2.write(str(rna) + "\n")
        inf_2.write("\n")

        protein = translate_rna_to_protein(rna)

        inf_3.write(key + "\n")
        inf_3.write(str(protein) + "\n")
        inf_3.write("\n")

        iteration += 1

# now let's draw our histograma
labels = ["A", "C", "G", "T"]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rect1 = ax.bar(x - width / 2, dna_one_means, width, label="HSGLTH1")
rect2 = ax.bar(x + width / 2, dna_second_means, width, label="HSBGPG")

ax.set_ylabel("Number of nucleotides")
ax.set_title("Number of nucleotides by group and type")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

autolabel(rect1)
autolabel(rect2)

fig.tight_layout()

plt.show()
