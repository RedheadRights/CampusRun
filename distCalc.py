import math
<<<<<<< HEAD
=======

>>>>>>> ec90da391643c0f456b657aac362b1a7bb56f28a
def distCalc(lat1, lon1, lat2, lon2):
    R = 6371*10**3 # meters

    radLat1 = lat1 * math.pi/180
    radLon1 = lon1 * math.pi/180
    radLat2 = lat2 * math.pi/180
    radLon2 = lon2 * math.pi/180

    dLat = radLat2 - radLat1
    dLon = radLon2 - radLon1

    a = hav(radLat2 - radLat1) + (1 - hav(radLat1 - radLat2) - hav(radLat1 + radLat2)) * hav(radLon2 - radLon1)
    d = 2*R*math.asin(math.sqrt(a))

    return(d)

def hav(theta):
    return(math.sin(theta/2)**2)
