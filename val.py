from ultralytics import YOLO

if __name__ == '__main__':
    
  model=YOLO('EdgeAnt.yaml')
  results = model.val(data='antenna.yaml', batch=1)