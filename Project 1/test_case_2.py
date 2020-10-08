from gamify import *

if __name__ == "__main__":
    initialize()
    # offer_star("textbooks")
    # perform_activity("textbooks", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 70)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 130)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("textbooks")
    # print(most_fun_activity_minute())
    
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("textbooks")
    offer_star("textbooks")
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("textbooks")
    perform_activity("textbooks", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    
    # perform_activity("textbooks", 50)
    # print(get_cur_health())         # 100 = 50 * 2
    # print(get_cur_hedons())         # -10 = 20 * 1 + 30 * (-1)
    # perform_activity("textbooks", 50)
    # print(get_cur_health())         # 200 = 100 + 50 * 2
    # print(get_cur_hedons())         # -110 = -10 + 50 * (-2)
    # perform_activity()
    
    # offer_star("textbooks")
    # perform_activity("running", 60)
    # print(get_cur_hedons())         #  -80 = 10 * (2) - 50 * 2
    # print(get_cur_health())         #  180 = 3 * 60
    # offer_star('running')
    # perform_activity('running', 5)
    # print(get_cur_hedons())         #  -75 = -80 + 5 * (3 - 2)
    # print(get_cur_health())         #  195 = 180 + 3 * 5
    # perform_activity('running', 2)  
    # print(get_cur_hedons())         #  -79 = -75 + 2 * (- 2)
    # print(get_cur_health())         #  201 = 195 + 3 * 2
    # offer_star('textbooks')
    # perform_activity("textbooks", 40) 
    # print(get_cur_hedons())         # -119 = -79 + 40 * (-1)
    # print(get_cur_health())         #  281 = 201 + 2 * 40
 
 
    # offer_star("running")
    # perform_activity("running", 60)
    # print(get_cur_hedons())         #  -50 = 10 * (3 + 2) - 50 * 2
    # print(get_cur_health())         #  180 = 3 * 60
    # offer_star("running")
    # perform_activity("running", 59)
    # print(get_cur_hedons())         # -138 = -50 + 1 * 10 - 49 * -2 
    # print(get_cur_health())         #  357 = 180 + 3 * 59
    # offer_star("running")
    # perform_activity("running", 60)
    # print(get_cur_hedons())         # -258 = -138 - 2 * 60
    # print(get_cur_health())         #  537 = 357 + 3 * 60

    # perform_activity("running", 30)
    # print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    # print(get_cur_health()) # 90 = 30 * 3
    # print(most_fun_activity_minute()) #resting
    # perform_activity("resting", 30)
    # offer_star("running")
    # print(most_fun_activity_minute()) # running
    # perform_activity("textbooks", 30)
    # print(get_cur_health()) # 150 = 90 + 30*2
    # print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
    # offer_star("running")
    # perform_activity("running", 20)
    # print(get_cur_health()) # 210 = 150 + 20 * 3
    # print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    # perform_activity("running", 170)
    # print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    # print(get_cur_hedons()) # -430 = -90 + 170 * (-2)