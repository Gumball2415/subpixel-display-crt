@echo off

del renders\testpalette_on_0.png
blender -b subpixel_example.blend -o //renders/testpalette_on_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0 -- "Camera" "//texture/full_palette_000.png" 500 CRT

del renders\testpalette_off_0.png
blender -b subpixel_example.blend -o //renders/testpalette_off_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0  -- "Camera" "//texture/full_palette_001.png" 500 CRT

del renders\testsuite1_0.png
blender -b subpixel_example.blend -o //renders/testsuite1_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0 -- "Camera 5" "//texture/240pee_000.png" 500 CRT

del renders\testsuite1_blur_0.png
blender -b subpixel_example.blend -o //renders/testsuite1_blur_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0 -- "Camera 6" "//texture/240pee_000.png" 500 CRT

del renders\testsuite2_0.png
blender -b subpixel_example.blend -o //renders/testsuite2_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0 -- "Camera 2" "//texture/240pee_000.png" 500 CRT

del renders\testsuite3_0.png
blender -b subpixel_example.blend -o //renders/testsuite3_#.png -F PNG -E CYCLES -t 0 --python render_renders.py -f 0 -- "Camera 3" "//texture/240pee_000.png" 500 CRT


rem Camera: testpalette_on, testpalette_off
rem Camera 2: testsuite2
rem Camera 3: testsuite3
rem Camera 4: ?
rem Camera 5: testsuite1.png
rem Camera 6: testsuite1_blur
