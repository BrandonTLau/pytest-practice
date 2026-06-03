'''
1) EP:

invalid:
weight == 0 [done]
weight == -1 [done]
destination == "USA" [done]
weight == "heavy" [done]


valid:
weight == 1 [done]
destination == "domestic"
destination == "international"

2)BVA 

BVA for weight (boundary is 0):

weight = -1 (just below — invalid)
weight = 0 (on boundary — invalid)
weight = 1 (just above — valid)


'''

def shipping_cost(weight, destination):
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")
    if destination not in ["domestic", "international"]:
        raise ValueError("Destination must be domestic or international.")
    
    if destination == "domestic":
        domestic_cost = 5 + (2*weight)
        return domestic_cost
    if destination == "international":
        international_cost = 20 + (5*weight)
        return international_cost
