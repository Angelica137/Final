trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    if len(us_num) == 1:
        for key in trans:
            if key == us_num:
                return trans[key]
    if len(us_num) == 2:
        if us_num[0] == '1':
            for key in trans:
                if key == us_num[1]:
                    return (trans['10'] + " " + trans[key])
        elif us_num[1] == '0':
            for key in trans:
                if key == us_num[0]:
                    return (trans[key] + " " + trans['10'])
        else:
            translation = []
            for char in range(len(us_num)):
                for key in trans:
                    if key == us_num[char]:
                        translation.append(trans[key])
        translation.insert(1, 'shi')
        return " ".join(translation)
    return None
