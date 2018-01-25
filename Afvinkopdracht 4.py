import re, time

def main():
    l_p53 = check_proteins('Mus_musculus.GRCm38.pep.all.fasta')
    verified_proteins = is_protein(l_p53)
    file = read_file('Mus_musculus.GRCm38.dna.chromosome.1.fasta')

    verified_seqs_regex = is_DNA_regex(seqs)
    verified_seqs_iter = is_DNA_iter(seqs)

def check_proteins(file_name):
    pattern = re.compile('MCNSSC[MV]GGMNRR')
    l_p53 = []

    with open(file_name, 'r') as f:
        file = f.readlines()

    for line in file:
        matchObj = pattern.search(line)
        if matchObj:
            l_p53.append(matchObj.group())

    return l_p53

def is_protein(l_p53):
    pattern = re.compile('[^ARNDCQEGHILKMFPSTWYVX]*')

    for seq in l_p53:
        matchObj = pattern.search(seq)
        if matchObj:
            l_p53.remove(seq)

    return l_p53

def read_file(file_name):
    seqs = []
    seq = []

    with open(file_name, 'r') as f:
        file = f.readlines()

    for line in file:
        line = line.rstrip()
        if '>' in line:
            if seq != []:
                seqs.append(''.join(seq))
        else:
            seq.append(line)

    return seqs

def is_DNA_regex(seqs):
    s_time = time.time()
    pattern = re.compile('[^ATGCN]')

    for seq in seqs:
        matchObj = pattern.search(seq)
        if matchObj:
            print(matchObj.group())
            seqs.remove(seq)

    total_time = time.time() - s_time
    print('is_DNA_regex finished in', total_time, 'seconds.')

    return seqs

def is_DNA_iter(seqs):
    s_time = time.time()

    for seq in seqs:
        for char in seq:
            if char not in 'ATGCN':
                print(char)
                seqs.remove(seq)
                break

    total_time = time.time() - s_time
    print('is_DNA_iter finished in', total_time, 'seconds.')
    return seqs

main()









