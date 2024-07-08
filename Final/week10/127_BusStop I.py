"""Week 10""" #**
def main():
    """BusStop I"""
    amount = int(input())
    count = int(input())
    passenger_string = []
    passenger_integer = []
    at_home = 0
    for _ in range(count):
        bus = input().split()
        passenger_string.append(bus)
    passenger_string.sort(key=lambda i: int(i[0]))
    for i in passenger_string:
        stage_bus_stop = int(i[0])
        if len(passenger_integer) != 0:
            passenger_integer2 = passenger_integer.copy()
            for arrive in passenger_integer:
                if arrive == stage_bus_stop:
                    passenger_integer2.remove(arrive)
                    at_home += 1
            passenger_integer = passenger_integer2
        for j in range(1, len(i)):
            if len(passenger_integer) == amount:
                break
            if stage_bus_stop < int(i[j]):
                passenger_integer.append(int(i[j]))
    print(at_home)
main()

def main(quan, bus_stop):
    """BusStop I"""
    pass_in_bus, goal = [], 0
    for _ in range(1, bus_stop+1):
        passenger = input().split()
        # รับผู้โดยสาร set1
        if _ == 1:
            can_go = passenger[1:quan+1]
            pass_in_bus = can_go
            continue
        # พาผู้โดยสารลง
        if passenger[0] in pass_in_bus:
            goal += pass_in_bus.count(passenger[0])
            # เอาผู้โดยสารออก
            left_passenger = [people for people in pass_in_bus if people != passenger[0]]
            pass_in_bus = left_passenger
        # รับผู้โดยสารเพิ่ม กรณีคนยังไม่เต็ม
        if len(pass_in_bus) != quan:
            can_go = passenger[1:(len(can_go)-quan)+1]
            pass_in_bus = can_go
    print(goal)
main(int(input()), int(input()))



def bus_stop(passengers, stop): #009
    """Count the passengers that get to desired stop"""
    passengers_now, all_stop = [], []
    passengers_count = 0
    for _ in range(stop):
        get_stop = str(input()).split()
        get_stop = list(map(int, get_stop))
        all_stop.append([get_stop[0], get_stop[1:]])
    all_stop.sort()
    for stop_now in all_stop:
        if stop_now[0] in passengers_now:
            for _ in range(passengers_now.count(stop_now[0])):
                passengers_now.remove(stop_now[0])
                passengers_count += 1
        for people in stop_now[1]:
            bus_size = len(passengers_now)
            if bus_size < passengers and people > stop_now[0]:
                passengers_now.append(people)
            elif bus_size >= passengers:
                break
    print(passengers_count)
bus_stop(int(input()), int(input()))

def busstop(cap: int, route: int): #117 aom
    """ambussingg"""
    allstation = sorted([input().split() for _ in range(route)], key=lambda x: int(x[0]))
    bus = {str(k+1):0 for k in range(route)}
    passed = []
    result = 0
    for i in range(route):
        rows = allstation[i]
        result += bus[rows[0]]
        bus[rows[0]] = 0
        for each in rows[1:]:
            if sum(bus.values()) == cap:
                break
            if each not in passed:
                bus[each] += 1
        passed.append(rows[0])
    result += bus[str(route)]
    print(result)
busstop(int(input()), int(input()))