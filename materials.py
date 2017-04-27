

density = [0.0899, 0.1785, 535., 1848., 2460., 2260., 1.251, 1.429, 1.696, 0.900, 968., 1738., 2.7e3, 2330., 1823., 1960., 3.214, 1.784, 856., 1550., 2985., 4507., 6110., 7190., 7470., 7874., 8.9e3, 8908., 8960., 7140., 5904., 5323., 5727., 4819., 3120., 3.75, 1532., 2630., 4472., 6511., 8570., 10280., 1.15e4, 12370., 12450., 12023., 10490., 8650., 7310., 7310., 6697., 6240., 4940., 5.9, 1879., 3510., 6146., 6689., 6640., 7010., 7264., 7353., 5244., 7901., 8219., 8551., 8795., 9066., 9320., 6570., 9841., 13310., 16650., 19250., 21020., 2.259e4, 2.256e4, 21450., 1.93e4, 13534., 11850., 11340., 9780., 9196., None, 9.73, None, 5.0e3, 10070., 11724., 15370., 19050., 20450., 19816., 1.367e4, 13510., 14780., 1.51e4]

atomic_mass = [1.00794, 4.002602, 6.941, 9.012182, 10.811, 12.0107, 14.0067, 15.9994, 18.9984032, 20.1791, 22.98976928, 24.3050, 26.9815386, 28.0855, 30.973762, 32.065, 35.453, 39.948, 39.0983, 40.078, 44.955912, 47.867, 50.9415, 51.9961, 54.938045, 55.845, 58.933195, 58.6934, 63.546, 65.38, 69.723, 72.63, 74.92160, 78.96, 79.904, 83.798, 85.4678, 87.62, 88.90585, 91.224, 92.90638, 95.96, 98., 101.07, 102.90550, 106.42, 107.8682, 112.411, 114.818, 118.710, 121.760, 127.60, 126.90447, 131.293, 132.9054519, 137.327, 138.90547, 140.116, 140.90765, 144.242, 145., 150.36, 151.964, 157.25, 158.92535, 162.500, 164.93032, 167.259, 168.93421, 173.054, 174.9668, 178.49, 180.94788, 183.84, 186.207, 190.23, 192.217, 195.084, 196.966569, 200.59, 204.3833, 207.2, 208.98040, 209., 210., 222., 223., 226., 227., 232.03806, 231.03586, 238.02891, 237., 244., 243., 247., 247., 251.]

def number_density(Z):
    i = Z-1
    return density[i] / 1000 / atomic_mass[i]

def get_properties(Z):
    props = {'Z': Z, 'N': number_density(Z)}
    return props