import yaml
import os
from collections import Counter
import shutil

dataset_yaml_path = "dataset/data.yaml"
with open(dataset_yaml_path) as f:
    data = yaml.load(f)

dataset_dir = os.path.dirname(dataset_yaml_path)

dirs = {
    "train": {
        "images": os.path.join("dataset", "train", "images"), 
        "labels": os.path.join("dataset", "train", "labels")
    },
    "val": {
        "images": os.path.join("dataset", "valid", "images"), 
        "labels": os.path.join("dataset", "valid", "labels")
    },
    "test": {
        "images": os.path.join("dataset", "test", "images"), 
        "labels": os.path.join("dataset", "test", "labels")
    }
}

classes = data['names']
filtered_ds_name = "filtered_dataset"
min_boxes = 1000

# filtered dataset output folder
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(filtered_ds_name, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(filtered_ds_name, split, "labels"), exist_ok=True)

# number of boxes per class
counter = Counter()
for split in ["train", "val", "test"]:
    label_dir = dirs[split]["labels"]
    
    print(f"Processing {split} labels from: {label_dir}")
    label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]
    print(f"  Found {len(label_files)} label files")
    
    for label_file in label_files:
        label_path = os.path.join(label_dir, label_file)
        with open(label_path) as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    class_id = int(line.split()[0])
                    counter[class_id] += 1

print(f"\nClass counts: {dict(counter)}")

classes_enough = {cls for cls, count in counter.items() if count >= min_boxes}
print(f"Classes with >= {min_boxes} boxes: {classes_enough}")

if not classes_enough:
    print("No classes meet the minimum box requirement!")
    exit(1)

old_to_new = {old: new for new, old in enumerate(sorted(classes_enough))}
new_names = [classes[old] for old in sorted(classes_enough)]
print(f"Class mapping: {old_to_new}")
print(f"New class names: {new_names}")

# Function to filter labels and copy images
def filter_labels(src_labels_dir, src_images_dir, dst_labels_dir, dst_images_dir):
    if not os.path.exists(src_labels_dir):
        print(f"Source labels directory doesn't exist: {src_labels_dir}")
        return
    
    label_files = [f for f in os.listdir(src_labels_dir) if f.endswith(".txt")]
    copied_count = 0
    
    for f in label_files:
        src_label_path = os.path.join(src_labels_dir, f)
        new_lines = []
        
        try:
            with open(src_label_path) as file:
                for line in file:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue
                    parts = line.split()
                    class_id = int(parts[0])
                    if class_id in old_to_new:
                        parts[0] = str(old_to_new[class_id])
                        new_lines.append(" ".join(parts) + "\n")
        except Exception as e:
            print(f"Error reading {f}: {e}")
            continue
        
        if not new_lines:
            continue
        
        # Write filtered labels
        dst_label_path = os.path.join(dst_labels_dir, f)
        with open(dst_label_path, "w") as out_file:
            out_file.writelines(new_lines)
        
        # Copy corresponding image
        img_name_base = f.replace(".txt", "")
        image_copied = False
        
        for ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
            src_img_path = os.path.join(src_images_dir, img_name_base + ext)
            if os.path.exists(src_img_path):
                dst_img_path = os.path.join(dst_images_dir, img_name_base + ext)
                shutil.copy2(src_img_path, dst_img_path)
                image_copied = True
                break
        
        if image_copied:
            copied_count += 1
        else:
            print(f"Warning: No image found for {img_name_base}")
    
    print(f"  Copied {copied_count} image-label pairs")

# Filter all splits
print("\nFiltering datasets...")
for split in ["train", "val", "test"]:
    print(f"Processing {split}...")
    filter_labels(
        dirs[split]["labels"],
        dirs[split]["images"],
        os.path.join(filtered_ds_name, split, "labels"),
        os.path.join(filtered_ds_name, split, "images")
    )

# new dataset
new_data_yaml = {
    'train': os.path.join("train", "images"),
    'val': os.path.join("val", "images"), 
    'test': os.path.join("test", "images"),
    'nc': len(new_names),
    'names': new_names
}

output_yaml_path = os.path.join(filtered_ds_name, "data.yaml")
with open(output_yaml_path, "w") as f:
    yaml.dump(new_data_yaml, f, default_flow_style=False)

print(f"Original classes: {len(classes)} -> Filtered classes: {len(new_names)}")
