from flask import Flask
from scipy.io import loadmat, savemat
from flask import request

app = Flask(__name__)
output_rect_path = '/tmp/output_rect.mat'

@app.route('/process')
def process():
   frames_path = request.args.get('frames_path')
   frames = loadmat(frames_path)['frames']
   rect_path = request.args.get('rect_path')
   rect = loadmat(rect_path)['rect']
   out_rects = []
   for f in frames:
       out_rects.append(rect[0])
   #import pdb; pdb.set_trace()
   savemat(output_rect_path, {"out_rects": out_rects})
   return output_rect_path


