import os

# Checks for images not used in any files.

imagePath = "/home/mccgeoff/workplace/mccgeoff/vpc/src/AWSVPCDocs/latest/ug/images"
filePath = "/home/mccgeoff/workplace/mccgeoff/vpc/src/AWSVPCDocs/latest/ug/"

fileList = (os.listdir(filePath))
imageList = (os.listdir(imagePath))
usedImagesIndex = []
usedImages = []
unusedImages = []

# Change to the dir of the XML files.

os.chdir(filePath)

# Loop over each image file in the imageDir directory.

for image in imageList:

    # For each file in the fileList directory, check that the file is a file, not a directory, and read the file. If the image in is in one of the files, add it to the usedImagesIndex list. 

    for file in fileList:
        if os.path.isfile(file):
            with open(file, "r") as file_object:
                readfile = file_object.read()
            if image in readfile:
                usedImagesIndex.append(image)
            else:
                pass          
        else:
            pass
    
    # Remove duplicates in the usedImagesIndex list

    usedImages = list(dict.fromkeys(usedImagesIndex))

    # Check if image is in usedImages list. If not, add image to unusedImages list. 

    if image in usedImages:
        pass
    else:
        unusedImages.append(image)

# Print the results.

print()
print(f"Files checked: {len(fileList)}")
print(f"Images checked: {len(imageList)}")
print(f"Images used: {len(usedImages)}")
print(f"Images not used: {len(unusedImages)} ",*unusedImages, sep='\n')
print()