This directory contains camera calibration (intrinsic and extrinsic)
for the Gym in the MEVA data collection.  The goal is to provide camera
models in a common coordinate system to allow tools to project points
from one camera into the world space and then into other cameras. The
local camera coordinate system is scaled to units of meters.  The Z=0
plane is roughly aligned with the ground with the origin at the center
of the basketball court.

The data here is stored in KRTD format. 
KRTD is an ASCII file containing the following matrices:

K - 3x3 upper triangular intrinisic matrix encoding focal length,
    principal point, skew, pixel aspect ratio.

R - 3x3 orthonormal rotation matrix

T - 3d translation vector 

D - Nd vector of lens distortion parameters (using OpenCV conventions)
