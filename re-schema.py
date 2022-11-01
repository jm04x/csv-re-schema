import os.path


# New schema: name, mass, diameter ... .. ..    

def reschema():

    while True:
        file_path = input('Enter file path: ')
        if os.path.exists(file_path):
            break
        else:
            print('Invalid file path.')


    with open(file_path, 'r') as input_file:
        # Assigne first line to headers.
        headers = input_file.readline()
        
        # Assign the rest of data to variable
        file_data = input_file.readlines()


    # Split each header into a list
    for h in headers:
        header_list = headers.split(',')


    # Remove 0th value as it was NULL and remove \n from last index.
    del header_list[0]
    header_list[-1] = header_list[-1].strip()


    # Create dictionary for each header and assign an empty list.
    header_dict = {}
    for h in header_list:
        header_dict[h] = []


    # Initiate a labels array which will store each stats label e.g. mass, diameter.
    # User input is inputted to determine the label for the item which holds these stats e.g. Name
    labels = [] 
    labels.append(input('Enter label: '))


    # Iterate through each line of data and split it into an array,
    # append each index of data to corrosponding header array in header dict.
    # ... Also append labels array with each stat label.
    for l in file_data:
        l_split = l.split(',')
        l_split[-1] = l_split[-1].strip()

        labels.append(l_split[0])
        
        for i, h in enumerate(header_dict):
            header_dict[h].append(l_split[i+1]) # <- i+1 as [0]th value is labels.


    # Write new schema to file.
    with open('output_file.csv', 'w') as output_file:
        for l in labels:
            output_file.writelines(l + ',')

        output_file.write('\n')    

        for k in header_dict:
            output_file.writelines(k + ',')
            for i in header_dict[k]:
                output_file.writelines(i + ',')
            output_file.write('\n')


if __name__ == '__main__':
    reschema()
        



        
        

    
    
    


    







        




