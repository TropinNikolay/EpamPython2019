""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO


def translate_from_dna_to_rna(dna):
    rna = dna.seq.complement().transcribe()
    return rna


def count_nucleotides(dna):
    num_of_nucleotides = {i: dna.seq.count(i) for i in ['A', 'C', 'G', 'T']}
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    protein = rna.translate(stop_symbol='Stop')
    return protein


# this is necessary for histograma
def autolabel(rects):
    """ Attach a text label above each bar in *rect*, displaying its height """
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


dna = None
iteration = 0  # needs for saving number of nucleotides
for dna in SeqIO.parse('files/dna.fasta', 'fasta'):
    rna = translate_from_dna_to_rna(dna)

    nucleotides = count_nucleotides(dna)
    if iteration == 0:
        dna_one_means = [i for i in nucleotides.values()]
    else:
        dna_second_means = [i for i in nucleotides.values()]

    with open('nucleotides.txt', 'a') as inf_1, open('RNA.txt', 'a') as inf_2, open('protein.txt', 'a') as inf_3:
        inf_1.write(dna.description + '\n')
        for key, value in nucleotides.items():
            inf_1.write(key + ' => ' + str(value) + '\n')
        inf_1.write('\n')

        inf_2.write(dna.description + '\n')
        inf_2.write('RNA: ' + str(rna) + '\n')
        inf_2.write('\n')

        inf_3.write(dna.description + '\n')
        inf_3.write('protein: ' + str(translate_rna_to_protein(rna)) + '\n')
        inf_3.write('\n')

    iteration += 1

# now let's draw our histograma
labels = ['A', 'C', 'G', 'T']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rect1 = ax.bar(x - width / 2, dna_one_means, width, label='HSGLTH1')
rect2 = ax.bar(x + width / 2, dna_second_means, width, label='HSBGPG')

ax.set_ylabel('Number of nucleotides')
ax.set_title('Number of nucleotides by group and type')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

autolabel(rect1)
autolabel(rect2)

fig.tight_layout()

plt.show()
