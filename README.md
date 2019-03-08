# Mimic-Instagram

## Create an application that is not ashamed to show to people as a portfolio.

### Description
- Create SNS with Django
  - Instagram tribute
- Upload image
- Labeling posted images using vgg16
- Compute similarity of user's tastes based on posted images, implement user's recommendation

## Preview
### Index pages
![Imgur](https://i.imgur.com/UN5p3N9.gif)

### Post Image
![Imgur](https://i.imgur.com/YhWezYq.gif)

### Recommend Users
The most important feature is user base filtering from the user's posted image and recommends similar users  
![Imgur](https://i.imgur.com/b7sowfW.png)

### Usage
`$ mkdir <YOUR DIR> && cd <YOUR DIR>`
`$ python -m venv venv`
`$ source venv/bin/activate`
`$ git clone git@github.com:10380r/Mimic-Instagram.git`
`$ cd Mimic-Instagram`
`$ pip install -r requirements.txt`
`$ ./manage.py migrate`
`$ ./manage.py createsuperuser`
`$ ./manage.py runserver`

login at [admin page](http://localhost:8000/admin)
  - create users
  > _Notes: When entering User information, change the permission to Staff status. Also select Choose all for User permission._

Then, you can try sns. at http://localhost:8000/app

### Requirements
`python 3.7.2`  
`django 2.1.5`  
`Mac OS Mojave 10.14.3` (I am trying to execute it only on this OS)  

### References
[vgg16](https://keras.io/ja/applications/#vgg1://keras.io/ja/applications/#vgg16)  
[vue.js network](http://visjs.org/docs/network/) You can change the drawing style of the network by changing vue. 
