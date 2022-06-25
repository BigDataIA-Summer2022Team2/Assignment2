# Team1 API Doc notes

> main focus on tran_ship_segment_v2.csv and tran_v2.folder

- There are two rows: image_id, encoded pixels
- There are two results in images: with ship or without ship

## API Function 1: get image and masks

### Input

- User input required
- @param: imageid
- @type: str
- @default: imgshape (768,768)

### Output

- a original image in Numpy array format
- a mask of image in Numpy array format

### Error Handeling

- If name of image file invalid, return Team 1 custom String

![截图](59aba48a872659d242cde19b22ca2f81.png)

![截图](0c40315c50a1687713da55d1a0f1b753.png)

## API function 2: get run length decode

### Input

- User input required
- @param mask_rle: run-length
- @type str
- @default: imgshape (768,768)

### Output

- return a Numpy array with 2 types of int value: 0,1
- 0 means no ship, 1 means in this position has ship

### Error Handeling

- return a Team 1 custom error message

![截图](7e8dd6a3d3064f789e1ae96da06f4e1c.png)

![截图](5327f1886ca5597373bc2f241358dbce.png)

## API function 3: get ship and non-ship image

### Input

- User input required
- @param "ship" or "noship"
- @type: str

### Output

- one of the images name with "ship" or "noship" condition in the image

### Error Handeling

- return Team1 custom error message

![截图](4fa9cb44451290e3ffc58746419eb553.png)

![截图](5f6fc5956ca8bf22a2200373e8ab31d8.png)

## API function 4: get the number of images that has certain number of ships

### Input

- User input required
- @param num  ->  number of ships in an image
- @type: int

### Output

- return number of images with certian input number of ships

### Error Handeling

- return Team1 custom error message

![截图](f66ea8bccae2cf56ac2eaf7a70796630.png)

![截图](809d84f2bb81632861df33fcce4e1e3b.png)

## API Function 5: get image directly from S3

### Input

- User input required
- @param: file name in the S3 storage
- @type: str

### Output

- return a Numpy array of the image pixels

### Error Handeling

- return Team 1 custom error message

![截图](d13fd7ec9f349be6168335d420d38b90.png)

![截图](2f9e0985a6ecdfebcac47c2ef952dca0.png)

## API function 6: get the number of ships in a certain image

### Input

- User input required
- @param image filename
- @type: str

### Output

- return an integer, count number of ships are in this image

### Error Handeling

- return Team1 custom error message

![截图](d1f7e65056868103f28e833da20548de.png)

![截图](a8be4392c6ffe1e16d16300f976774ef.png)
