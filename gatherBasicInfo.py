import re

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'september', 'october', 'november', 'december']

def gather_basic_data(files):
    lower_file = files[1]
    split_file = files[0]
    def find_data(category):
        for i in lower_file:
            if(category in i):
                lower_index = lower_file.index(i)
                full_str = split_file[lower_index]
                if(':' in full_str):
                    return full_str.split(':')[1]
                else:
                    return full_str
            
    def find_date(file):
        for i in file:
            if(re.match("[0-9]{2}/[0-9]{2}/[0-9]{4}", i)):
                print(i)
                return i
            else:
                for month in months:
                    if(month in i):
                        date_str = i.split(' ')
                        for j in date_str:
                            if(j == month):
                                month_index = date_str.index(j)
                                if(re.match('\\d', date_str[month_index - 1])):
                                    return date_str[month_index - 1] + ' ' + date_str[month_index] + ' ' + date_str[month_index+1]

    def get_signal_word():
        for i in lower_file:
            if('signal word' in i):
                return lower_file[lower_file.index(i)+1]
    
    product = find_data('product name:')
    supplier = find_data('supplier')
    reccomended_use = find_data('recommended use')
    form = find_data('form:')
    signal_word = get_signal_word()
    date = find_date(lower_file)
    
    return [signal_word, date, product, supplier, reccomended_use, form]


            