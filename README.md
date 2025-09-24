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