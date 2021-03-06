# MEVA-Data-Repo Documentation

This directory contains documentation for the MEVA dataset.

* [The MEVA Annotation Definitions](MEVA-Annotation-Definitions.pdf) defines the activities and objects which are being evaluated as part of the [NIST ActEV SDL evaluation](https://actev.nist.gov).

* [The KPF annotation specification](KPF-specification-v4.pdf) describes the YAML-based schemas used to annotate the activities and objects.

* [The NIST json schemas](nist-json-for-actev) are derived from the KPF and are used by NIST for scoring in ActEV.

* Activity names: In February 2020 the activity names were normalized:

  * The [activity-names.txt](activity-names.txt) file lists the canonical names for the 37 ActEV activities. Note that these names are case-sensitive.

  * The [activity-name-mapping.csv](activity-name-mapping.csv) file is a comma-separated file mapping "old" (pre-February 2020) names to their canonical equivalent. This file includes variations for capitalization.
