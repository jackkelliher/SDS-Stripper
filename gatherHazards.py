import re
import gatherBasicInfo


#Gathers all data regarding hazards assuming the sds is in the correct format, hazard classificaiton needs to begin with the hazard code
def gather_hazard_info(files):
    split_file = files[0]
    lower_file = files[1]
    #Strips items that do not begin with codes
    def strip_items (items):
        #Holds items that fit the regex specs
        stripped_items = []
        for i in items:
            i_index = split_file.index(i)
            
            code = i[:4]
            #Tests if the first 4 charicters are codes
            if( re.match(('[A-Z](\\d)(\\d)(\\d)'), code)):
                code_length = 4
                all_code = True
                extra_code = i[code_length:code_length + 5]

                #While loop to capture all codes when mutliple exist on a classificaition
                while(all_code):

                    extra_code = i[code_length:code_length + 5] #Getting next 5 charicters in classification (e.g. +H319)

                    if(re.match(('\\+[A-Z](\\d)(\\d)(\\d)'), extra_code)): #If matching '+[LETTER][Digit][digit][digit]'
                        code_length += 5 #Continue loop until the extra code does not match
                    else:
                        all_code = False #Stops the loop
                line = remaning_line(i_index) #Tests that all data is present
                #if remaning line function returned true
                if(line[0]):
                    i = i + line[1]
                stripped_items.append(i[:code_length] + '!' + i[code_length:]) 

                
            else:
                print(i + ' does not fit the pattern necissary')
        return stripped_items
    
    #Tests the line below to catch sentaces streching lines
    def remaning_line(index):
        next_line = split_file[index+1]
        
        #Tests if the next line begins with a lowercase letter
        if(re.match(('[a-z]'), next_line)):
            #if this is true, return true and the next line
            return [True, next_line]
        else:
            #else return false
            return [False]

    def find_category(category):
        for i in lower_file:
            if(i == category):
                print('Found category: ' +category)
                return lower_file.index(i)
            
        return ''
        
        #Finding the hazard statements in the file

    #Finds each category index

    try:
        hazard_index = find_category("hazard statement")
        prevention_index = find_category('prevention precautionary statements')
        response_index = find_category('response precautionary statements')
        storage_index = find_category('storage precautionary statements')
        disposal_index = find_category('disposal precautionary statement')
        goods_index = find_category('dangerous good classification')
    except TypeError as err:
        print(err.args)
        raise NameError('Cannot find hazard categories. This SDS may not be compatable with SDS Stripper or the hazard section may not exist.')
        return 'ERROR'

    try:
        #Using the indexes to split the string to gather the data contained in the category
        hazards = split_file[hazard_index + 1: prevention_index]
        prevention = split_file[prevention_index + 1: response_index]
        response = split_file[response_index + 1: storage_index]
        storage = split_file[storage_index + 1: disposal_index]
        disposal = split_file[disposal_index: goods_index]
    except:
        print("An error occured while gathering hazard classifications, no hazard classifications will be present once the script is complete.")
        return 'ERROR'
    #Stripping sentances
    hazards = strip_items(hazards)
    prevention = strip_items(prevention)
    response = strip_items(response)
    storage = strip_items(storage)
    disposal = strip_items(disposal)
    #Returns all data gathered
    return [hazards, prevention, response, storage, disposal]