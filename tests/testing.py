from qrstyler import QRGenerator
from qrstyler.themes import THEMES_DICT,  ThemesEnum
from dataclasses import dataclass
from qrstyler.generator import QRConfig




output_file = "qr_code_anotherone_saved3.png"
default_config = QRConfig(version=4, show_logo=True, theme=ThemesEnum.WHATSAPP, show_theme=False, color_positiond_detection_corners=True, custom_finder_pattern_color="#96CC38")
qrcode_generator = QRGenerator(default_config)
qrcode_ready_to_save = qrcode_generator.generate_qr_code("https://www.google.com", output_file=output_file)
if qrcode_ready_to_save is not None:
    qrcode_ready_to_save.save(output_file)

config = QRConfig(
    version=6,
    show_logo=True,
    show_theme=True,
    theme=ThemesEnum.LINKEDIN,
    color_positiond_detection_corners=True,
    custom_finder_pattern_color="#051F57",
    custom_theme_color="#4387E7",
    box_size=10,
    border=4,
)
qrgen = QRGenerator(config)
qrgen.generate_qr_code("https://www.linkedin.com/in/vipul-malhotra-5545b829/", output_file="linkedin_qr.png")