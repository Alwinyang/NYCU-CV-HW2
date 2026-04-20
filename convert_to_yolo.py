import json
import os

def convert(json_path, image_dir, label_dir):
    os.makedirs(label_dir, exist_ok=True)

    with open(json_path, 'r') as f:
        data = json.load(f)

    images = {img['id']: img for img in data['images']}

    ann_dict = {}
    for ann in data['annotations']:
        img_id = ann['image_id']
        ann_dict.setdefault(img_id, []).append(ann)

    for img_id, img_info in images.items():
        file_name = img_info['file_name']
        name = os.path.splitext(file_name)[0]

        label_path = os.path.join(label_dir, name + ".txt")

        w = img_info['width']
        h = img_info['height']

        with open(label_path, 'w') as f:
            if img_id in ann_dict:
                for ann in ann_dict[img_id]:
                    x, y, bw, bh = ann['bbox']
      
                    cls = ann['category_id'] - 1
                    x_center = (x + bw / 2) / w
                    y_center = (y + bh / 2) / h
                    bw /= w
                    bh /= h

                    f.write(f"{cls} {x_center} {y_center} {bw} {bh}\n")

    print(f"Done: {json_path}")

if __name__ == "__main__":
    convert("data/train.json", "data/images/train", "data/labels/train")
    convert("data/valid.json", "data/images/valid", "data/labels/valid")