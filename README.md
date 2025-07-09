# QRGenerator

QRGenerator is a Python package for generating highly customizable QR codes with support for color themes, embedded logos, and more. Perfect for personal, business, or social media use cases.

## Features

- Generate QR codes for any data (URLs, text, etc.)
- Embed a logo in the center of the QR code (with border and rounded corners)
- Apply color themes for popular platforms (YouTube, LinkedIn, Instagram, etc.)
- Customize QR code size, border, and finder pattern colors
- Fully configurable via Python API
- Lightweight and easy to use

## Installation

Install via PyPI:

```bash
pip install qrgenerator
```

## Usage Example

```python
from qrgenerator import QRGenerator # Main class for creating qr codes
from qrgenerator.themes import THEMES_DICT,  ThemesEnum # to get access to theme enums and related pre-set configurations
from qrgenerator.generator import QRConfig # This dataclass is the input to the main method of QRGenerator

# Configure your QR code
config = QRConfig(
    version=4,  # QR code version (1-40), default to 1
    show_logo=True,  # Embed a logo
    logo_path="path_to_your_log.png",  # Custom logo (optional)
    show_theme=True,  # Use a color theme
    color_positiond_detection_corners=True,  # Color the finder patterns
    box_size=10,  # Size of each QR box (pixels), default to 10
    border=1,  # Border size (boxes), default to 1
    theme=ThemesEnum.LINKEDIN,  # Choose a theme (see below)
    custom_finder_pattern_color=None,  # Custom finder pattern color (hex or None)
    custom_theme_color=None,  # Custom QR body color (hex or None)
)

# Generate the QR code
qrgen = QRGenerator(config)
qrgen.generate_qr_code("https://www.linkedin.com/in/yourprofile", output_file="linkedin_qr.png")
```

## QRConfig Options

| Option                          | Type           | Default           | Description |
|---------------------------------|----------------|-------------------|-------------|
| `version`                       | int            | 1                 | QR code version (1-40, controls size/complexity) |
| `show_logo`                     | bool           | False             | Whether to embed a logo in the QR code |
| `logo_path`                     | str or None    | None              | Path to a custom logo image file |
| `show_theme`                    | bool           | False             | Whether to apply a color theme |
| `color_positiond_detection_corners` | bool       | False             | Color the finder patterns (QR corners) |
| `box_size`                      | int            | 10                | Size of each QR code box (pixels) |
| `border`                        | int            | 1                 | Border size (in boxes) |
| `theme`                         | str/enum       | ThemesEnum.DEFAULT| Theme name or enum value |
| `custom_finder_pattern_color`    | str or None    | None              | Custom color for finder patterns (hex) |
| `custom_theme_color`            | str or None    | None              | Custom color for QR code body (hex) |

## ThemesEnum Values

You can use any of the following themes for quick branding and color matching. Each theme comes with a default color scheme and logo.

| Enum Value           | Description         | Logo Used (placeholder) | Finder Pattern Color | Theme Color |
|----------------------|--------------------|------------------------|---------------------|-------------|
| `ThemesEnum.YOUTUBE`   | YouTube            | <img src="qrgenerator/icons/youtube_logo.png" width="24"/> | #FF0000 <span style="display:inline-block;width:16px;height:16px;background:#FF0000;border:1px solid #ccc;vertical-align:middle;"></span> | #F43D3D <span style="display:inline-block;width:16px;height:16px;background:#F43D3D;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.LINKEDIN`  | LinkedIn           | <img src="qrgenerator/icons/linkedin_logo.png" width="24"/> | #0077B5 <span style="display:inline-block;width:16px;height:16px;background:#0077B5;border:1px solid #ccc;vertical-align:middle;"></span> | #0077B5 <span style="display:inline-block;width:16px;height:16px;background:#0077B5;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.INSTAGRAM` | Instagram          | <img src="qrgenerator/icons/instagram_logo.png" width="24"/> | #E1306C <span style="display:inline-block;width:16px;height:16px;background:#E1306C;border:1px solid #ccc;vertical-align:middle;"></span> | #E1306C <span style="display:inline-block;width:16px;height:16px;background:#E1306C;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.FACEBOOK`  | Facebook           | <img src="qrgenerator/icons/facebook_logo.png" width="24"/> | #1877F2 <span style="display:inline-block;width:16px;height:16px;background:#1877F2;border:1px solid #ccc;vertical-align:middle;"></span> | #1877F2 <span style="display:inline-block;width:16px;height:16px;background:#1877F2;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.TWITTER`   | X (formerly Twitter)| <img src="qrgenerator/icons/x_logo.png" width="24"/> | #000000 <span style="display:inline-block;width:16px;height:16px;background:#000000;border:1px solid #ccc;vertical-align:middle;"></span> | #000000 <span style="display:inline-block;width:16px;height:16px;background:#000000;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.WHATSAPP`  | WhatsApp           | <img src="qrgenerator/icons/whatsapp_logo.png" width="24"/> | #25D366 <span style="display:inline-block;width:16px;height:16px;background:#25D366;border:1px solid #ccc;vertical-align:middle;"></span> | #25D366 <span style="display:inline-block;width:16px;height:16px;background:#25D366;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.GITHUB`    | GitHub             | <img src="qrgenerator/icons/github_logo.png" width="24"/> | #181717 <span style="display:inline-block;width:16px;height:16px;background:#181717;border:1px solid #ccc;vertical-align:middle;"></span> | #181717 <span style="display:inline-block;width:16px;height:16px;background:#181717;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.LINKTREE`  | Linktree           | <img src="qrgenerator/icons/linktree_logo.png" width="24"/> | #39D2B4 <span style="display:inline-block;width:16px;height:16px;background:#39D2B4;border:1px solid #ccc;vertical-align:middle;"></span> | #39D2B4 <span style="display:inline-block;width:16px;height:16px;background:#39D2B4;border:1px solid #ccc;vertical-align:middle;"></span> |
| `ThemesEnum.DEFAULT`   | Default (black/white)| *(No logo)* | #000000 <span style="display:inline-block;width:16px;height:16px;background:#000000;border:1px solid #ccc;vertical-align:middle;"></span> | #000000 <span style="display:inline-block;width:16px;height:16px;background:#000000;border:1px solid #ccc;vertical-align:middle;"></span> |

> **Note:** You can also provide your own logo via the `logo_path` option.

## Advanced Example

```python
from qrgenerator.generator import QRConfig, QRGenerator
from qrgenerator.themes import ThemesEnum

config = QRConfig(
    version=6,
    show_logo=True,
    show_theme=True,
    theme=ThemesEnum.INSTAGRAM,
    color_positiond_detection_corners=True,
    custom_finder_pattern_color="#FF00FF",
    custom_theme_color="#FFD700",
    box_size=12,
    border=4,
)
qrgen = QRGenerator(config)
qrgen.generate_qr_code("https://instagram.com/yourprofile", output_file="instagram_qr.png")
```

## License

This project is licensed under the MIT License.

## Contact

For issues or feature requests, please open an issue on [GitHub](https://github.com/vipulm124/qrgenerator/issues).

