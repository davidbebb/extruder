

extruder_cutter     = '1/8_endmill'
extruder_material   = 'abs'
extruder_thickness  = 12

spacer_cutter       = 'laser'
spacer_material     = 'perspex'
spacer_thickness    = 3

cover_cutter = 'laser'
cover_material = 'perspex'
cover_thickness = 3

motor = 'NEMA1.7'

width =  42.3
height = 13.7

corner_rad = 3
centre = V(0,0)
stepper_pos = V(0, (42.3/2)-(height/2))

plane = camcam.add_plane(Plane('plane'))

plane.add_layer(
    'spacer',
    material = spacer_material,
    thickness = spacer_thickness,
    # cutter = spacer_cutter,
    z0 = 0)

plane.add_layer(
    'extruder',
    material = extruder_material,
    thickness = extruder_thickness,
    # cutter = extruder_cutter,
    z0 = 0)

plane.add_layer(
    'cover',
    material = cover_material,
    thickness =cover_thickness,
    z0 = 0)

border = RoundedRect(
    centre,
    width = width,
    height = height,
    rad = corner_rad,
    centred = True)

cover_border = RoundedRect(
    stepper_pos + V(0, height/2),
    width = width,
    height = width+height,
    rad = corner_rad,
    centred = True)

spacer = plane.add_path(
    Part(name = 'space_part',
        border = border,
        layer = 'spacer',
        cutter = spacer_cutter
    )
)


stepper = spacer.add(Stepper(stepper_pos, motor, 'spacer'))

extruder = plane.add_path(
    Part(name = 'extrued_part',
        border = border,
        layer = 'extruder',
        cutter = extruder_cutter
    )
)

d = stepper.d
print d
extruder.add(Hole(stepper_pos+V(d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
extruder.add(Hole(stepper_pos+V(-d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))

cover = plane.add_path(
    Part(name = 'cover_part',
        border = cover_border,
        layer = 'cover',
        cutter = cover_cutter
    )
)


cover.add(Hole(stepper_pos+V(d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
cover.add(Hole(stepper_pos+V(-d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
cover.add(Hole(stepper_pos+V(d['bolt_sep']/2, d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
cover.add(Hole(stepper_pos+V(-d['bolt_sep']/2, d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
cover.add(Hole(stepper_pos, rad=d['shaft_diam']/2+1))

cover.add(Hole(stepper_pos+V(d['bolt_sep']/2, d['bolt_sep']/1.05), rad=milling.bolts[d['bolt_size']]['clearance']/2))
cover.add(Hole(stepper_pos+V(-d['bolt_sep']/2, d['bolt_sep']/1.05), rad=milling.bolts[d['bolt_size']]['clearance']/2))
