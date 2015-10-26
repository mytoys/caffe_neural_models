# Specify the path caffe here
caffe_path = "../../caffe_gt"
# Specify wether or not to compile caffe
library_compile = True

# Specify the device to use
device_id = 0

# Specify the solver file
solver_proto = "net/solver.prototxt"

output_dims = [44, 44, 44]
input_padding = [88, 88, 88]

border_reflect = False

# Select "train" or "process"
mode = "train"