The clip table is a file containing information about how individual
clips relate to others in space (via camera models) and time (via
reference cameras and frame offsets.)

Each line has seven fields, some of which have special values for
exceptional conditions.

* clip name
* reference time slot
* camera file
* camera set
* reference time clip
* reference time frame offset
* reference time offset precision

The fields are interpreted as follows:

``clip name``: The prefix of the video clip; all other data on
the line relates to this clip.

``reference time slot``: The "normalized" five-minute time slot of the
clip.

``camera file``: The KRTD camera file associated with this clip, or
'no-camera-model' if no camera model is available.

``camera set``: The camera set to which this camera belongs. A camera
set is a group of cameras which share sufficient field-of-view that
some degree of frame-level synchronization is possible. This field is
a string which is either 'N-M', where N and M are numbers, or 'IR', or 'skip'.

 * 'N-M' (e.g. '3-638', or '5-423'): The first number is either 3
   (March) or 5 (May); the second is the camera ID of the reference
   camera. For example, clip 2018-03-11.16-45-00.16-50-00.bus.G509
   belongs to camera set "3-508", which is the March configuration of
   cameras using G508 as the reference camera.

 * 'IR': The IR cameras have not been incorporated into the camera
   topology yet.

 * 'skip': Some cameras, for example any PTZ cameras in patrol mode,
 have not yet been assigned to a camera set.

``reference time clip``: Either the name of a clip, the string 'self',
or the string 'no-reference-clip-available'. If a clip is named, that
clip is the clip belonging to the reference camera which shares the
same reference time slot as this clip. 'self' is an optimization
meaning that this clip is its own reference. No reference clip is
available either when the clip does not belong to a camera set or
(more rarely) when the reference camera was not recording in this
reference time slot (for example, at the start or end of recording
sessions.) (The reference time clip is essentially the clip of the
reference camera in the *camera set* field which shares the same
*reference time slot* with this clip.)

``reference time frame offset``: The frame offset between this clip
and its reference clip (if any). Only valid when the reference time
frame precision (next field) is not -1. For example, if this is clip
A, the reference clip is B, and the offset is 300, then frame 73 in
clip A should be the same world time as 73 + 300 == 373 in clip
B. This value is always zero when the reference time clip is 'self'.

``reference time offset precision``: A number N such that the offset
equation above is accutate to within +/- N frames. If N == -1, no
offset is available.
