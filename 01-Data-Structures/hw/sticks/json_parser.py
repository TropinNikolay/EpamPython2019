def parser(line: str) -> list:
    """ this function does the following:
        1. neglects square brackets
        2. null -> None
        3. returns the list of wines but type(wine) = str
    """
    data = []
    fixed = line[1:-1].replace(' null,', ' None,')
    index = 0
    while index != len(fixed):
        obj, index = take_obj(fixed, index)
        data.append(obj)
    return data


def take_obj(line: str, index: int):
    """ takes next object from the line if exists """
    start_obj = line.find('{"', index)
    end_obj = line.find('"}, {"', index) + 1
    if end_obj == 0:
        if line:
            return line[start_obj:], len(line)
        else:
            return None, 0
    else:
        obj: str = line[start_obj:end_obj + 1]
        index: int = end_obj + 3
        return obj, index


def make_dict(obj: str) -> dict:
    """ gets one wine and making dict type from it """
    dictionary = {}
    lst = obj[2:-1].split('": ')
    key = []
    value = []

    for ind in range(1, len(lst) - 1):
        left = lst[ind].rfind('"')
        key.append(lst[ind][left + 1:])
        value.append(lst[ind][:left - 2])
    key.insert(0, lst[0])
    value.append(lst[len(lst) - 1])

    for ind in range(len(key)):
        if value[ind] == 'None':
            dictionary[key[ind]] = None
        elif '"' in value[ind]:
            dictionary[key[ind]] = value[ind][1:len(value[ind]) - 1].replace('\n', '\r\n')
        else:
            dictionary[key[ind]] = int(value[ind])
    return dictionary


def wine_features(value):
    """ this is for sorting our wines """
    return (-value['price'] if value['price'] is not None else float('-inf'),
            value['variety'] if value['variety'] is not None else '')


def dumper(arr: list) -> bytes:
    """ makes json string from our list of wines """
    json = str(arr).replace('None', 'null').replace('"', r'\"').replace("', '", '", "').replace('", \'', '", \"') \
        .replace("': '", '": "').replace("': ", '": ').replace("'}, ", '"}, ').replace("{'", '{"') \
        .replace(", '", ', "').replace("'}]", '"}]').replace(r': \"', ': "').replace(r'\", "', '", "') \
        .replace(r'\"}, {', '"}, {').replace(r"\'s", "'s").replace('1, "1', "1, '1") \
        .replace(', "9', ", '9").replace(r"\'", "'").encode('ascii', 'backslashreplace').replace(b'\\x', b'\\u00')
    return json


with open('winedata_1.json', encoding='unicode-escape') as wine_1, \
        open('winedata_2.json', encoding='unicode-escape') as wine_2:
    data_1 = parser(wine_1.read())
    data_2 = parser(wine_2.read())

merged_wines = set(data_1 + data_2)
wines = []
for i in merged_wines:
    a = make_dict(i)
    wines.append(a)

wines.sort(key=wine_features)
my_json = dumper(wines)
with open('winedata_full.json', 'wb') as file:
    file.write(my_json)
