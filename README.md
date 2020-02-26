## dWise

An web application for showing dashboard. project board [here](https://github.com/users/Semooze/projects/2).

### Prerequisites
* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

### How to use
1. Clone this repository
2. Download data from [here](https://drive.google.com/drive/folders/17zfmjp-kTIVjiXoXdt_YGoLAAVG3wjYU?usp=sharing)
   There are there datafiles first is a clean data which is same as raw data but insert double qoute to differentiate
   field of data. RAW data contains message in different line without double qoute.
   second is word list. it's a binary file that I preprocessing in order to gain high speed when start up the appliation.
   third is hashtag list it's the same as word list but contains list of .
   All three files I use this [library](https://github.com/Semooze/morphling) to do preprocessing.
3. Place the files inside dwise/data/
4. Go to directory of the project and run following commane:
    ```shell
    $ docker-compose up
    ```
5. Open a web browser and go to url __127.0.0.1:7000__

### Run test
You can run test with the following command (There is no end-to-end test right now.)
```shell
$ ./runtests.sh
```

if you cannot run test try build an image again with the following command:
```
$ docker-compose build
```