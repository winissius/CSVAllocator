def merge_dictionaries(dict1, dict2):
    for k, v in dict1.items():
        for k1, v1 in dict2.items():
            if k == k1:
                for values in v1:
                    v.append(values)
    return dict1


