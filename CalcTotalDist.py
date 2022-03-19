from distCalc import distCalc


def CalcTotalDist(coordList):
    #Calculates the total distance of a run
    #Inputs: A list of coordinate tuples (latitude, longitude)
    #Outputs: total distance in meters

    totalDistance = 0
    
    for coordIndex in range(len(coordList) - 1):
        #Pull longitude and latitudes out of the tuples
        lat1 = coordList[coordIndex][0]
        lon1 = coordList[coordIndex][1]
        lat2 = coordList[coordIndex + 1][0]
        lon2 = coordList[coordIndex + 1][1]
        
        totalDistance += distCalc(lat1, lon1, lat2, lon2)
        
    return totalDistance