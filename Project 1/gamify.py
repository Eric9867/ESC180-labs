##################################
## TODO: 
# bored_with_stars logic
# (probably) separating perform_activity into multiple functions


##################################


def initialize():
    '''
    Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it
    '''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars, cur_star, cur_star_activity, cur_star_list
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = False
    cur_star_activity = None
    cur_star_list = []
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = 120

def is_bored_with_stars():
    '''check if the user is bored with stars based on if they have recieved 3 within 2 hours'''
    
    global bored_with_stars, cur_star_list
    global cur_time
    
    for time in cur_star_list:
        if cur_time - time >= 120:
            cur_star_list.remove(time)
        
    if len(cur_star_list) >= 3:
        bored_with_stars = True
    
def star_can_be_taken(activity):
    '''
    Tests if the user has a star 
    '''
    global cur_star, cur_star_activity, bored_with_stars
   
    is_bored_with_stars()
    return cur_star and (cur_star_activity == activity) and not bored_with_stars
    
def perform_activity(activity, duration):
    '''

    '''
    if not activity in ("running", "textbooks", "resting"):
        return None

    global cur_health, cur_hedons, cur_time
    global last_activity, last_activity_duration, last_finished
    global cur_star, cur_star_activity

    # If the user has a star, and are perform the correct activity reward them with 
    # 3 hed / min for the first 10 minutes of the activity. Remove the star after
    if star_can_be_taken(activity):
        if duration >= 10:
            cur_hedons += 30
        else:
            cur_hedons += duration * 3
    cur_star = False 
    cur_star_activity = None

    # the user is tired if they finished running or carrying textbooks 
    # less than 2 hours before the current activity started
    tired = last_finished < 120

    if activity == "running":
        if last_activity == activity:

            ############ LOGIC FAULTY : fails when one calls running more than two times in a row
            # (need to sum the durations before storing in last_activity_duration)
            
            
            # Since the user is tired, lose 2 hed / min
            cur_hedons -= duration * 2

            # Running : 
                # 3 HP / min for up to 180 minutes, 
                # 1 HP / min for every minute over 180 minutes
            # Counting the time that was run previously to this
            if duration + last_activity_duration <= 180:
                cur_health += duration * 3
            elif last_activity_duration > 180:
                cur_health += duration
            else:
                cur_health += (180 - last_activity_duration) * 2 + duration
            last_activity_duration += duration

        else:
            # tired : -2 hed / min
            # not tired : 
                #  2 hed / minute for the first 10 minutes,
                # -2 hed / min for every minute after the first 10
            if tired:
                cur_hedons -= duration * 2
            elif duration <= 10:
                cur_hedons += duration * 2
            else:
                cur_hedons += 40 - 2 * duration

            # Running : 
                # 3 HP / min for up to 180 minutes, 
                # 1 HP / min for every minute over 180 minutes
            if duration <= 180:
                cur_health += duration * 3
            else:
                cur_health += 360 + duration
            last_activity_duration = duration

        last_activity = "running"
        last_finished = 0
        

    elif activity == "textbooks":
        # Carrying textbooks always gives 2 health points per minute.
        cur_health += 2 * duration

        # tired : -2 hed / min
        # not tired : 
            #  1 hed / minute for the first 20 minutes,
            # -1 hed / min for every minute after the first 20
        if tired:
            cur_hedons -= duration * 2
        elif duration <= 20:
            cur_hedons += duration
        else:
            cur_hedons += 40 - duration

        last_activity = "textbooks"
        last_activity_duration = duration
        last_finished = 0

    elif activity == "resting":
        last_finished += duration


    cur_time += duration

def get_cur_hedons():
    global cur_hedons
    return cur_hedons
    
def get_cur_health():
    global cur_health
    return cur_health
    
def offer_star(activity):
    global cur_star, cur_star_activity, cur_time, cur_star_list
    cur_star = True
    cur_star_activity = activity
    cur_star_list.append(cur_time)

def most_fun_activity_minute():
    '''
    Returns the activity that, if performed for 
    the next minute, would give the most hedons.
    '''
    global last_finished, bored_with_stars, cur_star, cur_star_activity
    if not bored_with_stars and cur_star:
        return cur_star_activity
    elif last_finished < 120:
        return "resting"
    else:
        return "running"
    
################################################################################
# These functions are not required, but we recommend 
# that you use them anyway as helper functions

def get_effective_minutes_left_hedons(activity):
    '''
    Return the number of minutes during which the user will 
    get the full amount of hedons for activity activity
    '''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''
    Return the amount of hedons the user would get for 
    performing activity activity for duration minutes
    '''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("textbooks", 50)
    print(get_cur_health())         # 100 = 50 * 2
    print(get_cur_hedons())         # -10 = 20 * 1 + 30 * (-1)
    perform_activity("textbooks", 50)
    print(get_cur_health())         # 200 = 100 + 50 * 2
    print(get_cur_hedons())         # -110 = -10 + 50 * (-2)
    perform_activity()
    
    
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
    
    
