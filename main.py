input_file = open('csv_flies/zernike.csv', 'r')
output_file = open('txt_files/zernike.txt', 'w')
# input_file.readline() # skip first line
for line in input_file:
    output_file.write(" ".join(line.split()).replace(',', ' ') + '\n')
input_file.close()
output_file.close()