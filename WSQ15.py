from PIL import Image

def rotate_Image(image, name_Image):
    orientation = input("Rotate to 'left' or 'right' or 'vertical'?\n")
    if orientation == "left":
        image_90 = image.rotate(90, expand=True)
        if name_Image == "cat.jpg":
            image_90.save("cat_rotate_left.jpg")
        else:
            image_90.save("dog_rotate_left.jpg")
    elif orientation == "right":
        image_270 = image.rotate(270, expand=True)
        if name_Image == "cat.jpg":
            image_270.save("cat_rotate_right.jpg")
        else:
            image_270.save("dog_rotate_right.jpg")
    elif orientation == "vertical":
        image_180 = image.rotate(180, expand=True)
        if name_Image == "cat.jpg":
            image_180.save("cat_rotate_vertical.jpg")
        else:
            image_180.save("dog_rotate_vertical.jpg")

def flip_Image(image, name_Image):
    orientation = input("Flip image to 'vertical' or 'horizontal'?\n")
    if orientation == "vertical":
        image_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
        if name_Image == "cat.jpg":
            image_vertical.save("cat_flip_vertical.jpg")
        else:
            image_vertical.save("dog_flip_vertical.jpg")
    elif orientation == "horizontal":
        image_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
        if name_Image == "cat.jpg":
            image_horizontal.save("cat_flip_horizontal.jpg")
        else:
            image_horizontal.save("dog_flip_horizontal.jpg")

def resize_Image(image, name_Image):
    new_width = int(input("New width (pixels):\n"))
    new_length = int(input("New length (pixels):\n"))
    image_resized = image.resize((new_width,new_length),)
    if name_Image == "cat.jpg":
        image_resized.save("cat_resized.jpg")
    else:
        image_resized.save("dog_resized.jpg")

def main():
    name_Image = input("Select an image cat.jpg or dog.jpg:\n")
    if name_Image == "cat.jpg":
        cat_Image = Image.open("cat.jpg")
        decision = input("Rotate:1     Flip:2     Resize:3\n")
        if decision == "1":
            rotate_Image(cat_Image, name_Image)
        elif decision == "2":
            flip_Image(cat_Image, name_Image)
        elif decision == "3":
            resize_Image(cat_Image, name_Image)

    elif name_Image == "dog.jpg":
        dog_Image = Image.open("dog.jpg")
        decision = input("Rotate:1     Flip:2     Resize:3\n")
        if decision == "1":
            rotate_Image(dog_Image, name_Image)
        elif decision == "2":
            flip_Image(dog_Image, name_Image)
        elif decision == "3":
            resize_Image(dog_Image, name_Image)

    else:
        print("You didn't select a valid option.")

if __name__ == "__main__":
    main()
