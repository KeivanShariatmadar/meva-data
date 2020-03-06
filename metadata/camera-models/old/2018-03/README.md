This directory contains the geometric scene model for the March 2018
MEVA data collection.  The format of the data is a common coordinate
system containing a calibrated camera model for each camera and a
collection of 3D landmark points with their annotated 2D locations in
each image that sees them.  Additionally the model is georegistered.

This directory contains models covering a subset of the public
cameras.  We started with the stationary (non-patrolling)
RGB cameras that are outdoors and have overlapping fields of view.
In the future we will add models for IR cameras and each state of
the patrolling cameras.  We may also provide model of indoor cameras,
but these will likely be in different local coordinates that are
not georegistered.

The data is structured as follows:

* [cameras](cameras) is a directory of camera files, one per camera
  id/state.  Refer to the [cameras readme](cameras/README.md)
  for details on the format.

* [frames](frames) is a directory of sample images, one per camera
  id/state.  The file names match the camera names, but with a different
  file extension.  These files are mostly here for convenience to help
  visualize the geometry in the image space without needing the video.

* [frames.txt](frames.txt) is an ordered list of the frames (and
  corresponding cameras) that are currently considered for the model.
  The order of the image name in this file assigned it an integer index.
  The first line in this file is camera 1, the second is 2, and so on.

* [tracks.txt](tracks.txt) is a text file containing the image location
  of selected landmark points in each image.  Each line provides a the
  following `track_id camera_id X_loc Y_loc`.  There are several other
  fields that appear on each line as well, but these are currently not
  used for this application and appear as default values
  `1 1 0 255 255 255 0`.  The `camera_id` indicates the camera index
  that sees the current landmark, it match the line number in `frames.txt`.

* [landmarks.ply](landmarks.ply) is sparse 3D point cloud of selected
  landmark points.  PLY is a standard ASCII file format for 3D mesh
  and point data.  The header documents the order of the fields.  The
  relevant fields are the first three, `X Y Z` location, and the last
  two `track_id observations`.  The `track_id` is a unique number for
  each track/landmark and matches the `track_id` in `tracks.txt`.  The
  `observations` field indicates the number of cameras that see the
  landmark.  You can open PLY files in many 3D applications such as
  [MeshLab](http://www.meshlab.net/) and [Blender](https://www.blender.org).

* [gcps.json](gcps.json) is a geo-JSON formatted file that contains
  a few manually selected ground control points (GCPs) that were used
  to georegister the coordinate system.  You should not need to use
  these GCPs directly, see `geo_origin.txt`.

* [geo_origin.txt](geo_origin.txt) a simple ASCII file containing only
  three numbers: `latitude longitude elevation` in WGS84.  This is the
  location of the origin of the local cartesian coordinate system in
  geographic coordinates.

* [meva-2018-03-telesculptor.conf](meva-2018-03-telesculptor.conf)
  This is an optional project configuration file that enables loading
  all of the above data into the open source
  [TeleSculptor](https://github.com/kitware/TeleSculptor) application
  for visualization of the camera geometry.  TeleSculptor, along with
  other tools, was used to build this model.  If you have all of the data
  checked out and have TeleSculptor v1.0 you can use
  `File -> Open Project` and select this file to view the data.

* [homographies](homographies) (coming soon) contains alternative models for direct
  image-to-image mapping with a homography transformation.  These models
  are only applied in cases of co-located RGB and IR cameras that have similar viewpoints and minimal parallax.
