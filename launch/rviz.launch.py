from ament_index_python import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch import LaunchDescription

pkg_path = get_package_share_directory("deter1")

def generate_launch_description():
    rsp_launch_path = os.path.join(pkg_path, "launch", "rsp.launch.py")
    rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([rsp_launch_path])
    )

    rviz_file_path = os.path.join(pkg_path, "rviz", "urdf.rviz")
    rviz_cmd = ExecuteProcess(
        cmd= ["rviz2", "-d", rviz_file_path]
    )

    jsp_gui_node = Node(
        package= "joint_state_publisher_gui",
        executable= "joint_state_publisher_gui",
    )

    return LaunchDescription(
        [   
            rsp_launch,
            rviz_cmd,
            jsp_gui_node
        ]
    )