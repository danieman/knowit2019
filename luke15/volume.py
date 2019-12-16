class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"


def signed_volume_of_triangle(p1, p2, p3):
    """Implemented from https://stackoverflow.com/a/1568551/12348201"""
    v321 = p3.x * p2.y * p1.z
    v231 = p2.x * p3.y * p1.z
    v312 = p3.x * p1.y * p2.z
    v132 = p1.x * p3.y * p2.z
    v213 = p2.x * p1.y * p3.z
    v123 = p1.x * p2.y * p3.z
    return (-v321 + v231 + v312 - v132 - v213 + v123)/6


def volume_of_mesh(mesh):
    vols = [signed_volume_of_triangle(t.p1, t.p2, t.p3) for t in mesh]
    return round(sum(vols)/1000, 3)


mesh = []
with open('MODEL.CSV') as f:
    for line in f:
        v = [float(n) for n in line.split(',')]
        p1 = Point(v[0], v[1], v[2])
        p2 = Point(v[3], v[4], v[5])
        p3 = Point(v[6], v[7], v[8])
        t = Triangle(p1, p2, p3)
        mesh.append(t)

print(volume_of_mesh(mesh))
