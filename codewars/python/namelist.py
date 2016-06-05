def namelist(names):
    if names == []:
        return ''
    name_list = []
    name_str = ''
    for i in names:
        name_list.append(i['name'])
    if len(name_list) > 1:
        name_str = ', '.join(name_list[0:-1]) + ' & ' + name_list[-1]
    else:
        name_str = name_list[0]
    return name_str

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
# returns 'Bart, Lisa & Maggie'
