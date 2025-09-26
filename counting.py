import os
from collections import defaultdict

# Base dataset path
base_dir = r"C:\Users\Stoic\OneDrive\Desktop\Waste-Sorter\datasets"

splits = ["train", "valid", "test"]

# Overall counters
total_annotations = defaultdict(int)
total_images = defaultdict(int)


def process_labels(labels_dir):
    """Process a labels directory and return per-class counts."""
    annotation_counts = defaultdict(int)
    image_counts = defaultdict(int)

    if not os.path.exists(labels_dir):
        return annotation_counts, image_counts

    for file in os.listdir(labels_dir):
        if not file.endswith(".txt"):
            continue

        filepath = os.path.join(labels_dir, file)

        with open(filepath, "r") as f:
            lines = f.readlines()

        classes_in_image = set()
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0].startswith("#"):
                continue

            try:
                class_id = int(parts[0])
            except ValueError:
                continue

            annotation_counts[class_id] += 1
            classes_in_image.add(class_id)

        for cid in classes_in_image:
            image_counts[cid] += 1

    return annotation_counts, image_counts


# Process each split
for split in splits:
    labels_dir = os.path.join(base_dir, split, "labels")
    ann_counts, img_counts = process_labels(labels_dir)

    print(f"\n=== {split.upper()} SPLIT ===")
    print("Annotations per class:")
    for cid, count in sorted(ann_counts.items()):
        print(f"Class {cid}: {count} annotations")

    print("Images containing each class:")
    for cid, count in sorted(img_counts.items()):
        print(f"Class {cid}: {count} images")

    # Add to totals
    for k, v in ann_counts.items():
        total_annotations[k] += v
    for k, v in img_counts.items():
        total_images[k] += v

# Print combined summary
print("\n=== TOTAL DATASET SUMMARY ===")
print("Annotations per class:")
for cid, count in sorted(total_annotations.items()):
    print(f"Class {cid}: {count} annotations")

print("\nImages containing each class:")
for cid, count in sorted(total_images.items()):
    print(f"Class {cid}: {count} images")
