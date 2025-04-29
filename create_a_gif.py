import imageio.v3 as iio

# Create a GIF from a list of images
filenames = ['team-pic1.png', 'team-pic2.png']
images = []

# Read each image file and append it to the images list
for filename in filenames:
    images.append(iio.imread(filename))

# * .imread() method loads an image based on the file path. So now, our `images` variable has all the images.

# Create a GIF from the images list
iio.imwrite('team.gif', images, duration=500, loop=0) # duration is in milliseconds
# * .imwrite() takes in four arguments:
# * 1. 'team.gif' - This is the name you want to give to your new GIF file.
# * 2. images - The list containing the image data.
# * 3. duration = 500 - How long each picture should in the GIF, in milliseconds.
# * 4. loop = 0 - How many times the GIF should repeat (0 means it keeps looping forever).

