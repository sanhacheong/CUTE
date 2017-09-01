import numpy as np



input_file_name = "./data/galaxies_DR9_CMASS_South_ascii.dat"

ra, dec, z, weight_fkp, weight_noz, weight_cp, weight_sdc = np.loadtxt(input_file_name, delimiter='\t', unpack=True, skiprows=1)
weight = weight_fkp * weight_sdc * (weight_noz + weight_cp - 1)

output_file_name = ".".join(input_file_name.split('.')[:-1]) + "_CUTE.dat"

np.savetxt(output_file_name, np.column_stack([ra, dec, z, weight]), delimiter='\t', fmt='%.8f')