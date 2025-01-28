

def gather_incompatablities(split_file, lower_file):
    for i in lower_file:
        if('10. stability and reactivity' in i):
            start_index = lower_file.index(i)
        elif('11. toxicological information' in i):
            end_index = lower_file.index(i)
            
    section = lower_file[start_index:end_index]
    
    for i in section:
        if('incompatible materials' in i):
            incompat_section = lower_file.index(i)
            print(incompat_section)
            
    return split_file[incompat_section]