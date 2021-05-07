# virtual-video-with-python
Create virtual video with opencv and python to use in video call like MEET, ZOOM or Microsoft teams

Works well on Ubuntu 18.04

## Check your original video

    $ ls /dev/video*
        /dev/video0  /dev/video1


## Install v4l2loopback
    
    Reference : https://github.com/umlaeute/v4l2loopback.git

    $ git clone https://github.com/umlaeute/v4l2loopback.git
    $ cd v4l2loopback/
    $ make && sudo make install
    $ sudo depmod -a

    run 

    $ sudo modprobe v4l2loopback

    check

    $ ls /dev/video*
        /dev/video0  /dev/video2


    If you have error like v4l2llopback is not permitted:

        Reference : https://stackoverflow.com/questions/61754689/v4l2loopback-cannot-load-module-on-aws-ubuntu-18-04

        Disable secure boot work well for me:

        $ sudo mokutil --disable-validation 
        $ sudo reboot now


# Run code python:

    Reference : https://github.com/Flashs/virtualvideo.git



    $ sudo modprobe v4l2loopback
    $ ls /dev/video*
        /dev/video0  /dev/video2    
    $ pip3 install virtualvideo
    $ python3 showFish.py


<img src="new_virtual_camera.jpeg?raw=true" width="2500" height = "300"/>

