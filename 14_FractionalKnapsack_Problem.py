'''You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the tru
'''

def fill_truck(DiffBoxes, truck_size):

    DiffBoxes.sort(key=lambda x: x[1], reverse=True)
    
    total_units = 0
    
    for boxes, units in DiffBoxes:

        boxes_to_fill_with = min(boxes, truck_size)

        total_units += boxes_to_fill_with * units
    
        truck_size -= boxes_to_fill_with

        if truck_size == 0:
            break
    
    return total_units


DiffBoxes = [[1, 5], [2, 3]]
truck_size = 11

max_fill = fill_truck(DiffBoxes, truck_size)
print(max_fill)  
