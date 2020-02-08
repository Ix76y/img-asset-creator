# img-asset-creator
Creating image assets for iOS and Android Apps with Python3 from the command-line.

I build this script to easily create image assets for iOS and Android Apps. You can pass an image or a folder of images to the script, define which size the images should be and for which platform and it will scale the images and save them.

The script will handle the correct scaling and naming for iOS and Android.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

In order to run the script you need to have python3 installed on your machine. The script also makes use of the Pillow module.
If you have pip installed you can simply run the script and it will install Pillow for you, otherwise you have to install it yourself.

### Runnning the script

To download the project you can either download it from the browser or over the command-line and git, by running the following command.
```
git clone git@github.com:Ix76y/img-asset-creator.git
```
After that you can run the script with the following command, which will show you all available options
```
python3 imgasset.py --help
```

## Examples
Here are some example usages for the script.

For example if you have one image called **pineapple.png** and you want to have this image for **iOS** with a **width** of **1200px**(\@3x), 800px(\@2x) and 400px (\@1x). ***Note:*** *You just have to pass the biggest width or height, the rest will be calculated accordingly.*
```
python3 imgasset.py -iOS -w 1200 pineapple.png

# Output:
  |-- pineapple.png
  |-- pineapple@1x.png
  |-- pineapple@2x.png
  |-- pineapple@3x.png
```

If you have a folder called <code>input</code> of images and you want them all for **Android** with a **height** of **1800px** for xxxhdpi then you can run the following command.
```
python3 imgasset.py -android -h 1800 /input

# Output:
  |-- input
  |-- xxxhdpi
  |-- -- ...
  |-- xxhdpi
  |-- -- ...
  |-- xhdpi
  |-- -- ...
  |-- hdpi
  |-- -- ...
  |-- mdpi
  |-- -- ...
  |-- ldpi
  |-- -- ...
  # each of the folders contains all the scaled images that are in the input folder
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Notes
* Feel free to use this script and
* let me know if you are missing any functionality
