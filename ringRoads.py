import math

'''
Key here is don't over complicate things.  You COULD set up nodes for paths
you COULD try to get the shortest arc...abs

OR you could just calculate the distances for ALL the paths
'''
def circumTravel(radius, startAngle, endAngle):
    # returns distance traveled along a ring from start to end
    
    traveledAngle = math.fabs(endAngle - startAngle) 
    # if distance is more than half the circle, go the other direction
    if traveledAngle > 180:
        traveledAngle = 360 - traveledAngle

    return (traveledAngle * math.pi * radius) / 180

# We don't need this at all
def shortestArc(angle, roads):
    # Get the degree arc to each road given an angle
    paths = [math.fabs(x - angle) for x in roads]
    paths = [360 - x if x > 180 else x for x in paths]

    # Get the road to the shorest path
    return roads[paths.index(min(paths))]
    

def ringRoads(innerRing, outerRing, roads, travels):
    ret = [0] * len(travels)
    ringDist = outerRing - innerRing
    
    # Take every road
    for i, t in enumerate(travels):
        toStart = [circumTravel(innerRing, t[0], x) for x in roads]
        toFinish = [circumTravel(outerRing, t[1], x) for x in roads]
        for j in range(len(roads)):
            toStart[j] += toFinish[j]
        ret[i] = min(toStart)

    ret = [x + ringDist for x in ret]
    return ret

#print(ringRoads(10, 20, [180], [[0,0], [60,300]]))

#print(ringRoads(5, 30, [220.28249], [[180.520251,80.37913], [15.794063,85.984333]]))

#print(ringRoads(1, 42, [338.864038, 311.235725], [ [37.959303,20.206089] ]))

#
print(ringRoads(999, 1000, [ 1.93573,0.904473,209.253983, 38.969013, 178.467116, 137.531902, 181.993079, 129.885195, 178.516437, 283.597115, 147.611906, 70.972958, 30.68365, 287.241272, 327.252872, 320.581891, 207.981467, 230.251322, 57.999991, 175.158868, 218.254257, 276.207182, 74.387357, 42.690989, 311.780595, 219.341251, 82.990768, 121.382704, 341.861433, 223.908523, 89.413574, 91.510786, 63.453949, 281.596767, 7.812061, 89.234636, 155.427805, 146.770936, 334.669652, 359.928379, 84.990235, 205.403351, 353.127536, 288.703872, 292.191005, 48.789789, 143.825368, 82.991824, 7.082733, 220.705587, 135.904538, 229.574117, 102.247097, 116.28474, 232.236324, 28.565627, 309.324372, 247.603646, 309.936331, 38.6685, 245.371316, 15.799253, 278.360391, 123.745333,  146.333184, 148.875957, 43.006822, 173.749581, 96.635514, 272.695444, 56.108854, 349.687975, 48.880578, 315.660873, 187.702005, 307.663622, 9.174811, 281.815963, 356.598521, 157.795476, 274.792717, 98.406199,  188.436128, 306.709474, 249.287469, 273.368373, 77.922331, 289.508906, 195.037041, 96.526764, 288.353308, 265.453368, 306.190427, 27.456484, 324.509789, 77.683106, 224.602919, 145.821893, 223.176635, 279.00666]
, [ [6.285942,3.727166] ]))

#print (220.28249 - 15.794063)