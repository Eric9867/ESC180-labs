from gamify import *

if __name__ == "__main__":
    initialize()
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
#  0
#  0
#  140
#  -30
#  260
#  -150
#  590
#  -370
#  820
#  -520
#  1000
#  -670
#  1000
#  -670
#  1000
#  -670
#  running
#  1000
#  -670
#  1330
#  -850
#  1530
#  -1050
#  resting
#  1530
#  -1050
#  running
#  running
#  1950
#  -1290
#  1950
#  -1290
#  2280
#  -1510
#  2500
#  -1670
#  2500
#  -1670