"""Week 7"""
def ping():
    """[Midterm 2020] Ping"""
    link = input()
    space = input("\n") #เว้น1บรรทัดก่อนใส่ Input
    # หา IP address
    if "www" in link:
        space[space.find(" ")+1:space.find(" ")+2].isalpha()
        ipaddress = space[space.find("[")+1:space.find("]")]
    else:
        ipaddress = space[space.find("ping ")+5:]
    # หาเวลาจาก 4 input() 
    # time = [reply[reply.find("time")+5:reply.find("ms")] if "time" in (reply := input()) else 0 for _ in range(4)]
    time = [reply[reply.find("time")+5:reply.find("ms")] for _ in range(4) if "time" and " Reply"in (reply := input())]
    int_time = [int(i) for i in time] #แปลงเวลาที่หา str >> int
    # min max avg
    minimum = min(int_time)
    maximum = max(int_time)
    avg = 0
    for num in int_time:
        avg += num
    # win lose
    win = len(int_time)
    lost = 4 - len(int_time)
    per_lost = str(lost * 25) + "%"
    print("Ping statistics for %s:" % (ipaddress))
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss)," % (win, lost, per_lost))
    if win != 0 and int_time[0] != 0:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" % (minimum, maximum, int(avg/4)))
ping()

# หาที่ไม่บอก ping
# ping[ping.find("[")+1:ping.find("]")]

#check ping ทืี่ไม่มี www
#ping[ping.find(" ")+1:ping.find(" ")+2]