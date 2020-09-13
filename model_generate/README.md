### Preparations.
Using the Flicker API

*Get Key and Secret*.
1. https://www.flickr.com/services/api/
2. create an app at the top of the screen after login.
Request an API on the right.
4. choose the one that best suits your purpose
5. enter at random
6. get the Key and Secret
pip3 install flickrapi
 + Install the Flickr API module

### Process.
1. download.py
 + Saves the first photo. The number of photos to be saved is adjusted in line 20. If the folder does not exist, it will be created. 2.
    
2. generate_data_224.py
 + Saves the downloaded photos in numpy format. The photo must be specified in line 6.
 + generate_data.py will be less accurate because of the small size of the image.
    
3. vgg16_transger.py
 + Create a model.
    
4. predict.py
 + We check to see if the prediction is correct by entering the name of the jpg file we are preparing as the first argument### Preparations.
Using the Flicker API

*Get Key and Secret*.
1. https://www.flickr.com/services/api/
2. create an app at the top of the screen after login.
Request an API on the right.
4. choose the one that best suits your purpose
5. enter at random
6. get the Key and Secret
pip3 install flickrapi
 + Install the Flickr API module

### Process.
1. download.py
 + Saves the first photo. The number of photos to be saved is adjusted in line 20. If the folder does not exist, it will be created. 2.
    
2. generate_data_224.py
 + Saves the downloaded photos in numpy format. The photo must be specified in line 6.
 + generate_data.py will be less accurate because of the small size of the image.
    
3. vgg16_transger.py
 + Create a model.### Preparations.
Using the Flicker API

*Get Key and Secret*.
1. https://www.flickr.com/services/api/
2. create an app at the top of the screen after login.
Request an API on the right.
4. choose the one that best suits your purpose
5. enter at random
6. get the Key and Secret
pip3 install flickrapi
 + Install the Flickr API module

### Process.
1. download.py
 + Saves the first photo. The number of photos to be saved is adjusted in line 20. If the folder does not exist, it will be created. 2.
    
2. generate_data_224.py
 + Saves the downloaded photos in numpy format. The photo must be specified in line 6.
 + generate_data.py will be less accurate because of the small size of the image.
    
3. vgg16_transger.py
 + Create a model.
    
4. predict.py
 + We check to see if the prediction is correct by entering the name of the jpg file we are preparing as the first argument
    
4. predict.py
 + We check to see if the prediction is correct by entering the name of the jpg file we are preparing as the first argument