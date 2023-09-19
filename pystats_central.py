# ARITHMETIC MEAN
def mean(data: list):
    
    """
    Function: mean() -> Gets the mean of a list of numbers.
    Input: data -> a list stored as "data".
    Output: mean -> a float denoting the mean or average stored as "mean".
    
    The mean is obtained by dividing the sum of the data by the 
    number of datapoints (number of observations).
    """
    
    mean = (sum(data))/len(data)
    return mean
# =============================================================================
# Other means to impliment:
# floor_mean -> arithmetic mean but truncates the decimals by performing floor
# division
# weighted_mean
# golden_mean

# MEDIAN
def median(data: list):

    """
    Function: median() -> Get's the median of a list of numbers
    Input: data -> a list of numbers
    Output: median -> the number in the middle of the list if the length of the
                      list is odd or the arithmetic mean of the two numbers in
                      the middle of the list if the length of the list is even.

    The median is obtained by:
    1. Sorting the numbers in ascending order
    2. Checking whether the length of the list is even or odd
    3. If odd, obtain the {(n+1)/2}th value.
    4. If even, obtain the mean of the {n/2}th value and the {(n+2)/2}th value.
    """

    sorted(data) # This arranges the data in ascending order
    
    if (len(data)%2) != 0:
        median = data[(int((len(data) + 1) / 2) - 1)] 
        """
        -> All we're doing is getting the {(n+1)/2}th value. 
        -> I then turn this from a float to an int in order to index it from
           the list. 
        -> I finally subtract 1 because indices usually start from 0, so if I
           want the 4th item, I should index the 3rd.
        """

    else:
        median = (data[(int((len(data)) / 2)) - 1] 
                  + data[(int(((len(data)) + 2) / 2)) - 1]) / 2
        """
        -> Here, I get the {n/2}th value and the {(n+2)/2}th value.
        -> To get the {n/2}th value, I divide the len by 2, then change it from
           float to int to index it.
        -> I subtract by 1 because of zero indexing. Same goes for the
           {(n+2)/2}th value.
        -> I then get the mean between the {n/2}th value and the {(n+2)/2}th
           value to get the median
        """ 
    
    return median
# =============================================================================

# MODE
def mode(data: list):
   
   """
   Function: mode() -> Get's the mode of a list of numbers
   Input: data -> a list of numbers
   Output: mode -> The number that occurs the highest amount of times
                   a list if there's more than one mode
                   None if all numbers occur an equal amount of times
   """

   # A list was made just incase there is more than one element occur the
   # highest number of times
   list_of_modes = [] 

   # The number of times an element occurs is inputed here and compared with
   # the next element the highest number is the one that is stored.
   mode_count = 0 
   
   for i in data:
       
      if data.count(i) > mode_count:
          
         # Resets the list when a new high occuring item is found
         list_of_modes = []

         # Counts the number of times an element occurs.
         mode_count = data.count(i)

         # The element is appended to the list iff it occurs the highest
         # number of times
         list_of_modes.append(i)
      
      # Comes in handy when we have more than one mode
      elif data.count(i) == mode_count:
          
          # Avoids repetition
          if i in list_of_modes:
              pass
          
          else:
              # Appends another element that occurs just as much as the highest
              # element did
              list_of_modes.append(i)

   # Returning the number that occurs the highest amount of times
   if len(list_of_modes) == 1:
       return list_of_modes[0]
   
   # Or a None if all numbers occur an equal amount of times
   elif len(list_of_modes) == len(data):
       return None
   
   # Or a list if there's more than one mode
   else:
      return list_of_modes
# =============================================================================


# TESTS
# Testing the above functions to ensure they work properly

if __name__ == "__main__":
    data_1 = [34500, 30700, 32900, 36000, 34100, 33800, 32500]
    data_2 = [34900, 27500, 31600, 39700, 35300, 33800, 31700]

    print(data_1)
    print(f"Mean: {mean(data_1)}")
    print(f"Median: {median(data_1)}")
    print(f"Mode: {mode(data_1)}")

    print("\n")

    print(data_2)
    print(f"Mean: {mean(data_2)}")
    print(f"Median: {median(data_2)}")
    print(f"Mode: {mode(data_2)}")