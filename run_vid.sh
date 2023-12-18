#!/bin/bash

# Set your specific data path and processed data directory
DATA_TYPE="video"
DATA_PATH="/home/zihao/Documents/cvlv/footage/single_building/vids.MP4"
PROCESSED_DATA_DIR="/home/zihao/Documents/cvlv/nerf/single_building"
NERFACTO_DATA_DIR="/home/zihao/Documents/cvlv/nerf/single_building/output"

# Run the following command if the error "QObject::moveToThread: Current thread (0x560bf022c870) is not the object's thread (0x560bf0243430). Cannot move to target thread (0x560bf022c870)..." occurs
export QT_QPA_PLATFORM=offscreen

# Run the command
# ns-process-data {video,images,polycam,record3d} --data {DATA_PATH} --output-dir {PROCESSED_DATA_DIR}
# ns-process-data "$DATA_TYPE" --data "$DATA_PATH" --output-dir "$PROCESSED_DATA_DIR"

# ns-train nerfacto --data {PROCESSED_DATA_DIR}
# ns-train nerfacto --data "$PROCESSED_DATA_DIR" --output-dir "$NERFACTO_DATA_DIR"


# Define the target line to monitor
# target_line="Use ctrl+c to quit"

# Loop to monitor the output
ns-train nerfacto --data "$PROCESSED_DATA_DIR" --output-dir "$NERFACTO_DATA_DIR" 2>&1 | tee >(while IFS= read -r line; do
    # Check if the line "Use ctrl+c to quit" is present
    if echo "$line" | grep -q "Use ctrl+c to quit"; then
        # Emphasize the important message
        echo -e "\n\033[1;31mBefore exiting! Use the viewer to visualize the result, determine the volume to export, and obtain the export command line.\033[0m\n"
        break
    fi
done)

# ns-export pointcloud --load-config outputs/good_circle_30/nerfacto/2023-11-10_204128/config.yml --output-dir exports/pcd/ --num-points 1000000 --remove-outliers True --normal-method open3d --use-bounding-box True --bounding-box-min -0.5 -0.5 -1 --bounding-box-max 0.5 0.5 0