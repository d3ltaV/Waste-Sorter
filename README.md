# NMH Waste Sorter: Program Description

NMH Waste Sorter is built by Alan, Joelle, Lorcan, and Siddiqi. This program uses a YOLO model fine-tuned on the TACO dataset to determine if an object on camera or in an image is recyclable, compostable, or trash.

---

## Folder Structure

```bash
|WASTE-SORTER/
|   runs/detect                 # YOLO training logs 
|   static/             
|       css/
|           home.css            # Stylization for homepage
|   templates/              
|       base.html               # Layout for homepage; calls model endpoint
|       home.html               # Fills homepage content
|   .gitignore                  # Ignore pycache and venv folders
|   README.md                   # Documentation   
|   counting.py                 # Some dataset exploration
|   main.py                     # Main program file
|   model.py                    # Training file for model
|   utils.py                    # Helper functions
|   webcam.py                   # Testing YOLO model for family day!
|
```

Datasets were indcluded inside the project directory.

---

## Dataset

The YOLO formatted TACO dataset was used in training: https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format

The TACO dataset has 18 classes:
Aluminium foil, Battery, Blister pack, Bottle, Bottle cap, Broken glass, Can, Carton, Cigarette, Cup, Food waste, Glass jar, Lid, Paper, Paper bag, Plastic bag & wrapper, Plastic container, Plastic gloves, Plastic utensils, Pop tab, Rope, Scrap metal, Shoe, Squeezable tube, Straw, Styrofoam piece, Other plastic, Unlabeled litter

Which were merged into the following:
Recycling, Trash, Compost

---

## Training

The model was trained in three phases:
1. YOLOv8s with Adam optimizer for 100 Epochs
2. last.pt was then trained with SGD for 200 Epochs
3. last.pt from step 2 was trained with SGD for 150 epochs with augmentation=True

The inspiration for this training style came from this paper: https://www.opt-ml.org/papers/2021/paper53.pdf

---

## Deployment

To deploy this program, ensure Python is installed, clone the github repository with 'git clone'. Install dependencies in the requirements.txt file, and run the **main.py** file.

---

## Task split

Alan: frontend
Lorcan: train model
Joelle: initial file structure and README.md file, model validation
Siddiqi: backend/helper functions
All: testing & debugging

---

## Progress 09/24

- Alan: More frontend/Flask work.
- Joelle: Update README.md file, got model to run on her machine, work on eliminating classes without enough images, pushed work in progress to Github.
- Lorcan: Added SGD to improve model, which boosted mAP. Added webcam file for testing purposes, pushed to Github.
- Siddiqi: Work on function to decide which specific categories go to trash, recycling, or other.

---

## Progress 09/25

- Alan: Finish frontend work and pushed -> integrated video feature and writing output
- Joelle: Update README.md file, model acc (working on understanding/preprocess data)
- Lorcan: Merged everything to MVP branch, testing functionality, look at ways of improving model accuracy
- Siddiqi: Finished function for mapping, helped test final project



