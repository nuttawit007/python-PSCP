"""Week 11"""
import json
def main(list_num: list):
    """Flatten"""
    result = []
    for item in list_num:
        if isinstance(item, list):
            result += main(item)
        else:
            result.append(item)
    result.sort(reverse=True)
    return result
print(main(json.loads(input())))
