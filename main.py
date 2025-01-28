from gatherBasicInfo import gather_basic_data
from gatherHazards import gather_hazard_info
from gatherHandlingInfo import gather_handling
from gatherFirstAid import gather_first_aid
from gatherIncompat import gather_incompatablities
from gatherPPE import gatherPPE

filename = './spraywell.txt'

def extract_file(filename):
    #Opens and manipulates the file
    with open(filename, "r", encoding='UTF-8') as file:
        raw_file = file.read()
        raw_lower_file = raw_file.lower()
        split_file = raw_file.split('\n')
        lower_file = raw_lower_file.split('\n')
        
    return [split_file, lower_file]
    

#Begins the data gathering, calls all other functions
def gather_all_info(files):
    split_file = files[0]
    lower_file = files[1]
    basic_data = gather_basic_data([split_file, lower_file])
    hazards = gather_hazard_info([split_file, lower_file])
    handling = gather_handling(split_file, lower_file)
    hazard_data = [hazards[0], hazards[1], hazards[2],hazards[3],hazards[4]]
    first_aid_data = gather_first_aid(split_file, lower_file)
    incompat_data = gather_incompatablities(split_file, lower_file)
    ppe = gatherPPE(split_file, lower_file)
    write_to_file(hazard_data, basic_data, handling, first_aid_data, incompat_data, ppe)

#Writes the data gathered to a file
def write_to_file(hazard_data, basic_data, handling, first_aid, incompat_data, ppe):
    with open('./sds-data.txt' , 'w') as hazard_data_file:
        for i in hazard_data:
            for j in i:
                hazard_data_file.write(j + '\n')
            hazard_data_file.write('\n\n')
    
    with open('./basicinfo.txt', 'w') as basic_data_file:
        for i in basic_data:
            basic_data_file.write(i + '\n')
            basic_data_file.write('\n\n')
        basic_data_file.write(handling + '\n\n')
        basic_data_file.write(incompat_data + '\n\n')
        for i in first_aid:
            basic_data_file.write(i[0] + ':\n' + i[1] + '\n')
    
    with open('./PPE.txt', 'w') as ppefile:
        ppefile.write(ppe)
            
            
file_data = extract_file(filename)
gather_all_info(file_data)
