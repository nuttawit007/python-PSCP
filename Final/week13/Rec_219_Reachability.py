import json
def main():
    """test json"""
    x = input().replace("\'", "\"")
    y = json.loads(x)
    print(type(y))
main()