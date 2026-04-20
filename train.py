from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="C:/HW2/data.yaml",
        epochs=5,
        imgsz=416,
        batch=8,
        device="cpu",
        workers=0,
        plots=False,
        amp=False,
        project="runs",
        name="digit_train_cpu"
    )

if __name__ == "__main__":
    main()