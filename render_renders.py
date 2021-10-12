import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])

pvm_shadowmask = ["//texture/shadowmask_inline-unlit_10x10_R.png","//texture/shadowmask_inline-unlit_10x10_G.png","//texture/shadowmask_inline-unlit_10x10_B.png"]
crt_shadowmask = ["//texture/shadowmask_inline_10x10_R.png","//texture/shadowmask_inline_10x10_G.png","//texture/shadowmask_inline_10x10_B.png"]
tvl = float(argv[2])

import bpy
bpy.context.scene.camera = bpy.data.objects[argv[0]]
bpy.data.materials["TV-CRT"].node_tree.nodes['Source Image R'].image.filepath = argv[1]
bpy.data.materials["TV-CRT"].node_tree.nodes['Source Image G'].image.filepath = argv[1]
bpy.data.materials["TV-CRT"].node_tree.nodes['Source Image B'].image.filepath = argv[1]


bpy.data.materials["TV-CRT"].node_tree.nodes['TVL'].outputs[0].default_value = tvl

if argv[3] == "PVM":
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask R'].image.filepath = pvm_shadowmask[0]
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask G'].image.filepath = pvm_shadowmask[1]
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask B'].image.filepath = pvm_shadowmask[2]
if argv[3] == "CRT":
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask R'].image.filepath = crt_shadowmask[0]
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask G'].image.filepath = crt_shadowmask[1]
  bpy.data.materials["TV-CRT"].node_tree.nodes['phosphor shadowmask B'].image.filepath = crt_shadowmask[2]