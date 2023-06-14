from vpython import *

# параметры солнца
sun = sphere(pos=vector(0, 0, 0), radius=1.5, color=color.yellow, emissive=True)

# параметры планет
mercury = sphere(pos=vector(3, 0, 0), radius=0.3, color=color.gray(0.8))
venus = sphere(pos=vector(6, 0, 0), radius=0.5, color=color.orange)
earth = sphere(pos=vector(9, 0, 0), radius=0.5, texture=textures.earth)
moon = sphere(pos=vector(9.7, 0, 0), radius=0.2, color=color.white)

mars = sphere(pos=vector(12, 0, 0), radius=0.4, color=color.orange)

jupiter = sphere(pos=vector(16, 0, 0), radius=1.2, color=color.orange)
jupiter_ring = ring(pos=jupiter.pos, axis=jupiter.axis, radius=jupiter.radius * 1.2, thickness=0.2, color=color.white)

saturn = sphere(pos=vector(21, 0, 0), radius=1, color=color.yellow)
saturn_ring = ring(pos=saturn.pos, axis=saturn.axis, radius=saturn.radius * 1.5, thickness=0.2, color=color.white)

uranus = sphere(pos=vector(27, 0, 0), radius=0.8, color=color.cyan)

neptune = sphere(pos=vector(33, 0, 0), radius=0.8, color=color.blue)

pluto = sphere(pos=vector(38, 0, 0), radius=0.2, color=color.white)

# параметры орбит



def ellipse(pos, length, width, color, opacity):
    pass
mercury.orbit = ellipse(pos=sun.pos, length=6, width=3, color=color.white, opacity=0.3)
venus.orbit = ellipse(pos=sun.pos, length=9, width=5, color=color.white, opacity=0.3)
earth.orbit = ellipse(pos=sun.pos, length=12, width=8, color=color.white, opacity=0.3)
mars.orbit = ellipse(pos=sun.pos, length=16, width=10, color=color.white, opacity=0.3)
jupiter.orbit = ellipse(pos=sun.pos, length=24, width=14, color=color.white, opacity=0.3)
saturn.orbit = ellipse(pos=sun.pos, length=32, width=20, color=color.white, opacity=0.3)
uranus.orbit = ellipse(pos=sun.pos, length=38, width=24, color=color.white, opacity=0.3)
neptune.orbit = ellipse(pos=sun.pos, length=44, width=28, color=color.white, opacity=0.3)
pluto.orbit = ellipse(pos=sun.pos, length=48, width=30, color=color.white, opacity=0.3)

# анимация движения планет и лун
dt = 0.1
while True:
    rate(50)

    # перемещение планет
    mercury.pos = rotate(mercury.pos, radians(0.5), vector(0, 1, 0))
    venus.pos = rotate(venus.pos, radians(0.4), vector(0, 1, 0))
    earth.pos = rotate(earth.pos, radians(0.3), vector(0, 1, 0))
    moon.pos = rotate(moon.pos, radians(0.4), vector(0, 1, 0))
    moon.pos = vector(earth.pos.x + moon.pos.x, moon.pos.y, moon.pos.z)
    mars.pos = rotate(mars.pos, radians(0.2), vector(0, 1, 0))
    jupiter.pos = rotate(jupiter.pos, radians(0.1), vector(0, 1, 0))
    jupiter_ring.pos = jupiter.pos
    saturn.pos = rotate(saturn.pos, radians(0.08), vector(0, 1, 0))
    saturn_ring.pos = saturn.pos
    uranus.pos = rotate(uranus.pos, radians(0.06), vector(0, 1, 0))
    neptune.pos = rotate(neptune.pos, radians(0.05), vector(0, 1, 0))
    pluto.pos = rotate(pluto.pos, radians(0.04), vector(0, 1, 0))

    # перемещение орбит
    mercury.orbit.pos = sun.pos
    venus.orbit.pos = sun.pos
    earth.orbit.pos = sun.pos
    mars.orbit.pos = sun.pos
    jupiter.orbit.pos = sun.pos
    saturn.orbit.pos = sun.pos
    uranus.orbit.pos = sun.pos
    neptune.orbit.pos = sun.pos
    pluto.orbit.pos = sun.pos
