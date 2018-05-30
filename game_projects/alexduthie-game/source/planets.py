import math
import numpy
#simple 2D orbital mechanics
x = [[5, 5, 1], [0, 0, 2]]
# xcoord, ycoord, mass
f = [[0, 0], [0, 0]]
f2 = [[0, 0], [0, 0]]
# force, yforce
v = [[1, 0], [2, 3]]

dt = 0.001

# the force in the direction from mass 1 to mass 2. Hence the force acting ON mass 1.

def pbc(min,max,coord):
    length = max - min +1
    if coord > max:
        coord += -length
    if coord < min:
        coord += length
    return coord



def pair(x1, y1, m1, x2, y2, m2):
    dx = x2 - x1
    dy = y2 - y1
    mag = math.sqrt(dx ** 2 + dy ** 2)
    vector = (dx / mag, dy / mag)
    force = m1 * m2 / (mag ** 2)
    return vector[0]*force, vector[1]*force

def forces(forc, pos):
    for i in range(len(pos)):
        forc[i][0] = 0
        forc[i][1] = 0
        for j in range(len(pos)):
            if i != j:
                newf = pair(pos[i][0], pos[i][1], pos[i][2], pos[j][0], pos[j][1], pos[j][2])
                forc[i][0] += newf[0]
                forc[i][1] += newf[1]

running = True
while running:
    for i in range(len(x)):
        x[i][0] = pbc(0,5,x[i][0] + v[i][0] * dt + 0.5 * f2[i][0] * (dt ** 2) / x[i][2])
        x[i][1] = pbc(0,5,x[i][1] + v[i][1] * dt + 0.5 * f2[i][1] * (dt ** 2) / x[i][2])
        forces(f, x)
        v[i][0] = v[i][0] + 0.5 * (f2[i][0]+f[i][0])*dt
        v[i][1] = v[i][1] + 0.5 * (f2[i][1] + f[i][1]) * dt

        x[i][0] = pbc(0,5,x[i][0] + v[i][0] * dt + 0.5 * f[i][0] * (dt ** 2) / x[i][2])
        x[i][1] = pbc(0,5,x[i][1] + v[i][1] * dt + 0.5 * f[i][1] * (dt ** 2) / x[i][2])
        forces(f2,x)
        v[i][0] = v[i][0] + 0.5 * (f2[i][0] + f[i][0]) * dt
        v[i][1] = v[i][1] + 0.5 * (f2[i][1] + f[i][1]) * dt
        print(2)
        print("hello")
        print("A\t{0}\t{1}\t0".format(x[0][0],x[0][1]))
        print("A\t{0}\t{1}\t0".format(x[1][0], x[1][1]))






