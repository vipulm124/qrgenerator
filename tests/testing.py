from qrgenerator import QRGenerator
from qrgenerator.themes import THEMES_DICT,  ThemesEnum
from dataclasses import dataclass
from qrgenerator.generator import QRConfig




output_file = "qr_code_anotherone_saved3.png"
default_config = QRConfig(version=4, show_logo=True, logo_path="tests/python.webp", show_theme=False, color_positiond_detection_corners=True, custom_finder_pattern_color="#96CC38")
qrcode_generator = QRGenerator(default_config)
qrcode_ready_to_save = qrcode_generator.generate_qr_code("https://www.google.com", output_file=output_file)
if qrcode_ready_to_save is not None:
    qrcode_ready_to_save.save(output_file)