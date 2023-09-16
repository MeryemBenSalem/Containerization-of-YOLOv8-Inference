
# Import required functions and classes
from sahi import AutoDetectionModel
from sahi.utils.file import download_from_url
from sahi.predict import get_sliced_prediction
from IPython.display import Image
import cv2

yolov8_model_path = 'models/yolov8l.pt'

# Download test images into demo_data folder
download_from_url('https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg', 'demo_data/small-vehicles1.jpeg')

detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.3,
    device="cuda:0", # or 'cpu'
)

result = get_sliced_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model,
    slice_height = 128,
    slice_width = 128,
    overlap_height_ratio = 0.7,
    overlap_width_ratio = 0.7
)

result.export_visuals(export_dir="demo_data/")
Image("demo_data/prediction_visual.png")

image = cv2.imread('demo_data\prediction_visual.png')
cv2.imshow('Image', image)
cv2.waitKey()
cv2.destroyAllWindows()