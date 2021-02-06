import fnmatch
import json
import os
from collections import defaultdict

import cv2
import numpy as np
from filevideostream1 import FileVideoStream
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def recglob(directory, ext):
    lst = []
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, ext):
            lst.append(os.path.join(root, filename))
    return lst


def load_annotations(filename):
    d = {}
    with open(filename) as f:
        d = json.loads(f.read())
    return d


def overlay(videofile, annotations):
    print(annotations)
    fnt_small = ImageFont.truetype("FreeMono.ttf", 25)
    dframesf = defaultdict(list)
    dactsf = defaultdict(list)
    for item in annotations:
        # print(annotations[item]['trajectory'])
        # print(annotations[item]["event_type"])

        dframes = defaultdict(list)
        dacts = defaultdict(list)
        for x in annotations[item]["trajectory"]:
            # print(x)
            dframes[int(x)].append(annotations[item]["trajectory"][x])
            dacts[int(x)].append(annotations[item]["event_type"])

        mnx = float('Inf')
        mny = float('Inf')
        mxx = -float('Inf')
        mxy = -float('Inf')
        for k in dframes:
            if dframes[k][0][0] < mnx:
                mnx = dframes[k][0][0]

            if dframes[k][0][1] < mny:
                mny = dframes[k][0][1]

            if dframes[k][0][2] > mxx:
                mxx = dframes[k][0][2]

            if dframes[k][0][3] > mxy:
                mxy = dframes[k][0][3]

        for k in range(
            annotations[item]["start_frame"], annotations[item]["end_frame"],
        ):
            dframesf[k].append([mnx, mny, mxx, mxy])
            dactsf[k].append(annotations[item]["event_type"])

    cv2.namedWindow("image")
    cap = FileVideoStream(videofile).start()
    frameno = 0
    while cap.more():
        frame = cap.read()
        try:
            if not frame:
                continue
        except ValueError:
            pass

        if frameno % 5 == 0:
            im_pil = Image.fromarray(frame[:, :, ::-1])
            (x, _) = im_pil.size

            draw = ImageDraw.Draw(im_pil)

            # print(frameno)

            for q, act in zip(dframesf[frameno], dactsf[frameno]):

                # print(q)
                color = (0, 255, 0)

                draw.text((q[0], q[1]), act, color, font=fnt_small)
                for i in range(2):
                    draw.rectangle(
                        ((q[0] + i), (q[1] + i), (q[2] + i), (q[3] + i)),
                        outline=color,
                        fill=None,
                    )

            imcv = np.array(im_pil)
            imcv = imcv[:, :, ::-1].copy()
            cv2.imshow("image", imcv)
            if cv2.waitKey(1) == ord(" "):
                cv2.waitKey(-1)

        frameno = frameno + 1


def main():
    # video location, you need a flat directory with all the videos:
    video_location = "d:/meva/"

    lst = recglob(video_location, "*.avi")
    print(len(lst))
    olist = []

    for videofile in lst:
        total_instances = 0
        annot_files = []
        for x in ['']:
            path = 'cuboids'
            vf = videofile.split("/")[-1].replace(".avi", "").replace(".", "_") + ".json"
            annotfile = os.path.join(path, vf)
            print(annotfile)
            if os.path.exists(annotfile):
                d = load_annotations(annotfile)
                total_instances = total_instances + len(d)
                annot_files.append(annotfile)
        if total_instances > 0:
            olist.append((total_instances, annot_files, videofile))

    print("------------------------------")
    olist = sorted(olist, reverse=True)
    for (_, annot_files, videofile) in olist:
        # if len(annot_files) == 1:
        #     continue
        dfull = {}
        count = 0
        for annotfile in annot_files:
            print(annotfile)
            print(annot_files)
            if os.path.exists(annotfile):
                d = load_annotations(annotfile)
                for item in d:
                    dfull[str(count)] = d[item]
                    count = count + 1
                print(len(d))
        overlay(videofile, dfull)


if __name__ == "__main__":
    main()
