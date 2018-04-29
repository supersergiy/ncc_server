from flask import Flask
from scipy.io import loadmat, savemat
from scipy.ndimage import imread
from flask import request

app = Flask(__name__)
output_rect_path = '/tmp/output_rect.mat'

@app.route('/process')
def process():
   frames_path = request.args.get('frames_path')
   frames = loadmat(frames_path)['frames']
   rect_path = request.args.get('rect_path')
   init_rect = loadmat(rect_path)['rect'][0]

   out_rects = []
   for f in frames:
       image_path = f[0][0]
       image_data = imread(image_path)
       ## Result bounding box computation:
       # TODO
       result_bbox = init_rect
       out_rects.append(result_bbox)

   savemat(output_rect_path, {"out_rects": out_rects})
   return output_rect_path


