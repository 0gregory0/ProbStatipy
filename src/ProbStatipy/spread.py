import central
import math

# VARIANCE
def variance(data: list):
    """
    Function: variance() -> Gets the variance of a list of numbers
    Input: data -> a list of numbers
    Output: variance -> a float representing variance

    Variance is obtained by:
    1. getting the mean of the data
    2. getting the differences between the mean and each datapoint
    3. squaring these differences
    4. getting the mean of the squares differences
    """

    # getting the mean of the data
    mean = central.mean(data)

    # getting the squared differences between the mean and each datapoint
    deviation_squared = [(i - mean) ** 2 for i in data]

    # getting the mean of the squares differences
    variance = central.mean(deviation_squared)

    return variance
# =============================================================================

# STANDARD DEVIATION
def stdeviation(data: list):
    """
    Function: stdeviation() -> Get's the standard deviation of a list of
    data
    Input: data -> a list of numbers
    Output: stdeviation -> a float representing the standard deviation.

    Standard deviation is derived from the square root of the variance of the
    data
    """

    # getting the variance of the data
    var_of_data = variance(data)

    # getting the square root of the data
    stdeviation = math.sqrt(var_of_data)

    return stdeviation
# =============================================================================

# MEAN ABSOLUTE DEVIATION
def mad(data: list):
    """
    Function: mad() -> gets the Mean Absolute Deviation (MAD)
    Input: data -> a list of numbers
    Output: mad -> a float representing the Mean Absolute Deviation (MAD)

    The Mean Absolute Deviation is obtained by:
    1. Deriving the mean of the data
    2. Getting the difference between the mean and each datapoint
    3. Making these differences absolute
    4. Getting the mean of the absolute differences
    """

    # Deriving the mean
    mean = central.mean(data)

    # Getting the absolute difference between the mean and each datapoint
    absolute_deviation = [abs(i - mean) for i in data]

    # getting the mean of the absolute differences
    mad = central.mean(absolute_deviation)

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

# INTERQUARTILE RANGE
def iqr(data: list):
    """
    Function: iqr() -> get's the interquartile range for a list of numbers
    Input: data -> a list of numbers
    Output: iqr -> a number representing the interquartile range
    """

    # sort the data
    data = sorted(data)

    # find the q1th value [1/4 * (n+1)]
    q1th_value = (1/4)*(len(data) + 1)

    # let q1 be the q1th value if the q1th value is whole
    if q1th_value.is_integer() :
        q1 = data[q1th_value - 1] # -1 because of zero based indexing
    
    # and carry out linear interpolation to find q1 if it is not a whole number
    else:
        q1 = data[int(q1th_value) - 1] + ((q1th_value - int(q1th_value))*((data[int(q1th_value)]) - (data[int(q1th_value) - 1])))

    # find the q3rd value [3/4 * (n+1)]
    q3rd_value = (3/4)*(len(data) + 1)

    # let q3 be the q3rd value if the q3rd value is whole
    if q3rd_value.is_integer():
        q3 = data[q3rd_value - 1] # -1 because of zero-based indexing

    # if the q3rd value is not a whole number, carry out linear interpolation
    else:
        q3 = data[int(q3rd_value) - 1] + ((q3rd_value - int(q3rd_value))*((data[int(q3rd_value)]) - (data[int(q3rd_value) - 1])))

    # finally, to get IQR, we get the difference between q3 and q1
    iqr = q3-q1
    return iqr

iqr([7, 1, 3, 5, 9, 6, 8, 2])


# TESTS
# Testing the above functions to ensure they work properly

if __name__ == "__main__":
    data_1 = [34500, 30700, 32900, 36000, 34100, 33800, 32500]
    data_2 = [34900, 27500, 31600, 39700, 35300, 33800, 31700]
    data_3 = [7, 1, 3, 5, 9, 8, 6, 2]
    data_4 = [-19.8, -13.8, 12.0, 13.6, 14.3, 25.5, 36.3, 43.6]

    print(data_1)
    print(f"Variance: {variance(data_1)}")
    print(f"Mean Standard Deviation: {stdeviation(data_1)}")
    print(f"Mean Absolute Deviation: {mad(data_1)}")
    print(f"Range: {get_range(data_1)}")

    print("\n")

    print(data_2)
    print(f"Variance: {variance(data_2)}")
    print(f"Mean Standard Deviation: {stdeviation(data_2)}")
    print(f"Mean Absolute Deviation: {mad(data_2)}")
    print(f"Range: {get_range(data_2)}")

    print("\n")

    print(data_3)
    print(f"IQR: {iqr(data_3)}")

    print("\n")

    print(data_4)
    print(f"IQR: {iqr(data_4)}")