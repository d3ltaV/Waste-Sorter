# Waste-Sorter
A program that determines if an object in an image should go to recycling, trash, or compost.


## Model

### Dataset

The YOLO formatted TACO dataset was used in training: https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format

The TACO dataset has 18 classes:
Aluminium foil, Battery, Blister pack, Bottle, Bottle cap, Broken glass, Can, Carton, Cigarette, Cup, Food waste, Glass jar, Lid, Paper, Paper bag, Plastic bag & wrapper, Plastic container, Plastic gloves, Plastic utensils, Pop tab, Rope, Scrap metal, Shoe, Squeezable tube, Straw, Styrofoam piece, Other plastic, Unlabeled litter

Which were merged into the following:
Recycling, Trash, Compost

### Training
The model was trained in three phases:
1. YOLOv8s with Adam optimizer for 100 Epochs
2. last.pt was then trained with SGD for 200 Epochs
3. last.pt from step 2 was trained with SGD for 150 epochs with augmentation=True

The inspiration for this training style came from this paper: https://www.opt-ml.org/papers/2021/paper53.pdf


### File Structure (CURRENT)
- **static/css/** — CSS for the GUI  
- **templates/** — HTML template for the GUI  
- **main.py** — Main interface for program  
- **model.py** — file where hyperparameters are edited and the model is trained  
- **utils.py** — helper functions


