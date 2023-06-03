
G = 6.67 * 10**-10
AU = 1.496 * 10**11
timestep = 86400
earth_route = []

sun = {
        "mass": 1.989 * 10**30,
        "radius": 20,
        "x": 0,
        "y": 0
}
earth = {
        "mass": 5.97219 * 10**24,
        "radius": 3.5,
        "distance": 149.6,
        "x": AU / 10**9,
        "y": 0,
        "vy": 29.783 * 1000, # m/s
        "vx": 0
}
venus = {
        "mass": 4.867 * 10**24,
        "radius": 3.4,
        "distance": 104.7,
        "x": 0.7*AU / 10**9,
        "y": 0,
        "vy": 35.02 * 1000,
        "vx": 0
} 
mercury = {
        "mass": 3.285 * 10**23,
        "radius": 1.5,
        "distance": 59.84,
        "x": 0.4*AU / 10**9,
        "y": 0,
        "vy": 47.36 * 1000,
        "vx": 0
} 
mars = {
        "mass": 6.39 * 10**23,
        "radius": 2.5,
        "distance": 224.4,
        "x": 1.5*AU / 10**9,
        "y": 0,
        "vy": 24.08 * 1000,
        "vx": 0
} 
jupiter = {
        "mass": 1.898 * 10**27,
        "radius": 7,
        "distance": 600,
        "x": 4.02*AU / 10**9,
        "y": 0,
        "vy": 13.06 * 1000,
        "vx": 0 
}