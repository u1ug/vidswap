from settings.settings import Settings
from swapper.swapper import Swapper


def main():
    config = Settings()
    config.read_config("config.json")
    swapper = Swapper(
        config.get('input_video'),
        config.get('face_image'),
        config.get('output_video')
    )
    swapper.process()


if __name__ == '__main__':
    main()
