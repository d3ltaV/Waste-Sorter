# NMH Waste Sorter: Program Description

NMH Waste Sorter is built by Alan, Joelle, Lorcan, and Siddiqi. This program uses a YOLO model fine-tuned on the TACO dataset to determine if an object on camera or in an image is recyclable, compostable, or trash.

---

## Folder Structure

```bash
|WASTE-SORTER/
|   static/             
|       css/
|           home.css            # Stylization for homepage
|       img/
|       js/
|   templates/              
|       home.html               # Main page HTML
|   .gitignore                  # Ignore pycache and venv folders
|   main.py                     # Main program file
|   utils.py                    # Helper functions
|   model.py                    # Training file for model
|   webcam.py                   # Testing YOLO model for family day!
|   README.md                   # Documentation   
|
```

Model parameters are saved locally and loaded into the model.py file.

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
# Progress 09/24

- Alan: More frontend/Flask work.
- Joelle: Update README.md file, got model to run on her machine, work on eliminating classes without enough images, pushed work in progress to Github.
- Lorcan: Added SGD to improve model, which boosted mAP. Added webcam file for testing purposes, pushed to Github.
- Siddiqi: Work on function to decide which specific categories go to trash, recycling, or other.

---
# Progress 09/24

- Alan: Finish frontend work and pushed -> integrated camera feature and writing output
- Joelle: Update README.md file, tried to improve model accuracy (working on understanding data)
- Lorcan: Merged everything to MVP branch, testing functionality, look at ways of improving model accuracy
- Siddiqi: Finished function for mapping, helped test final project