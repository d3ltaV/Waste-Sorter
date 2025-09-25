
object_categories = {
# recyclable materials
    "aluminum foil": "recycling",  # just in case of spelling variants
    "bottle": "recycling",
    "bottle cap": "recycling",
    "can": "recycling",
    "carton": "recycling",
    "glass jar": "recycling",
    "lid": "recycling",
    "paper": "recycling",
    "paper bag": "recycling",
    "plastic container": "recycling",
    "pop tab": "recycling",
    "scrap metal": "recycling",

    # compost
    "food waste": "compost",

    # trash
    "battery": "trash",
    "blister pack": "trash",
    "broken glass": "trash",
    "cigarette": "trash",
    "cup": "trash", #double check
    "plastic bag & wrapper": "trash",
    "plastic gloves": "trash",
    "plastic utensils": "trash",
    "rope": "trash",
    "shoe": "trash",
    "squeezable tube": "trash",
    "straw": "trash",
    "styrofoam piece": "trash",
    "other plastic": "trash",
    "unlabeled litter": "trash",
}
def determine_category(class_name):
    key = class_name.strip().lower()
    return object_categories.get(key, "trash")

def map_classes(classes):
    return {c: determine_category(c) for c in classes}

def load_classes_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    return map_classes(names)
# testing psuh again












}