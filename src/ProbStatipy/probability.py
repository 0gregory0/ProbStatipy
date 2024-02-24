# PROBABILITY

def probability(successful_observations, total_observations):

    """
    Function: probability() -> Given the number of observations and the number of successes, this function derives the probability of a successful observation.
    Arguments: successful_observations, total_observations -> both of these arguments should be numbers (ints or floats)
    Output: probability -> the probability of success which ranges from 0 to 1 (inclusive)
    """

    probability = successful_observations/total_observations

    if probability > 1:
        raise ValueError("Probabilities cannot be greater than one.")
    
    elif probability < 0:
        raise ValueError("Probabilities cannot be less than zero (negative)")
    
    else:
        return probability

# ===========================================================================================================

# TESTS
if __name__ == "__main__":
    print(probability(3, 10))
    print(probability(50, 1000))
    # print(probability(10, 1))
    # print(probability(-4, 20))