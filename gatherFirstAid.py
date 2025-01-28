

def gather_first_aid(split_file, lower_file):
    #Finding first aid section of SDS
    for i in lower_file:
        if('4. first aid measures' in i):
            start_index = lower_file.index(i)
        elif('5. fire fighting measures' in i):
            end_index = lower_file.index(i)
            
    #Full first aid section
    first_aid = lower_file[start_index:end_index]
    
    inhalation = ''
    skin_contact = ''
    eye_contact = ''
    oral = ''
    
    #Getting all sub categories for first aid
    for i in first_aid:
        if('inhalation:' in i):
            inhalation_start = first_aid.index(i)
        elif('skin contact:' in i):
            skin_contact_start = first_aid.index(i)
        elif('eye contact:' in i):
            eye_contact_start = first_aid.index(i)
        elif('ingestion:' in i):
            oral_start = first_aid.index(i)
        elif('ppe for first aiders:' in i):
            oral_end = first_aid.index(i)
    
    #setting variables to their respective categories
    inhalation = ''.join(first_aid[inhalation_start:skin_contact_start])
    skin_contact = ''.join(first_aid[skin_contact_start: eye_contact_start])
    eye_contact = ''.join(first_aid[eye_contact_start:oral_start])
    oral = ''.join(first_aid[oral_start:oral_end])
    
    return [inhalation.split(':',1), skin_contact.split(':',1), eye_contact.split(':',1), oral.split(':',1)]