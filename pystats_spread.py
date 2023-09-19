import pystats_central as pc
import math

# VARIANCE
def get_variance(data: list):
    """
    Function: get_variance() -> Gets the variance of a list of numbers
    Input: data -> a list of numbers
    Output: variance -> a float representing variance

    Variance is obtained by:
    1. getting the mean of the data
    2. getting the differences between the mean and each datapoint
    3. squaring these differences
    4. getting the mean of the squares differences
    """

    # getting the mean of the data
    mean = pc.get_mean(data)

    # getting the squared differences between the mean and each datapoint
    deviation_squared = [(i - mean) ** 2 for i in data]

    # getting the mean of the squares differences
    variance = pc.get_mean(deviation_squared)

    return variance
# =============================================================================

# STANDARD DEVIATION
def get_stdeviation(data: list):
    """
    Function: get_stdeviation() -> Get's the standard deviation of a list of
    data
    Input: data -> a list of numbers
    Output: stdeviation -> a float representing the standard deviation.

    Standard deviation is derived from the square root of the variance of the
    data
    """

    # getting the variance of the data
    variance = get_variance(data)

    # getting the square root of the data
    stdeviation = math.sqrt(variance)

    return stdeviation
# =============================================================================

# MEAN ABSOLUTE DEVIATION
def get_mad(data: list):
    """
    Function: get_mad() -> gets the Mean Absolute Deviation (MAD)
    Input: data -> a list of numbers
    Output: mad -> a float representing the Mean Absolute Deviation (MAD)

    The Mean Absolute Deviation is obtained by:
    1. Deriving the mean of the data
    2. Getting the difference between the mean and each datapoint
    3. Making these differences absolute
    4. Getting the mean of the absolute differences
    """

    # Deriving the mean
    mean = pc.get_mean(data)

    # Getting the absolute difference between the mean and each datapoint
    absolute_deviation = [abs(i - mean) for i in data]

    # getting the mean of the absolute differences
    mad = pc.get_mean(absolute_deviation)

    return mad
# =============================================================================

# RANGE
def get_range(data: list):
    """
    Function: get_range() -> get's the range of a list of numbers
    Input: data -> a list of numbers
    Output: the_range -> a number representing the range

    The range is obtained by getting the difference between the highest and the
    lowest number in a list of numbers.
    """

    the_range = max(data) - min(data)
    return the_range
# =============================================================================


# TESTS
# Testing the above functions to ensure they work properly

if __name__ == "__main__":
    data_1 = [34500, 30700, 32900, 36000, 34100, 33800, 32500]
    data_2 = [34900, 27500, 31600, 39700, 35300, 33800, 31700]

    print(data_1)
    print(f"Variance: {get_variance(data_1)}")
    print(f"Mean Standard Deviation: {get_stdeviation(data_1)}")
    print(f"Mean Absolute Deviation: {get_mad(data_1)}")
    print(f"Range: {get_range(data_1)}")

    print("\n")

    print(data_2)
    print(f"Variance: {get_variance(data_2)}")
    print(f"Mean Standard Deviation: {get_stdeviation(data_2)}")
    print(f"Mean Absolute Deviation: {get_mad(data_2)}")
    print(f"Range: {get_range(data_2)}")