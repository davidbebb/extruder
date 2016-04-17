
extruder_cutter     = '1/8_endmill'
extruder_material   = 'delrin'
extruder_thickness  = 12

cutter_rad=milling.tools[extruder_cutter]['diameter']/2


spacer_cutter       = '1/8_endmill'
spacer_material     = 'pvc'
spacer_thickness    = 3

cover_cutter = '1/8_endmill'
cover_material = 'pvc'
cover_thickness = 3

motor = 'NEMA1.7'

width =  42.3
height = 13.7

corner_rad = 5
centre = V(0,0)
stepper_pos = V(0, (width/2)-(height/2))

plane = camcam.add_plane(Plane('plane', cutter=cover_cutter))

plane.add_layer(
    'spacer',
    material = spacer_material,
    thickness = spacer_thickness,
    z0 = 0)

plane.add_layer(
    'foo',
    material = spacer_material,
    thickness = spacer_thickness,
    z0 = 0)

plane.add_layer(
    'extruder',
    material = extruder_material,
    thickness = extruder_thickness,
    z0 = 0)

plane.add_layer(
    'cover',
    material = cover_material,
    thickness = cover_thickness,
    z0 = 0)


cover_border = RoundedRect(
    stepper_pos + V(0, height/2),
    width = width,
    height = width+height,
    rad = corner_rad,
    centred = True)

stepper = Stepper(stepper_pos, motor, 'foo')
d = stepper.d



spacer_pos = centre
spacer_x = width/2
spacer_y = (height)/2
x_offset=12

spacer_border = Path(closed=True, side='out')
spacer_border.add_point(PIncurve(spacer_pos + V(-spacer_x, -spacer_y), radius=corner_rad, direction = 'CW'))
spacer_border.add_point(PIncurve(spacer_pos + V(-spacer_x,  spacer_y), radius=corner_rad, direction = 'CW'))
spacer_border.add_point(PIncurve(spacer_pos + V( -x_offset,  spacer_y), radius=-1.5, direction = 'CW'))
spacer_border.add_point(POutcurve(stepper_pos, radius=11, direction = 'CW'))
spacer_border.add_point(PIncurve(spacer_pos + V(  x_offset,  spacer_y), radius=0, direction = 'CW'))
spacer_border.add_point(PIncurve(spacer_pos + V( spacer_x,  spacer_y), radius=corner_rad, direction = 'CW'))
spacer_border.add_point(PIncurve(spacer_pos + V( spacer_x, -spacer_y), radius=corner_rad, direction = 'CW'))

feed_offset=6

border = Path(closed=True, side='out')
border.add_point(PIncurve(spacer_pos + V(-spacer_x,  spacer_y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( spacer_x,  spacer_y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( spacer_x, -spacer_y), radius=corner_rad, direction = 'CW'))

border.add_point(PIncurve(spacer_pos + V( (feed_offset+1), -spacer_y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( feed_offset, -spacer_y+0.2), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( (feed_offset-1), -spacer_y), radius=corner_rad, direction = 'CW'))

border.add_point(PIncurve(spacer_pos + V( (-feed_offset+1), -spacer_y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( -feed_offset, -spacer_y+0.2), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(spacer_pos + V( (-feed_offset-1), -spacer_y), radius=corner_rad, direction = 'CW'))

border.add_point(PIncurve(spacer_pos + V(-spacer_x, -spacer_y), radius=corner_rad, direction = 'CW'))



spacer = plane.add_path(
    Part(name = 'space_part',
        border = spacer_border,
        layer = 'spacer',
        cutter = spacer_cutter
    )
)

spacer.add(Hole(stepper_pos+V(d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
spacer.add(Hole(stepper_pos+V(-d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))




extruder = plane.add(
    Part(name = 'extrued_part',
        border = border,
        layer = 'extruder',
        cutter = extruder_cutter
    )
)


extruder.add(Hole(stepper_pos+V(d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))
extruder.add(Hole(stepper_pos+V(-d['bolt_sep']/2, -d['bolt_sep']/2), rad=milling.bolts[d['bolt_size']]['clearance']/2))



cover = plane.add(
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
