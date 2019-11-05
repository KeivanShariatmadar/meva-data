File: meva-data-repo/annotation/README.txt

1. Overview.  

This direction contains a sub-directory for each form of annotation
performed on the MEVA data.  Crowd-supported annotations will be
provided within this directory when they become available.

Presently, there is a single directory 'DIVA-phase-2' which holds the
example annotations of the Known Facililty Data annotated by Kitware
Inc. according to the activity definitions in
'meva-data-repo/documents/MEVA-Annotation-Definitions.pdf' and
provided as JSON-formatted files described in
'meva-data-repo/documents/MEVA_Annotation_JSON.pdf'.

2. Directory Structure

The data structure within the annotation directory is as follows:

annotation/
   <ANNOTATION_TYPE>/
      documents/
      activity-index.json
      <DATASET>/   
          <ANNOTATION_DROP_NAME>/
	      <RECORDING_DATE>/
                  <RECORDING_BEGIN_HOUR>/
                       <FILE_NAME>.<FILETYPE>


<ANNOTATION_TYPE> - This directory contains homogenously prepared
annotations using a single standard.  If the annotations deviate in
any manor from the top-level documents, specializtion documentation
will be found in the documentation directory in the annotation type
dir.  

activity-index.json - The activity JSON that applies to all
annotations within the directory.

<DATASET> - The name of the data set as a hole, e.g., MEVA, VIRAT, etc.

<ANNOTATION_DROP_NAME> - Second level collection for release sets.
The naming convention is flexible.

<RECORDING_DATE> - The date (YYYY-MM-DD) of the recordings stored
within the directory.

<RECORDING_BEGIN_HOUR> - The 24-hour hour of the recordings stored
within the directory.

<FILE_NAME>.<FILETYPE> - The file name and file types of each video's
annotation.  The file name should not include the media file
extension.  The file types of conformant annotations are:
   
      .activities.json
      .file-index.json  


3. Contributing Annotations

The annotation directory is designed to hold contributed annotations
from the community.  The contribution process is simple - add your data
to a branch that you create and then send a merge request.  The
moderators will review the structure and accept the merge request when
completed.  Here're the detailed steps (See a git cheat sheets if
you're new to git.)

2.1 Clone the meva-data repo and make a branch:

% git clone git@gitlab.kitware.com:meva/meva-data-repo.git
% cd meva-data-repo
% git checkout -b <YOURBRANCH>

2.2 Make a directory structure that matches the
[DIVA-phase-2](DIVA-phase-2) annotations. (See Section 2 above)

2.3 Add, commit and push your changes to git repo

% git add <YOURFILES>
% git commit
% git push -u origin <YOURBRANCH>

2.4 Issue a merge request 

- Navigate a web browser to  https://gitlab.kitware.com/meva/meva-data-repo
- Click "Create merge request"
- Write a description
- For "Source Branch", select <YOURBRANCH>
- Leave "Target Branch" as master
- Select Assignee "Jon Fiscus"
- Click "Delete source branch when merge request is accepted."
- Click "Squash commits when merge request is accepted."
- Click "Submit merge request"

2.5 Work with the moderator to conform to standards

If the moderator asks for revisions, add, commit, and push revisions
to resovle the issues as needed.
