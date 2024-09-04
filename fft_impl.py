import math

def butterfly(v,k,h,a,b):
    e1 = v[k]+a*v[k+h]
    e2 = b*v[k+h]+v[k]
    v[k] = e1
    v[k+h] = e2


def sort_values(v,N):
    num_bit = int(math.log2(N))
    s = '{:0'+str(num_bit)+'d}'
    indices = list(range(0,N))
    #print(indices)
    #indici binari
    bin_indices = [format(i,'b') for i in indices]  
    #indici binari su num_bit
    bin_indices = [f'{s}'.format(int(i)) for i in bin_indices]
    #reverse indici binari
    rev_bin_indices = [bi[::-1] for bi in bin_indices]
    #conversione indici interi
    rev_indices = [int(rbi,2) for rbi in rev_bin_indices]
    #inverto il vettore
    #print(rev_indices)
    v = [v[i] for i  in rev_indices]
    return v

def fft(v):
    #numero di punti
    N = len(v)
    #numero butterfly
    n_bf = int(N/2)
    #numero stages
    n_stages = int(math.log2(N))
    #coefficienti W
    coeff = list(range(0,N))
    coeff = [i * int(N/2) for i in coeff] 
    WN = math.e**((-2j*math.pi)/N)
    v = sort_values(v,N)
    #print(v)
    
    for i in range(0,n_stages):
        stage_coeff = [int(c / (2**i)) for c in coeff]
        for j in range(0,n_bf):
            elem_per_cluster = 2**i
            k = (elem_per_cluster*(j//elem_per_cluster))*2 + (j % elem_per_cluster)
            h = elem_per_cluster
            w_coeff_a = stage_coeff[k]%N
            w_coeff_b = stage_coeff[k+h]%N
            Wa = WN**w_coeff_a
            Wb =  WN**w_coeff_b
            butterfly(v,k,h,Wa,Wb)
     #       print(i,j,k,f'coeff a {w_coeff_a}', f'Wa {Wa}',f'coeff b {w_coeff_b}', f'Wb {Wb}')
    #print(v)
    return v

if __name__ == '__main__':
    #vettore degli elementi
    v = [13,36,13,35,13,3,17,4]
    fft_v = fft(v)
    print(v,fft_v)
    