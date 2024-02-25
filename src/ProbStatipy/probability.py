# PROBABILITY FUNCTION

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

# =============================================================================
    
# PROBABILITY CLASSES
    
class SampleSpace(set):
    """
    Class -> SampleSpace

    Attributes -> sample_space, probability = 1, cardinality

    Methods -> get_sample_space(): returns the set of basic outcomes

    SampleSpace is a class that represents the sample space of a random experiment.
    It inherits from the set class since a sample space is a set of basic outcomes.
    A sample space cannot change mid experiment, therefore, you cannot change a
    SampleSpace object once declared (There are no setter methods).

    It's attributes include:

    self.sample_space -> the set of basic outcomes

    self.probability -> the probability of getting one outcome from the sample
    space during an experiment. This is always 1

    self.cardinality -> the number of basic outcomes [the len() of the set]
    """

    def __init__(self, sample_space: set):
        self.sample_space = sample_space
        self.probability = 1
        self.cardinality = len(self.sample_space)

    def get_sample_space(self):
        """
        SampleSpace method -> returns the set of basic outcomes (sample space). Arguments: None.
        """
        return self.sample_space


class Event(set):
    """
    Class -> Event
    Attributes -> event
    Methods -> get_event(), set_event(), union(), intersect()

    Event is a Class designed to mimick a subset of a sample space.
    Just like the SampleSpace class, it inherits from a set, as events are also sets.

    Attributes:

    self.event -> a set (meant to be a subset of a sample space)

    Methods:

    This class has one getter method [get_event()] and one setter
    method[set_event()]

    It also has a union() and an intersect() event that derives new sets by
    obtaining the union or the intersection, respectively, of two sets.

    The prob() method is used to derive the probability of the event occuring
    from the sample space. 
    
    Arguments:
    sample_space -> a sample space of type SampleSpace ought to be provided.
    This is mandatory.

    compound -> this is an optional argument that specifies whether the event
    is a compound event. It defaults to None. Possibe values are "or" (which
    applies the addition rule of probabilities) & "and" (which applies the
    multiplication rule). If compound is set to None and there is more than one
    basic outcome in the event, it will return a list of probabilities of each
    outcome.
    """
    def __init__(self, event: set):
        self.event = event

    def get_event(self):
        """
        Event method -> returns a subset of the sample space (an event)
        """
        return self.event
    
    def set_event(self, new_event):
        self.event = new_event

    # def union(self, event):
    #     return self.event.union(event)
    
    # def intersect(self, event):
    #     return self.event.intersection(event)

    def prob(self, sample_space: SampleSpace, compound = None):
        prob_list = []
        if compound == None:
            for i in self.event:
                prob_list.append(probability(1, sample_space.cardinality))
            
            if len(prob_list) == 1:
                return prob_list[0]
            else:
                return prob_list
        elif compound == "or":
            for i in self.event:
                prob_list.append(probability(1, sample_space.cardinality))
            return sum(prob_list)
        elif compound == "and":
            prob = 1
            for i in self.event:
                prob *= probability(1, sample_space.cardinality)
            return prob
        else:
            raise Exception(" The optional argument type can only take 3 values: None, 'or', 'and' ")

# TESTS
if __name__ == "__main__":
    print(probability(3, 10))
    print(probability(50, 1000))
    # print(probability(10, 1))
    # print(probability(-4, 20))

    die = SampleSpace({1,2,3,4,5,6})
    event1 = Event({4})
    event2 = Event({4,5})
    event3 = Event({2, 4, 6})

    print(die.probability)
    print(event1.prob(die))
    print(event2.prob(die))
    print(event2.prob(die, "or"))
    print(event2.prob(die, "and"))
    print(event3.prob(die, "or"))

    coin = SampleSpace({"H", "T"})
    event1 = Event({"H"})
    event2 = Event({"T"})
    event3 = Event({"H", "T"})

    print(coin.probability)
    print(event1.prob(coin, "or"))
    print(event2.prob(coin, "and"))
    print(event1.prob(coin))
    print(event2.prob(coin))
    print(event3.prob(coin))
    print(event3.prob(coin, "and"))
    print(event3.prob(coin, "or"))
    # print(event1.union(event2))