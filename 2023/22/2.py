import sys, copy

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
            print('oops')
            self.B = TPoint(A[0], A[1], A[2] - 1)
            self.A = TPoint(B[0], B[1], B[2] - 1)
        else:
            self.A = TPoint(A[0], A[1], A[2] - 1)
            self.B = TPoint(B[0], B[1], B[2] - 1)
        self.L = sum(B) - sum(A) + 1
        self.stepX = 0 if B[0] == A[0] else 1
        self.stepY = 0 if B[1] == A[1] else 1
        self.stepZ = 0 if B[2] == A[2] else 1
        global lenX, lenY, lenZ
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
                
    def Down(self, id, space):
        if self.stepZ == 0:
            for p in self.Points():
                space[p.x][p.y][p.z] = -1
                space[p.x][p.y][p.z - 1] = id
        else:
            space[self.B.x][self.B.y][self.B.z] = -1
            space[self.A.x][self.A.y][self.A.z - 1] = id
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
        layer.append([-1] * lenZ)
    Space.append(layer)
    
for b in range(len(Bricks)):
    for point in Brick[b].Points():
        Space[point.x][point.y][point.z] = b
        
def Fall(bricks, space):
    moved = True
    while moved:
        moved = False
        for b in range(len(bricks)):
            if all(p.z > 0 and space[p.x][p.y][p.z - 1] == -1 for p in bricks[b].Bottom()):
                bricks[b].Down(b, space)
                MovedBricks.add(b)
                moved = True
            
MovedBricks = set()
Fall(Bricks, Space)

cnt = 0
for b in range(len(Bricks)):
    NewBricks = copy.deepcopy(Bricks)
    NewSpace = copy.deepcopy(Space)
    NewBricks.pop(b)
    MovedBricks = set()
    for x in NewSpace:
        for y in x:
            for z in range(len(y)):
                if y[z] == b:
                    y[z] = -1
    Fall()
    cnt += len(MovedBricks)
    
 
print(cnt)

# 
                