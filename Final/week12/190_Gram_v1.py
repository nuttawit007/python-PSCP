"""Week 12"""
def main():
    """Gram_v1"""
    text = input()
    style1 = text.count('WO')
    style2 = text.count('WW')
    style3 = text.count('OW')
    if style1 > 0 or style2 > 0 or style3 > 0:
        all_style = {}
        if style1 > 0:
            all_style["WO"] = style1
        if style2 > 0:
            all_style["WW"] = style2
        if style3 > 0:
            all_style["OW"] = style3
        max_val = max(all_style.values())
        index_maxval, use_text = {}, text
        for key, val in all_style.items():
            if val == max_val:
                use_text = list(use_text.replace(key, "$"))
                index_maxval[key] = use_text.index("$")
                use_text = text
        first_index = min(index_maxval.values())
        for key, val in index_maxval.items():
            if val == first_index:
                print(key)
                print(all_style[key])
main()
