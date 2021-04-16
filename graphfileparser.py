from graphshw import WeightedGraph
import math 
import linecache


# Student Name: Joseph Difilippo

def haversine(lat1, lng1, lat2, lng2) :
    """Computes haversine distance between two points in latitude, longitude.

    Keyword Arguments:
    lat1 -- latitude of point 1
    lng1 -- longitude of point 1
    lat2 -- latitude of point 2
    lng2 -- longitude of point 2

    Returns haversine distance in meters.
    """
    r = 6378100
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLng = (lng2 - lng1) * math.pi / 180.0
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
     
    a =  (math.sin(dLat / 2) * math.sin(dLat / 2)) + (math.cos(lat1) * math.cos(lat2) * math.sin(dLng / 2) * math.sin(dLng / 2))
    c = 2 * math.asin(math.sqrt(a)) 
    
    return c * r


def parseHighwayGraphFile(filename) :
    """Parses a highway graph file and return a WeightedGraph
    representing a highway graph.

    Keyword arguments:
    filename -- The name of the file containing the highway
    graph data relative to the current working directory.
    """

    with open(filename) as f:
        txt = linecache.getline(filename, 2)   
        splitLine = txt.split()
        v = int(splitLine[0])
        verticesStart = 3     
        e = int(splitLine[1])
        edgesStart = int(splitLine[1])+2

        g = WeightedGraph(v)
        w, h = 2, e
        vList = [[0 for x in range(w)] for y in range(h)]
        for i in range(verticesStart, edgesStart):
            txt = linecache.getline(filename, i)
            splitLine2 = txt.split()
            vList[i-3][0] = splitLine2[1]
            vList[i-3][1] = splitLine2[2]    
            
        for i in range(edgesStart):
            next(f)
        for line in f:
            txt2 = line.split()
            a = int(txt2[0])
            b = int(txt2[1])
            lat1 = float(vList[a][0])
            lng1 = float(vList[a][1])
            lat2 = float(vList[b][0])
            lng2 = float(vList[b][1])
            w = haversine(lat1, lng1, lat2, lng2)
            g.addEdge(a, b, w)
            
    return g.getEdgeList(withWeights=True)
        
    


if __name__ == "__main__" :
    print("haversine:")
    lat1, lng1, lat2, lng2 = 53, 17, 34, 23
    print(haversine(lat1, lng1, lat2, lng2))
    
    print("\n")
    print("parseHighwayGraphFile:")
    filename = 'albuquerque50-area-simple.tmg'
    print(parseHighwayGraphFile(filename))




    
    
