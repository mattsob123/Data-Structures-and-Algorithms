import heapq
import math

def kClosest(points, k):
        
        heap = []
        distanceMap = {}
        
        output = []
        
        for point in points:
            distance = math.sqrt( (0-point[0])**2+(0-point[1])**2)
            distanceMap[distance] = [point[0], point[1]]
            heap.append(distance)
            
        heapq.heapify(heap)
        
        for i in range(k):
            print(heap)
            solution = heapq.heappop(heap)
            output.append(distanceMap[solution])
            print(distanceMap[solution])
            
            
        return output


kClosest([[1,3],[-2,2],[2,-2]], 2)