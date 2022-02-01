import numpy as np

def decision(t, randnum, size, c2b, speed, direction, dist, mean, std, m, weights):
    
    # t = time 
    # randnum is a function defined in main
    # size, c2b (contrast to background), speed, direction and dist (distance) are "factors" that will influence the yes/no decisions of clusters. These are the properties of the prey.
    # mean represents the middle, mean, and median of the normal distribution of the thresholds in a cluster. Std is the standard deviation of this thresholds normal distribution. 
    # m = a vector with the distribution of the number of units allocated for each factor
    # weights = these are the weights of the factors - how much they will influence the final decision
    
    prey = {'size' : [size],
            'c2b' : [c2b],
            'speed' : [speed],
            'direction' : [direction],
            'dist' : [dist]
            }
    
    
    # This is the overall, real quality of the prey
    
    overall_quality = np.zeros(len(t))  
    overall_quality[0] = np.mean([prey['size'][0], prey['c2b'][0], prey['speed'][0], prey['direction'][0], prey['dist'][0]])  # Defining the first one to enable the following for loop to start
    
    
    # Generating random different conditions for each time step, in order to simulate a real world situation in which the prey would change their characteristics over time. 
    
    for i in range(1, len(overall_quality)):
        
        prey['size'].append(prey['size'][i - 1] + randnum())
        prey['c2b'].append(prey['c2b'][i - 1] + randnum())
        prey['speed'].append(prey['speed'][i - 1] + randnum())
        prey['direction'].append(prey['direction'][i - 1] + randnum())
        prey['dist'].append(prey['dist'][i - 1] + randnum())
        factors_now = [prey['size'][i], prey['c2b'][i], prey['speed'][i], prey['direction'][i], prey['dist'][i]]
        overall_quality[i] = np.mean(factors_now)
    
    
    # Options[i] are the perceived qualities, and decision[i] is the final decision about that particular option
    
    options = np.zeros(len(overall_quality))
    decision = np.zeros(len(options))
    
    for i in range(len(overall_quality)):

        options_now = [cluster(prey['size'][i], weights[0], m[0], mean[0], std[0]), cluster(prey['c2b'][i], weights[1], m[1], mean[1], std[1]), cluster(prey['speed'][i], weights[2], m[2], mean[2], std[2]), cluster(prey['direction'][i], weights[3], m[3], mean[3], std[3]), cluster(prey['dist'][i], weights[4], m[4], mean[4], std[4])]
        options[i] = np.mean(options_now)
        
    
    # Found out that many times, options is filled with a lot of values of 1. Made conditions to avoid awkwardness. 
    
    if max(options) > 1:
        for k in range(len(decision)):
            if options[k] > 1:
                decision[k] += 1

    elif max(options) == 1:
        for k in range(len(decision)):
            if decision[k] == 1:
                decision[k] += options[k]
    
    return decision, overall_quality, options
    



# The decision-making machinery for each time step. Assigning a normally distributed array of thresholds to asses the quality of "factor" 

def cluster(factor, weight, mn, mean, std):
    thresholds = np.random.normal(mean, std, mn)
    yes = 0
    no = 0
    for i in range(len(thresholds)):
        if thresholds[i] < factor:
            yes += 1
        elif thresholds[i] > factor: 
            no += 1
        else:
            pass
    if yes < no:
        return 0 
    else:
        return yes * weight
        

    
    