"""Week 13"""
def show_gost(real_gost):
    """show_gost"""
    if len(real_gost) > 0:
        for gost in sorted(real_gost):
            print(gost)
    else:
        print("Not yet discovered")

def main():
    """Phasmophobia"""
    equipment = {'EMF Level 5' : {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'},\
            'Ghost Writing' : {'Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'},\
            'Fingerprints' : {'Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'},\
            'Spirit Box' : {'Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'},\
            'Freezing Temperatures' : {'Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'},\
            'Ghost Orb' : {'Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei'},\
            'No evidence' : "No"}
    evidence = [input() for _ in range(3)]
    gost1 = equipment[evidence[0]]
    gost2 = equipment[evidence[1]]
    gost3 = equipment[evidence[2]]
    real_gost = set()
    if gost1 == "No" and gost2 == "No" and gost3 == "No":
        print("Not yet discovered")
    elif gost1 == "No" and gost2 == "No":
        real_gost = gost3
        show_gost(real_gost)
    elif gost1 == "No" and gost3 == "No":
        real_gost = gost2
        show_gost(real_gost)
    elif gost2 == "No" and gost3 == "No":
        real_gost = gost1
        show_gost(real_gost)
    elif gost1 == "No":
        real_gost = gost2.intersection(gost3)
        show_gost(real_gost)
    elif gost2 == "No":
        real_gost = gost1.intersection(gost3)
        show_gost(real_gost)
    elif gost3 == "No":
        real_gost = gost1.intersection(gost2)
        show_gost(real_gost)
    else:
        real_gost = sorted(gost1.intersection(gost2, gost3))
        show_gost(real_gost)
main()
