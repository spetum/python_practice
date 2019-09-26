

## Single Process
import time
from PIL import Image, ImageFilter

img_names = [
    "original/photo-1524429656589-6633a470097c.jpg",
    "original/photo-1516972810927-80185027ca84.jpg",
    "original/photo-1516117172878-fd2c41f4a759.jpg",
    "original/photo-1513938709626-033611b8cc03.jpg",
    "original/photo-1507143550189-fed454f93097.jpg",
    "original/photo-1504198453319-5ce911bafcde.jpg",
    "original/photo-1493976040374-85c8e12f0c0e.jpg"
]

if __name__ == '__main__':
    t1 = time.perf_counter()
    size=(1200, 1200)

    for img_name in img_names:
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))

        img.thumbnail(size)
        img.save(f'processed/{img_name}')
        print(f'{img_name} was processed ...')

    t2 = time.perf_counter()

    print(f'Finished in {round(t2-t1, 2)} second(s)')