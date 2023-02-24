# Image Downloader

<div align="center">

  <a href="#">![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=plastic&logo=Python)</a>
  <a href="#">![PyPI - Wheel](https://img.shields.io/pypi/wheel/imagedownloader?style=fplastic)</a>
  <a href="#">![PyPI - Downloads](https://img.shields.io/pypi/dm/imagedownloader?style=plastic)</a>
  <a href="#">![PyPI - License](https://img.shields.io/pypi/l/imagedownloader?style=plastic)</a>
  <a href="https://imagedownloader.readthedocs.io/en/latest/">![Read the Docs](https://img.shields.io/readthedocs/imagedownloader?style=plastic)</a>
  

</div>

<div align="center">

  <a href="https://pypi.org/project/imagedownloader/">![PyPI](https://img.shields.io/pypi/v/imagedownloader?style=for-the-badge)</a>
  <a href="https://github.com/mm-mazhar/imagedownloader">![text](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub)</a>
  <a href="https://imagedownloader.readthedocs.io/en/latest/">![text](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)</a>

</div>

This is a Python Package called `imagedownloader` that defines three methods: `fromList()`, `fromCsv()`, and `zipFolder()`. The class is designed to download images from either a list of URLs or a CSV file containing multiple URLs, and then save them to a specified folder location. Additionally, it provides functionality to zip the folder where the downloaded images are saved.

The `fromList()` method takes a list of URLs and a folder path as arguments. If the specified folder does not exist, the method creates it. Then, it loops through the list of URLs, sends a request to download the image, and saves the image to the folder using the last part of the URL as the filename. If any errors occur during the process, the method prints an error message.

The `fromCsv()` method takes a CSV file path and a folder path as arguments. If the specified folder does not exist, the method creates it. Then, it reads the CSV file using the `csv.reader()` function and loops through each row. For each row, it extracts the URL, sends a request to download the image, and saves the image to the folder using the last part of the URL as the filename. If any errors occur during the process, the method prints an error message.

The `zipFolder()` method takes a folder path and an output path as arguments. It creates a new zip file at the output path and loops through each file in the specified folder using the `os.walk()` function. For each file, it adds the file to the zip file with the same filename. If any errors occur during the process, the method prints an error message.

The class also provides two dunder methods, __str__() and __repr__(), which return a string representation of the class instance.

## Installation

Pytubev3 requires an installation of Python 3.7 or greater, as well as pip. (Pip is typically bundled with Python [installations](https://python.org/downloads))

To install from PyPI with pip:

`python -m pip install imgdownloader`

## Examples

CSV File Should have all the urls in the first column as follows

<img src="https://i.imgur.com/z8i92e7.jpg" width="700px" height=100px/>

<br>

```
from imagedownloader import ImageDownloader

if __name__ == "__main__":
    
    image_urls = [
    'https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_960_720.jpg',
    ]
    
    save_path = "./images"
    csv_path = "./test.csv"
    output_path = "./images.zip"
    folder_path = "./images"
    
    imgDownloader = ImageDownloader()
    imgDownloader.fromList(image_urls, save_path)
    imgDownloader.fromCsv(csv_path, save_path)
    imgDownloader.zipFolder(folder_path, output_path)
```

## Development/Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: ` git commit -am 'Add Some Feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.
6. Email me at `mazqoty.01@gmail.com` because I do not check those messages often.

## History
* 1.0.0 - Initial Commit without tests 
