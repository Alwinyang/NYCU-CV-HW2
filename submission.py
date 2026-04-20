import json

predictions = []

for r in results:
    image_id = int(r.path.split("/")[-1].replace(".png", ""))

    for box in r.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        predictions.append({
            "image_id": image_id,
            "category_id": cls + 1,
            "bbox": [x1, y1, x2 - x1, y2 - y1],
            "score": conf
        })

with open("pred.json", "w") as f:
    json.dump(predictions, f)

print("done,", len(predictions))
print(predictions[:3])