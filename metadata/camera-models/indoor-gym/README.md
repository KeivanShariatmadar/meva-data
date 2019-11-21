This directory contains the geometric scene model for the Gym in the
MEVA data collection.  The format of the data is a common coordinate
system containing a calibrated camera model for each camera and a
collection of 3D landmark points with their annotated 2D locations in
each image that sees them.  The coordinates are local to the Gym and
do not relate to the outdoor or any other indoor models.

The data is structured as follows:

* [2018-03](2018-03) is a directory of camera files for the March
  collect in the gym. Refer to the [readme](2018-03/README.md)
  for details on the format.
