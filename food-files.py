# import json
import json
# takes 1 file and returns a list of the file contents
def open_file(filename):
    with open(filename) as file:
        next(file)
        lines = file.readlines()
    return lines
# takes 1 messy list and returns a cleaned list
def clean(lst):
    cleaned_list = []
    for i in range(0, len(lst)):
        # strip and make lowercase
        lst[i] = lst[i].strip().lower()
        # check for missing
        if lst[i] == '':
            continue
        # check for duplicate entries other than yes and no
        elif lst.count(lst[i]) > 1 and lst[i] != 'yes' and lst[i] != 'no':
            continue
        # check for invalid entries
        elif lst[i].isalpha() == False:
            if ' ' in lst[i] or ':' in lst[i]:
                cleaned_list.append(lst[i])
            else:   
                continue
        # if all's good
        else:
            cleaned_list.append(lst[i])
    return cleaned_list

# takes 1 list of 4 lists and returns 1 dictionary
def dictionary(lst):
    final_lst = []
    for i in range(0, len(lst[0])):
        d = {}
        d['food'] = lst[0][i]
        d['highfiber'] = lst[1][i]
        d['low-glycemic'] = lst[2][i]
        d['lowfat'] = lst[3][i]
        final_lst.append(d)
    return final_lst

# save list of dictionaries as json
def save(lst):
    json_object = json.dumps(lst)
    with open('foods_complete.json', 'w') as outfile:
        outfile.write(json_object)

#--------------Execution--------------------------#

# open files and read into lists
food_messy = open_file('foods.txt')
highfiber_messy = open_file('highfiber.txt')
lowfat_messy = open_file('lowfat.txt')
low_glycemic_index_messy = open_file('low-glycemic-index.txt')
# clean lists
food_clean = clean(food_messy)
highfiber_clean = clean(highfiber_messy)
lowfat_clean = clean(lowfat_messy)
low_glycemic_index_clean = clean(low_glycemic_index_messy)
# create list of cleaned lists, order matters here!
lsts = [food_clean, highfiber_clean, lowfat_clean, low_glycemic_index_clean]
# create dictionaries
final_lst = dictionary(lsts)
# save as json
save(final_lst)


