"""MoreEntryway"""
# def main():
#     """MoreEntryway"""
#     print("Output_1")
#     print("Output_2")
#     print("Output_3")
#     print("Output_4")
#     print("Output_5")
#     print("Output_6")
#     print("Output_7")
#     print("Output_8")
#     print("Output_9")
#     print("Output_10")
#     print("Output_11")
#     print("Output_12")
#     print("Output_13")
#     print("Output_14")
#     print("Output_15")
#     print("Output_16")
#     print("Output_17")
#     print("Output_18")
#     print("Output_19")
#     print("Output_20")
# main()

#recursive dunction
def main(num):
    if num > 21:
        return
    else:
        print("Output_"+str(num))
        num+=1
        main(num)
main(1)