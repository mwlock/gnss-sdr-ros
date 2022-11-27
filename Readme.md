# GNSS-SDR Monitoring Package for ROS Noetic

## Installation

1. Make sure you have protoc installed. If not, install it with:

```bash
sudo apt install libprotobuf-dev protobuf-compiler
```

2. Install the python protobuv extension

> Ensure you install the correct version of protobuf using ```protoc --version```

Download the protobuf binary that matches your protoc version from [here](https://github.com/protocolbuffers/protobuf/releases)

Go to the commit that matches your protoc version (as shown above) and navigate to the python folder. Here you can follow the instructions to install the python protobuf extension.


## Compile the Protobuf messages

1. Navigate to the proto folder

```bash
cd src/proto
```

2. Compile the protobuf messages

```bash
protoc -I=./ --python_out=./ ./monitor_pvt.proto
protoc -I=./ --python_out=./ ./gnss_synchro.proto
```