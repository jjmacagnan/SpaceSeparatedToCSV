input_file = open('texture_spectrum_CBIS-DDSM.csv', 'r')
output_file = open('texture_spectrum_CBIS-DDSM.txt', 'w')
# input_file.readline() # skip first line
for line in input_file:
    output_file.write(" ".join(line.split()).replace(',', ' ') + '\n')
input_file.close()
output_file.close()