import distCalc from distCalc


function CalcTotalDist(coordList){
    //Calculates the total distance of a run
    //Inputs: A list of coordinate tuples (latitude, longitude)
    //Outputs: total distance in meters

    var totalDistance = 0;
    
    for(let coordIndex = 0; coordIndex < length(coordList - 1); coordIndex++){
        //Pull longitude and latitudes out of the tuples
        var lat1 = coordList[coordIndex][0];
        var lon1 = coordList[coordIndex][1];
        var lat2 = coordList[coordIndex + 1][0];
        var lon2 = coordList[coordIndex + 1][1];
        
        totalDistance += distCalc(lat1, lon1, lat2, lon2);
    }

    return totalDistance
}