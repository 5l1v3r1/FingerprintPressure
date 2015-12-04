from scipy.fftpack import fft2, fftshift
#import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

image1 = ndimage.imread('Images/19.bmp')
F1 = fft2(image1)
F1 = fftshift(F1)
amps = []
for i in F1:
    row = []
    for j in i:
        row.append(np.abs(j))
    amps.append(row)
amps = np.array(amps)

print np.std(amps)

#plt.imshow(amps)
#plt.show()
