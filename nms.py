import numpy as np

#malisiewicz et al
def non_max_suppression(boxes, overlapThresh):
    #if no boxes, return empty list
    if len(boxes) == 0:
        return []

    #if bounding boxes are int, convert to float
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    #initialize list of picked indexes
    pick = []

    #coords of bounding boxes
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]

    #compute area of bounding boxes and sort them by bottom-right y coord of bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    #keep looping while some indexes remain in indexes list
    while len(idxs) > 0:
        #grab last index in indexes list and add the index value to list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        #find largest x and y coord for start of bounding box
        #and find smallest x and y coord for end of bounding box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

	#compute width and height of bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

	#compute ratio of overlap
        overlap = (w * h) / area[idxs[:last]]

	#delete all indexes from the index list
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    #return only bounding boxes that were pickedd using integer data type
    return boxes[pick].astype("int")
    
