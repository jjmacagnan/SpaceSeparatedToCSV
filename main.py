import os

csv_path = 'csv_files'
txt_path = 'txt_files'

# converts comma separated by single space

files = os.listdir(csv_path)

for filename in files:
    print(filename)

    input_file = open(csv_path + "/" + filename, 'r')

    # remove .csv from filename
    if filename.endswith('.csv'):
        filename = filename[:-4]

    output_file = open(txt_path + "/" + filename + '.txt', 'w')
    # input_file.readline() # skip first line
    for line in input_file:
        output_file.write(" ".join(line.split()).replace(',', ' ') + '\n')
    input_file.close()
    output_file.close()


# converts single spaces with a comma

# files = os.listdir(txt_path)
#
# for filename in files:
#     print(filename)
#
#     input_file = open(txt_path + "/" + filename, 'r')
#
#     # remove .csv from filename
#     if filename.endswith('.txt'):
#         filename = filename[:-4]
#
#     output_file = open(csv_path + "/" + filename + '.csv', 'w')
#     # input_file.readline() # skip first line
#     for line in input_file:
#         output_file.write(" ".join(line.split()).replace(' ', ',') + '\n')
#     input_file.close()
#     output_file.close()






