import os, shutil, tempfile, zipfile, unittest
from unittest.mock import patch, mock_open, Mock
from imagedownloader import ImageDownloader


class TestImageDownloader(unittest.TestCase):

    def setUp(self):
        self.downloader = ImageDownloader()

    def tearDown(self):
        pass

    def test_fromList(self):
        # Define a list of URLs to download
        urls = [
            'https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_960_720.jpg',
            'https://cdn.pixabay.com/photo/2016/01/09/18/27/camera-1130731_960_720.jpg',
            'https://images.all-free-download.com/images/graphicthumb/a_big_lead_to_the_distant_highdefinition_picture_166031.jpg',
            'https://i.pinimg.com/originals/94/0c/a8/940ca82f1117f98e188b7d38e68bc50d.jpg',
            'https://i.ytimg.com/vi/Uvy7UA6LAwA/maxresdefault.jpg',
            'https://qf7s26sxazr7uwqlogrl311.blob.core.windows.net/sys-master-root/ha1/h30/9840651337758/36445_main.jpg_480Wx480H',
            'https://qf7s26sxazr7uwqlogrl311.blob.core.windows.net/sys-master-root/h9b/h74/9922207481886/36105_main.jpg_480Wx480H'
        ]
        # Get the current working directory
        current_dir = os.getcwd()
        # Create a temporary directory inside the current directory
        with tempfile.TemporaryDirectory(dir = current_dir) as temp_dir:
            # Download the images
            self.downloader.fromList(urls, temp_dir)
            # Check that the images were downloaded and saved
            for url in urls:
                filename = url.split('/')[-1]
                self.assertTrue(os.path.exists(os.path.join(temp_dir, filename)))
        
    
    @patch('requests.get')
    def test_fromCsv(self, mock_get):
        # Mock the response of requests.get to return a mock image
        mock_response = Mock()
        mock_response.content = b'fake-image-bytes'
        mock_get.return_value = mock_response
        
        # Create a mock CSV file with multiple URLs
        csv_path = 'mock_csv.csv'
        csv_content = [
            'https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_960_720.jpg',
            'https://cdn.pixabay.com/photo/2016/01/09/18/27/camera-1130731_960_720.jpg',
            'https://images.all-free-download.com/images/graphicthumb/a_big_lead_to_the_distant_highdefinition_picture_166031.jpg',
            'https://i.pinimg.com/originals/94/0c/a8/940ca82f1117f98e188b7d38e68bc50d.jpg',
            'https://i.ytimg.com/vi/Uvy7UA6LAwA/maxresdefault.jpg',
            'https://qf7s26sxazr7uwqlogrl311.blob.core.windows.net/sys-master-root/ha1/h30/9840651337758/36445_main.jpg_480Wx480H',
            'https://qf7s26sxazr7uwqlogrl311.blob.core.windows.net/sys-master-root/h9b/h74/9922207481886/36105_main.jpg_480Wx480H'
        ]
        with open(csv_path, 'w') as file:
            file.write('\n'.join(csv_content))
        
        # Instantiate the ImageDownloader and call the fromCsv method
        save_path = 'test_images'
        self.downloader.fromCsv(csv_path, save_path)
        
        # Check that all the images were downloaded and saved correctly
        for i, url in enumerate(csv_content):
            expected_path = f'{save_path}/' + url.split('/')[-1]
            self.assertTrue(os.path.exists(expected_path))
            with open(expected_path, 'rb') as file:
                image_bytes = file.read()
            self.assertEqual(image_bytes, b'fake-image-bytes')
        
        # Clean up the mock CSV file and downloaded images
        for i in csv_content:
            os.remove(f'{save_path}/'+i.split('/')[-1])
        os.remove(csv_path)
        os.rmdir(save_path)
    
    def test_zipFolder(self):
        folder_path = 'test_images'
        output_path = 'test_images.zip'
        # Create the folders if they don't exist
        os.makedirs(folder_path, exist_ok = True)
        with open(os.path.join(folder_path, 'image1.jpg'), 'w') as f:
            f.write('test')
        with open(os.path.join(folder_path, 'image2.jpg'), 'w') as f:
            f.write('test')
        self.downloader.zipFolder(folder_path, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)
        os.remove(os.path.join(folder_path, 'image1.jpg'))
        os.remove(os.path.join(folder_path, 'image2.jpg'))
        os.rmdir(folder_path)
    
    
if __name__ == '__main__':
    unittest.main()




