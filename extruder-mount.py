

extruder_cutter     = '1/8_endmill'
extruder_material   = 'abs'
extruder_thickness  = 12

spacer_cutter       = 'laser'
spacer_material     = 'perspex'
spacer_thickness    = 3

motor = 'nema1.7'

width =  42.3
height = 13.7
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

border = RoundedRect(
    centre,
    width = width,
    height = height,
    rad = 1,
    centred = True)

spacer = plane.add_path(
    Part(name = 'space_part',
        border = border,
        layer = 'spacer',
        cutter = spacer_cutter
    )
)

stepper = spacer.add(Stepper(stepper_pos, 'NEMA1.7', 'spacer'))

extruder = plane.add_path(
    Part(name = 'extrued_part',
        border = border,
        layer = 'extruder',
        cutter = extruder_cutter
    )
)

print stepper.d

# d = pStepper['NEMA1.7']
#
# spacer.add(Hole(stepper_pos+V(d['bolt_sep']/2,d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2),layer)
# spacer.add(Hole(stepper_pos+V(-d['bolt_sep']/2,d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
