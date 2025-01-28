#Function to simply gather the handling section of SDS files, searches for the words 'handling:' and 'storage' to get the index of the handling section

def gather_handling(split_file, lower_file):
    start_index = -1
    end_index = -1
    for i in lower_file:
        if('handling:' in i):
            start_index = lower_file.index(i)
        elif('storage:' in i):
            end_index = lower_file.index(i)
    
    if(start_index == -1 or end_index == -1) :
        print("Error in gather_handling function, cannot find handling section")
    
    handling_data = ''.join(split_file[start_index:end_index])
    return handling_data
    
            
