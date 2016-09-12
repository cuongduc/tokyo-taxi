import urllib2


SERVICE_PATH = 'http://108.61.200.110:8080/SRAP/webresources/welcome?requeststring=11596+0+12766+7521+43509+67061+43509+67061+213840.0'

print(SERVICE_PATH)

response = urllib2.urlopen(SERVICE_PATH)
result = response.read()

result_set = result.split('\n')
result_set.pop() # remove last element as it's empty

is_forwarding = True
is_carrying_passenger = False
forward_path = []
backward_path = []

for line in result_set:
    item = line.split(' ')
    if 'R+' in line:
        is_forwarding = True
        if 'true' in item:
            is_carrying_passenger = True
        else:
            is_carrying_passenger = False
    elif 'R-' in line:
        is_forwarding = False
        if 'true' in item:
            is_carrying_passenger = True
        else:
            is_carrying_passenger = False
    else:
        if is_forwarding:
            forward_path.append(item[0])
        else:
            backward_path.append(item[0])

print('Forward', forward_path)
print('Backward', backward_path)
