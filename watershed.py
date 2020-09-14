import numpy as np
import cv2

    
def show():
    global windowname,dests
    cv2.imshow(windowname, dests[0])

def on_mouse(event, x, y, flags, param):
    global prev_pt,dirty
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        prev_pt = pt
    elif event == cv2.EVENT_LBUTTONUP:
        prev_pt = None

    if prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
        for dst, color in zip(dests, colors_func()):
            cv2.line(dst, prev_pt, pt, color, 5)
        dirty = True
        prev_pt = pt
        show()
        
def get_colors():
    return list(map(int, colors[marker_color])), marker_color

def watershed():
    m = markers.copy()
    cv2.watershed(img, m)
    overlay = colors[np.maximum(m, 0)]
    vis = cv2.addWeighted(img, 0.5, overlay, 0.5, 0.0, dtype=cv2.CV_8UC3)
    cv2.imshow('watershed', vis)


if __name__ == '__main__':
    path = './data/pothole1.jpg'
    img = cv2.imread(path)
    if img is None:
        raise Exception('Failed to load image file: %s' %path)
    
    #grab height and width of org image
    h, w = img.shape[:2]
    #initiate marker array 
    markers = np.zeros((h, w), np.int32)
    markers_vis = img.copy()
    marker_color = 1

    #define array of 7 colors
    colors = np.int32( list(np.ndindex(2, 2, 2)) ) * 255
    #decalare variaables
    windowname = 'img'
    dests = [markers_vis, markers]
    colors_func = get_colors
    auto_update = True
    dirty = False
    prev_pt = None
    show()
    cv2.setMouseCallback(windowname, on_mouse)

    while cv2.getWindowProperty('img', 0) != -1 or cv2.getWindowProperty('watershed', 0) != -1:
        ch = cv2.waitKey(50)
        if ch == 27:
            break
        if ch >= ord('1') and ch <= ord('7'):
            marker_color = ch - ord('0')
            print('marker: ', marker_color)
        if ch == ord(' ') or (dirty and auto_update):
            watershed()
            dirty = False
        if ch in [ord('a'), ord('A')]:
            auto_update = not auto_update
            print('auto_update if', ['off', 'on'][auto_update])
        if ch in [ord('r'), ord('R')]:
            markers[:] = 0
            markers_vis[:] = img
            show()
    cv2.destroyAllWindows()
