from PIL import Image
import numpy as np

def bw_convert(path):
    image = Image.open(path)
    
    A = np.asarray(image, dtype=np.uint8)
    k = np.array([0.2989, 0.587, 0.114])
    
    w, h, _ = A.shape
    A.reshape(w * h, 3)
    
    out = np.matmul(A, k)
    out.reshape(w, h)
    
    image_out = Image.fromarray(out.astype(np.uint8))
    image_out.save("./data/cat_2.jpg")

bw_convert("./data/cat.jpg")