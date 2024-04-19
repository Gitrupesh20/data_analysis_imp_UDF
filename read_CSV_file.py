def read_CSV_file(path, is_header = True, header_item = None):
  '''
  description:
  this function take path of data file and it read the file and extract data from 
  file and create and return list of  dictionary header as key and values as value

  read_CSV_file(str path, is_header = false, header_item = None)
  default value of header_item is none and is_header is True
  '''
  #read file's data
  with open(path) as f:
    d = f.readlines()
  
  #parse_header into list of string
  if  is_header and header_item == None:
    header = d[0].strip().split(",")


  if header_item != None:
    header = header_item


  result = []
  for ele in d[1:]:

 #parse value line into float and also handlle empty value
    value = []
    for item in ele.strip().split(","):
      if item == "":
        value.append(None)
      else:
        value.append(float(item))
  #create a dictionary items or data available in file where header is key and 
  # and value is value 
    result.append(dict(zip(header, value)))

  return result


