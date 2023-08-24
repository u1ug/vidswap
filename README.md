# vidswap

A python script for swapping faces in the video

## How to:

1. Clone repository and install dependencies
```
git clone https://github.com/u1ug/vidswap
cd vidswap
pip install -r requirements.txt
```
2. Download model weights [from here](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view) and palce them to project directory
3. Edit config.json for your files
```
{
  "input_video": "input.mp4", // Path for source video 
  "face_image": "face.jpg",  // Face image replace to
  "output_video:": "output.mp4" // Name for output video file
}
```
4. Run script
``python main.py``
