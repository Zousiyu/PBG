##Packed-Bed generation module (Version Beta)
##BPartopour, AG Dixon†
##Heat and Mass Transfer Lab
##Worcester Polytechnic Institute

#Defining parameters for the simulation 

# defining particle type, valid types: 'sphere', 'cylinder', 'Raschig Ring', 'f_point_star', 'three_holes', 'four_holes', 'tri_lobes', 'quadrilobes', 'four_hole_sphere'
Particle_type = 'tri_lobes'

##Tube's dimensions
# Raduis of the Tube
cyl_radius = 10.5
# Length of the Tube
#Warning! This is not the length of the packing. The packing length depends on number of particles. However, this should be in a safe-side to avoid an overload!
cyl_depth = 300


## Particles Properties
#Number of Particles
number_of_particle = 300
#Particle radius !! in case of Rashig Ring this is outer radius
particle_radius = 2.25
#particle innter radius for extruded geometries
particle_inner_radius = 0.6
#Particle Length (for cylinders, in case of spheres leave it as default)
particle_length = 4.5


## Rigidbody Properties
#Collision Shape, valid types: 'MESH', 'CONVEX_HULL', 'SPHERE'
collision_shape = 'CONVEX_HULL'
#Surface Friction Factor ( 0 < friction_factor < 1 )
friction_factor = 0.1
#Surface Restitution Factor (0 < restitution_factor < 1)
restitution_factor = 0.88
#Usinig Coloision Margin: Yes (True), NO (False)
use_margin = True
#Colosion margin (lower value = more accuracy, 0 perfect value)
collision_margin = 0.01
#linear_deactivation(linear deactivation velocity)

#linear_damping(amount of linear velicity particle is lost over time)
linear_damping = 0.2
#rotational_dampin
rotational_damping = 0.1

#Do you want to remove the tube after simulation?
remove_the_tube = True

#Do you want to calculate the angle distribution of the particles after the bed is generated?
angle_dist = True
#Where do you want to save the angle_dist results?
file_name ='Angle_spheres_300_spheres_N4-7.txt'

## Stl Export properties
file_path = "300_spheres_spheres_N=4.7.stl"
## Where do you want to save the radial voidage results?
file_path_2 = "radial_300_spheres_N=4.7.txt"
