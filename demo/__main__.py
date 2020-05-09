import demo
import os

if not os.path.isdir(".\\demo"):
    raise IOError("This should be run from the \\birds directory.")

demo.frame_nn.main()
