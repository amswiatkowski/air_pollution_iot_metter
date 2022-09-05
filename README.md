# Simple air pollution metter built with AWS Greengrass, NanoPi Neo V1.4 and SDS011

## Introduction

#### This project contains a source code for application used to measure air pollution and send PM2.5 and PM10 values to the AWS cloud.

## Running
Connect SDS011 sensor to the UART-USB converter, than connect converter to NanoPi Neo V1.4. Commands to run the program:

```
pip3 install -r requirements.txt
python3 main.py
```

## Author

**Adam Świątkowski**

* [github/sz3jdii](https://github.com/sz3jdii)
* [Blog](https://cloudybarz.com/)

### License

Copyright © 2022, [Adam Świątkowski](https://github.com/sz3jdii).
Released under the [MIT License](LICENSE).