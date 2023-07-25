import cv2
import numpy as np

data = open("data.txt").read().split('\n')
d = [list(map(int, list(s))) for s in data]

a = np.where(np.array(d) < 9, 255, 0).astype(np.uint8)
_, _, stats, _ = cv2.connectedComponentsWithStats(a, connectivity=4)
print(_, _, stats, _)

n = sorted([i[-1] for i in stats[1:]])[-3:]

print(n[0] * n[1] * n[2])