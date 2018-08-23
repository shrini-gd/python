def to_rna(dna_strand):
   dna_rna_map = { 'G': 'C', 'C':'G', 'T':'A', 'A':'U'}
   return ''.join([dna_rna_map[c] for c in dna_strand])
