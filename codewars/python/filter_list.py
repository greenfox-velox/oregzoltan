def filter_list(l):
  'return a new list with the strings filtered out'
  filtered_list = []
  for i in l:
      if type(i) == int:
          filtered_list.append(i)
  return filtered_list
