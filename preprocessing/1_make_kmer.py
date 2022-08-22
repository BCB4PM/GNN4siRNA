# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:53:19 2022

@author: Massimo La Rosa
crate the kmers count file
"""
import numpy as np
import params

class kmer_featurization:

  def __init__(self, k):
    """
    seqs: a list of DNA sequences
    k: the "k" in k-mer
    """
    self.k = k
    self.letters = ['A', 'T', 'C', 'G']
    self.multiplyBy = 4 ** np.arange(k-1, -1, -1) # the multiplying number for each digit position in the k-number system
    self.n = 4**k # number of possible k-mers

  def obtain_kmer_feature_for_a_list_of_sequences(self, seqs, write_number_of_occurrences=False):
    """
    Given a list of m DNA sequences, return a 2-d array with shape (m, 4**k) for the 1-hot representation of the kmer features.

    Args:
      write_number_of_occurrences:
        a boolean. If False, then in the 1-hot representation, the percentage of the occurrence of a kmer will be recorded; otherwise the number of occurrences will be recorded. Default False.    
    """
    kmer_features = []
    for seq in seqs:
      this_kmer_feature = self.obtain_kmer_feature_for_one_sequence(seq.upper(), write_number_of_occurrences=write_number_of_occurrences)
      kmer_features.append(this_kmer_feature)

    kmer_features = np.array(kmer_features)

    return kmer_features

  def obtain_kmer_feature_for_one_sequence(self, seq, write_number_of_occurrences=False):
    """
    Given a DNA sequence, return the 1-hot representation of its kmer feature.

    Args:
      seq: 
        a string, a DNA sequence
      write_number_of_occurrences:
        a boolean. If False, then in the 1-hot representation, the percentage of the occurrence of a kmer will be recorded; otherwise the number of occurrences will be recorded. Default False.
    """
    number_of_kmers = len(seq) - self.k + 1

    kmer_feature = np.zeros(self.n)

    for i in range(number_of_kmers):
      this_kmer = seq[i:(i+self.k)]
      ok = True
      for letter in this_kmer:
          if (letter not in self.letters):
              ok = False
      if (ok):
          this_numbering = self.kmer_numbering_for_one_kmer(this_kmer)
          kmer_feature[this_numbering] += 1

    if not write_number_of_occurrences:
      kmer_feature = kmer_feature / number_of_kmers

    return kmer_feature

  def kmer_numbering_for_one_kmer(self, kmer):
    """
    Given a k-mer, return its numbering (the 0-based position in 1-hot representation)
    """
    digits = []
    for letter in kmer:
        
      digits.append(self.letters.index(letter))
      

    digits = np.array(digits)

    numbering = (digits * self.multiplyBy).sum()

    return numbering


from Bio import SeqIO
# fasta file
sirna_fasta_file = params.sirna_fasta_file
mrna_fasta_file = params.mrna_fasta_file

# sirna k-mer size
k_sirna = params.k_sirna
k_mrna = params.k_mrna

kmer_sirna = kmer_featurization(k_sirna)
kmer_mrna = kmer_featurization(k_mrna)

foutput_sirna = open("sirna_kmers.txt",'w') #outuput file
foutput_mrna = open("mRNA_kmers.txt",'w') #outuput file


# create sirna k-mer file
for seq_record in SeqIO.parse(sirna_fasta_file, 'fasta'): #input fasta file
    rna_id = seq_record.id
    seq = seq_record.seq
    seq = seq.upper()
    seq = seq.replace('U','T')
    k = kmer_sirna.obtain_kmer_feature_for_one_sequence(seq,True)
    k = [int(elem) for elem in k]
    k = [str(elem) for elem in k]
    foutput_sirna.write(str(rna_id)+","+",".join(k)+"\n")
foutput_sirna.close()


  # create mRNA k-mer file
for seq_record in SeqIO.parse(mrna_fasta_file, 'fasta'): #input fasta file
    rna_id = seq_record.id
    seq = seq_record.seq
    seq = seq.upper()
    seq = seq.replace('U','T')
    k = kmer_mrna.obtain_kmer_feature_for_one_sequence(seq,True)
    k = [int(elem) for elem in k]
    k = [str(elem) for elem in k]
    foutput_mrna.write(str(rna_id)+","+",".join(k)+"\n")
foutput_mrna.close() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
