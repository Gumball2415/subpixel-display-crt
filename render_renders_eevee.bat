@echo off

REM issues with running in the background
REM del renders\yoeyrom1_0.png
blender subpixel_example.blend -o //renders/yoeyrom1_#.png -F PNG -E BLENDER_EEVEE -t 0 --python render_renders.py -f 0 -- "Camera 7" "//texture/yoeyrom_crt_000.png" 900 PVM 0

REM del renders\yoeyrom2_0.png
blender subpixel_example.blend -o //renders/yoeyrom2_#.png -F PNG -E BLENDER_EEVEE -t 0 --python render_renders.py -f 0 -- "Camera 8" "//texture/yoeyrom_crt_000.png" 900 PVM 0

rem Camera 7: yoeyrom1.png
rem Camera 8: yoeyrom2.png