import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter image url: ')
file_name = input('Enter file name to save as: ')
dl_jpg(url, 'images/', file_name)


#download images like in the social network movie
#face mash

#urllib documentation
#video downloads eg from youtube