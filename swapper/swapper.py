import cv2
import os
import sys
import insightface
from insightface.app import FaceAnalysis
from tqdm import tqdm

_swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False, download_zip=False)


def face_swap_on_frame(input_frame, face_to_swap_with):
    sys.stdout = open(os.devnull, 'w')  # Mute face analysis output
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    faces = app.get(input_frame)
    if not faces:
        return input_frame
    result_frame = input_frame.copy()
    for face in faces:
        result_frame = _swapper.get(result_frame, face, face_to_swap_with, paste_back=True)
    sys.stdout = open(os.devnull, 'w')
    return result_frame


class Swapper:
    def __init__(self, input_video: str, face_image: str, output_video: str):
        self._input_video = input_video
        self._face_image = face_image
        self._output_video = output_video

    def process(self):
        cap = cv2.VideoCapture(self._input_video)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        out = cv2.VideoWriter(self._output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
        me_img_path = cv2.imread(self._face_image)
        face_analysis_app = insightface.app.FaceAnalysis(name='buffalo_l')
        face_analysis_app.prepare(ctx_id=0, det_size=(640, 640))
        me_img_faces = face_analysis_app.get(me_img_path)

        me_face = me_img_faces[0] if me_img_faces else None

        if not me_face:
            raise ValueError(f"No face detected in {self._face_image}")

        for _ in tqdm(range(num_frames), desc="Processing video"):
            ret, frame = cap.read()
            if not ret:
                break
            swapped_frame = face_swap_on_frame(frame, me_face)
            out.write(swapped_frame)
        cap.release()
        out.release()
