"""
This is module_0 project from DST25 SkillFactory
Task: 
    find the random number from 1 to 100 in a minimum number of tries. 
"""


"""
Modification:
        the range is variable and from range_min to range_max
"""


"""all imported libraries are here"""
import numpy as np
"""---------------------------------------"""


def score_game(game_core,range_min=1,range_max=100,number_iterations=1000):
    '''Run the game number_iterations times 
        to find the mean number of steps (iterations) to reach the goal = find the given number'''
    
    count_ls = [] #here the number of requared number of steps is saved
    #np.random.seed(2) #To achieve reproducibility, you can uncomment it
    random_array = np.random.randint(range_min,range_max+1, size=number_iterations)
    for number in random_array:
        count_ls.append(game_core(number,range_min,range_max))
    
    score = round(np.mean(count_ls),2)
    stdev = round(np.std(count_ls),2)
    max_tries=max(count_ls)
    min_tries=min(count_ls)
    
    print(f"My script finds any number in the range [{range_min},{range_max}] in average in {score} tries")
    print(f"with the standard deviation of {stdev}")
    print(f"The minimum and maximum number of tries was min={min_tries} and max={max_tries}")
    print(f"The number of iterations was {number_iterations}")    
    
    return(score)


def mean_range(range_min,range_max):
    return (range_max+range_min)//2


def game_core_half_range(number,range_min=1,range_max=100):
    """Algorithm to find the number in the given range in a minimum number  of steps:
        always guess the predict number in the middle between min and max range values
        if predict is too small, then our range is from predict+1 to max range value
        if predict is too big, then our new range is from min range value to predict-1
    """
    
    count = 1    
    predict = mean_range(range_min,range_max)
    max_count = range_max
    
    while number != predict and count<max_count:
        count+=1
        if number > predict:             
            range_min=predict+1        
        elif number < predict: 
            range_max=predict-1 
        predict = mean_range(range_min,range_max)
        
    return(count)

#here the program starts
score_game(game_core_half_range,range_min=1,range_max=100,number_iterations=2000)

