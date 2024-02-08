import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])
print(argv[4])

dotpitch = float(argv[2])
world_strength = float(argv[4])

import bpy
bpy.context.scene.camera = bpy.data.objects[argv[0]]

tv_crt = bpy.data.materials["TV-CRT"].node_tree

tv_crt.nodes['Source Image R'].image.filepath = argv[1]
tv_crt.nodes['Source Image G'].image.filepath = argv[1]
tv_crt.nodes['Source Image B'].image.filepath = argv[1]

tv_crt.nodes['Dot Pitch'].outputs[0].default_value = dotpitch

bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = world_strength


vector = tv_crt.nodes["Texture Coordinate"]

node_r_location = tv_crt.nodes["Combine XYZ.003"]
node_g_location = tv_crt.nodes["Combine XYZ.004"]
node_b_location = tv_crt.nodes["Combine XYZ.005"]

node_b_scale = tv_crt.nodes["Vector Math.003"]

node_r_out = tv_crt.nodes["Vector Math.004"]
node_g_out = tv_crt.nodes["Vector Math.005"]
node_b_out = tv_crt.nodes["Vector Math.006"]

node_r_phosphor_light = tv_crt.nodes["R Phosphor light"]
node_g_phosphor_light = tv_crt.nodes["G Phosphor light"]
node_b_phosphor_light = tv_crt.nodes["B Phosphor light"]

if argv[3] == "PVM":
  node_r_phosphor_light.node_tree = bpy.data.node_groups.get("Phosphor Stripe")
  node_g_phosphor_light.node_tree = bpy.data.node_groups.get("Phosphor Stripe")
  node_b_phosphor_light.node_tree = bpy.data.node_groups.get("Phosphor Stripe")
  tv_crt.nodes['Scanline gamma'].outputs[0].default_value = 6

if argv[3] == "CRT":
  node_r_phosphor_light.node_tree = bpy.data.node_groups.get("Shadow Mask")
  node_g_phosphor_light.node_tree = bpy.data.node_groups.get("Shadow Mask")
  node_b_phosphor_light.node_tree = bpy.data.node_groups.get("Shadow Mask")
  tv_crt.nodes['Scanline gamma'].outputs[0].default_value = 2.0

# relink nodes
tv_crt.links.new(node_r_phosphor_light.outputs[0], node_r_out.inputs[0])
tv_crt.links.new(node_g_phosphor_light.outputs[0], node_g_out.inputs[0])
tv_crt.links.new(node_b_phosphor_light.outputs[0], node_b_out.inputs[0])
tv_crt.links.new(vector.outputs[3], node_r_phosphor_light.inputs[0])
tv_crt.links.new(vector.outputs[3], node_g_phosphor_light.inputs[0])
tv_crt.links.new(vector.outputs[3], node_b_phosphor_light.inputs[0])
tv_crt.links.new(node_r_location.outputs[0], node_r_phosphor_light.inputs[1])
tv_crt.links.new(node_g_location.outputs[0], node_g_phosphor_light.inputs[1])
tv_crt.links.new(node_b_location.outputs[0], node_b_phosphor_light.inputs[1])
tv_crt.links.new(node_b_scale.outputs[0], node_r_phosphor_light.inputs[2])
tv_crt.links.new(node_b_scale.outputs[0], node_g_phosphor_light.inputs[2])
tv_crt.links.new(node_b_scale.outputs[0], node_b_phosphor_light.inputs[2])
