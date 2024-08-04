# Image Sorting with TensorFlow

This repository contains a Python script that uses TensorFlow's MobileNetV2 model to classify and sort images into categories. This solution is designed to help manage and organize large collections of images efficiently.

![WhatsApp Image 2024-04-25 at 15 28 48_3820506d](https://github.com/user-attachments/assets/80f0507c-8fee-4e6f-84c8-bbcb548a4707)



## Features

- **Automated Image Classification:** Uses the pre-trained MobileNetV2 model to classify images into predefined categories.
- **Efficient Sorting:** Automatically moves images into corresponding folders based on their classification.
- **Customizable Categories:** Easily update the categories and folders as needed.

## Prerequisites

- Python 3.x
- TensorFlow
- OpenCV
- Pillow

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/image-sorting-tensorflow.git
cd image-sorting-tensorflow
```

2. **Install the required packages:**

```bash
pip install tensorflow opencv-python-headless pillow
```

## Usage

1. **Update the script:**
   - Change the `base_folder` and `image_directory` variables to point to your images directory.

2. **Run the script:**

```bash
python image_sorting.py
```

The script will classify and sort images into folders based on the defined categories.

## Categories

The default categories are:
- Ring
- Necklace
- Bracelet
- Earring
- Mangalsutra

You can update these categories in the script as needed.

## Example

Here’s an example of how the images are sorted:

```
base_folder/
├── rings/
├── necklaces/
├── bracelets/
├── earrings/
└── mangalsutras/
```

## Troubleshooting

If you encounter any issues, ensure that:
- Your image directory paths are correct.
- The images are in supported formats (.jpg, .jpeg, .png).

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the TensorFlow team for their incredible tools that made this project possible!

---

Feel free to customize the details, especially the repository URL and any additional information you think is necessary.
