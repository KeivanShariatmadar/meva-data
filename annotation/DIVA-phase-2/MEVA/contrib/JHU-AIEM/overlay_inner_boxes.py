import fnmatch
import json
import os
import pickle
import random
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


def find_closest(lst, f):
    return min(lst, key=lambda x: abs(x - f))


def overlay(skeys, videofile, annotations):
    activities = defaultdict(list)
    for (key, activity) in skeys:
        for pos, w in enumerate(annotations[(key, activity)]):
            # print(activity)
            # print(w["rects_by_frame"])
            mn = min(w["rects_by_frame"].keys())
            mx = max(w["rects_by_frame"].keys())
            for frame_t in range(mn, mx + 1):
                frame = find_closest(w["rects_by_frame"].keys(), frame_t)
                for i in range(len(w["rects_by_frame"][frame])):
                    x1 = int(round(w["rects_by_frame"][frame][i]["x1"]))
                    x2 = int(round(w["rects_by_frame"][frame][i]["x2"]))
                    y1 = int(round(w["rects_by_frame"][frame][i]["y1"]))
                    y2 = int(round(w["rects_by_frame"][frame][i]["y2"]))
                    activities[frame_t].append(
                        (activity + " id:" + str(w['identity']), x1, y1, x2, y2),
                    )

    cv2.namedWindow("image")
    cap = FileVideoStream(videofile).start()
    frameno = 0
    fnt_small = ImageFont.truetype("FreeMono.ttf", 25)
    while cap.more():
        frame = cap.read()
        try:
            if not frame:
                continue
        except ValueError:
            pass

        if frameno % 10 == 0:
            im_pil = Image.fromarray(frame[:, :, ::-1])

            draw = ImageDraw.Draw(im_pil)
            color = (0, 255, 0)
            for u in activities[frameno]:
                draw.text((u[1], u[2]), u[0], color, font=fnt_small)
                draw.rectangle((u[1], u[2], u[3], u[4]), outline=color, fill=None)

            # print(frameno)

            imcv = np.array(im_pil)
            imcv = imcv[:, :, ::-1].copy()
            cv2.imshow("image", imcv)
            if cv2.waitKey(1) == ord(" "):
                cv2.waitKey(-1)

        frameno = frameno + 1


def main():
    # video location, you need a flat directory with all the videos:
    video_location = "d:/meva/"
    annot = defaultdict(list)
    for x in ['-1']:
        filename = 'edited-mturked-annots{case}.pkl'.format(
            case=x,
        )
        annot_inner = pickle.load(open(filename, 'rb'))
        for (videoname, activity) in annot_inner:
            annot[(videoname, activity)].extend(
                annot_inner[(
                    videoname,
                    activity,
                )],
            )

    lst = recglob(video_location, "*.avi")
    print(len(lst))
    olist = []

    keys = annot.keys()
    for videofile in lst:

        skeys = []
        for (a, b) in keys:
            if a == videofile.split("/")[-1]:
                skeys.append((a, b))
        cnt = 0
        for (a, b) in skeys:
            cnt = cnt + len(annot[(a, b)])
        olist.append((cnt, videofile))

    print("------------------------------")
    olist = sorted(olist, reverse=True)
    # random.shuffle(olist)
    # olist = olist[50:]
    for (_, videofile) in olist:
        skeys = []
        for (a, b) in keys:
            if a == videofile.split("/")[-1]:
                skeys.append((a, b))

        overlay(skeys, videofile, annot)


if __name__ == "__main__":
    main()
