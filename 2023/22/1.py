import sys

Bricks = []
lenX = 0
lenY = 0
lenZ = 0

class TPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
class TBrick:
    def __init__(self, st):
        ends = st.split('~')
        A = list(map(int, ends[0].split(',')))
        B = list(map(int, ends[1].split(',')))
        if sum(A) > sum(B):
            self.B = TPoint(A[0], A[1], A[2] - 1)
            self.A = TPoint(B[0], B[1], B[2] - 1)
        else:
            self.A = TPoint(A[0], A[1], A[2] - 1)
            self.B = TPoint(B[0], B[1], B[2] - 1)
        self.L = sum(B) - sum(A) + 1
        self.stepX = 0 if B[0] == A[0] else 1
        self.stepY = 0 if B[1] == A[1] else 1
        self.stepZ = 0 if B[2] == A[2] else 1
        lenX = max(lenX, A[0], B[0])
        lenY = max(lenY, A[1], B[1])
        lenZ = max(lenZ, A[2], B[2])
        
    def Points(self):
        return [TPoint(self.A.x + i * self.stepX, self.A.y + i * self.stepY, self.A.z + i * self.stepZ) for i in range(self.L)]
        
    def Bottom(self):
        match self.stepZ:
            case 0:
                return self.Points()
            case 1:
                return [self.A]
                
    def Down(self):
        if self.stepZ == 0:
            for p in self.Points():
                Space[p.x][p.y][p.z] = None
                Space[p.x][p.y][p.z - 1] = self
        else:
            Space[B.x][B.y][B.z] = None
            Space[A.x][A.y][A.z - 1] = self
        self.A.z -= 1
        self.B.z -= 1
        

for line in sys.stdin:
    brick = TBrick(line)
    Bricks.append(brick)
    
Space = []
lenX += 1
lenY += 1

for x in range(lenX):
    layer = []
    for y in range(lenY):
        layer.append([None] * lenZ)
    Space.append(layer)
    
for brick in Bricks:
    for point in brick.Points():
        Space[point.x][point.y][point.z] = brick
        
moved = True
while moved:
    moved = False
    for brick in Bricks:
        if all(p.z > 0 or not Space[p.x][p.y][p.z - 1] for p in brick.Bottom()):
            brick.Down()
            moved = True
            
SupportedBy = {}
IsSupporting = {}
for brick in Bricks:
    SupportedBy[brick] = []
    IsSupporting[brick] = []

for brick in Bricks:
    bottom = brick.Bottom()
    if bottom[0].z > 0:
        for p in bottom:
            lower = Space[p.x][p.y][p.z - 1]
            if lower:
                SupportedBy[brick].append[lower]
                IsSupporting[lower].append[brick]
                
cnt = 0
for brick in Bricks:
    if all(len(SupportedBy[higher] > 1) for higher in IsSupporting[brick])
        cnt += 1
        
print(cnt)
                