input_file = open('database.txt', 'r')
output_file = open('mias_database.csv', 'w')
input_file.readline() # skip first line
for line in input_file:
    output_file.write(" ".join(line.split()).replace(' ', ',') + '\n')
input_file.close()
output_file.close()