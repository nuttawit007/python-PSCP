"""Week 6"""
def scv(time, s_con, m_con, h_con):
    """SecondConverter"""
    second = time
    minute = second//s_con
    second = second%s_con
    hour = minute//m_con
    minute = minute%m_con
    day = hour//h_con
    if day > 0:
        hour -= day*h_con
    print("%d:%d:%d" % (hour, minute, second))
scv(int(input()), int(input()), int(input()), int(input()))
