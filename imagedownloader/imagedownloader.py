#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Mazhar"
__credits__ = ["Mazhar"]
__Lisence__ = "BSD"
__maintainer__ = "Mazhar"
__email__ = "mazqoty.01@gmail.com"
__status__ = "Production"
__version__ = "1.1.0"

#Default Python Packages
import csv, os, requests, zipfile, warnings
warnings.filterwarnings("ignore")

#PIP installed Python Packages

#Imports from other files

class ImageDownloader:
    
    def fromList(self, list_urls, save_path):
        """_summary_
        
        Download images from urls and save them in the folder
        
        Args:
            list_urls (list): List containing urls of immages
            save_path (str): path of the folder where downloaded images to be saved
        """
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        if len(list_urls) > 0:
            for url in list_urls:
                try:
                    response = requests.get(url)
                    filename = os.path.join(save_path, url.split('/')[-1])
                    with open(filename, 'wb') as image_file:
                        image_file.write(response.content)
                except Exception as e:
                    print("Error 1", e)
        else:
            print("Please Enter URL List")
    
    def fromCsv(self, csv_path, save_path):
        """_summary_
        
        Download images from csv file that contains multiple urls and save them in the folder
        
        Args:
            csv_path (str): path of the file that contains Urls of the images to be downloaded
            save_path (str): path of the folder where downloaded images to be saved
        """
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        try:
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        image_url = row[0]
                        image_name = row[0].split('/')[-1]
                        response = requests.get(image_url)
                        with open(os.path.join(save_path, image_name), 'wb') as image_file:
                            image_file.write(response.content)
                    except Exception as e:
                        print("Error: 2", e)
        except Exception as e:
                        print("Error 3", e)

    def zipFolder(self, folder_path, output_path):
        """_summary_

        Zip the folder where images are saved
        
        Args:
            folder_path (str): path of the folder to be zipped
            output_path (str): output path of zipped folder
        """
        try:
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, arcname = file)
        except Exception as e:
            print("Error 4", e)
            
    def __str__(self):
        return f"{ImageDownloader}()"
    
    def __repr__(self):
        return f"ImageDownloader()"
                    
                    
                    