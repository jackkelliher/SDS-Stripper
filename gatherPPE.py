

def gatherPPE(split_file, lower_file):
    for i in lower_file:
        if('8. exposure controls / personal protection' in i):
            start_index = lower_file.index(i)
        elif('9. physical and chemical properties' in i):
            end_index = lower_file.index(i)
    
    section = split_file[start_index:end_index]
    
    for i in section:
        if ('personal protection equipment' in i.lower()):
            section = split_file[lower_file.index(i.lower()):end_index]
            print("FOUND")
    
    return '\n'.join(section)