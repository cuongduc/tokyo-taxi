import urllib2
import pprint

SERVICE_PATH = 'http://108.61.200.110:8080/SRAP/webresources/welcome?' \
    'requeststring=1+0+9439+12492+1800+2400+1800+6002+' \
    '857489.46+857489.46'

print(SERVICE_PATH)

pp = pprint.PrettyPrinter(indent=1)

response = urllib2.urlopen(SERVICE_PATH)
result = response.read()

result_set = result.split('\n')
result_set.pop()  # remove last element as it's empty

is_forwarding = True
is_carrying_passenger = False
forward_path = {
    "is_carrying_passenger": False,
    "points": []
}
backward_path = {
    "is_carrying_passenger": False,
    "points": []
}

for line in result_set:
    item = line.split(' ')
    if 'R+' in line:
        is_forwarding = True
        if 'true' in item:
            is_carrying_passenger = True
        else:
            is_carrying_passenger = False
        forward_path["is_carrying_passenger"] = is_carrying_passenger
    elif 'R-' in line:
        is_forwarding = False
        if 'true' in item:
            is_carrying_passenger = True
        else:
            is_carrying_passenger = False
        backward_path["is_carrying_passenger"] = is_carrying_passenger
    else:
        if is_forwarding:
            forward_path["points"].append(item[0])
        else:
            backward_path["points"].append(item[0])

pp.pprint(forward_path)
pp.pprint(backward_path)