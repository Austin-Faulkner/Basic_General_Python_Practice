# In geometry, a line segment is a part of a line that is
# bounded by two distinct endpoints and contains every point
# on the line between its endpoints. We want to model a line segment using Python classes.

# Create a class called Point to represent a point in the Cartesian plane.
# Every instance of Point will have two properties: x and y, both floating
# point numbers passed in at the time of creation.

# Create a class called LineSegment. Every instance of LineSegment will
# have two properties: endpoint1 and endpoint2, both Point objects passed in at the time of creation.

# Then to model the line segment bounded by the points (1,2) and (8,-3), you might say:

#   a = Point(1,2)
#   b = Point(8,-3)
#   seg = LineSegment(a,b)
   
# Add two methods to class LineSegment:

# length, which returns a floating-point number representing the length of the line segment.
# The length of a line segment with endpoints (a,b) and (c,d) is defined as the square root of (a-c)2 + (b-d)2.
# midpoint, which returns a Point object representing the midpoint of the line segment.
# The midpoint of a line segment with endpoint (a,b) and (c,d) is defined as the point ( (a+c)/2, (b+d)/2 ).

import math

class Point:

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:

    # Constructor
    def __init__(self, ep1, ep2):
        self.endpoint1 = ep1
        self.endpoint2 = ep2

    def length(self):
        return math.sqrt((self.endpoint1.x - self.endpoint2.x)**2 + \
                         (self.endpoint1.y - self.endpoint2.y)**2)

    def midpoint(self):
        # self.LineSegmentAssignmentAttribute.PointAssignmentAttribute
        midX = (self.endpoint1.x + self.endpoint2.x)/2
        midY = (self.endpoint1.y + self.endpoint2.y)/2
        
        # return Point object
        return Point(midX, midY)

def main():

    # Point instance: object(s)
    p1 = Point(5,2)
    p2 = Point(9,4)

    # Return LineSegment instance: object
    mySeg = LineSegment(p1, p2)
    print("Length (should be 4.472): ", round(mySeg.length(), 3))

    p3 = mySeg.midpoint()
    print("Midpoint (should be 7.0,3.0): ", p3.x, p3.y)
   
main()
