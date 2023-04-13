from ament_index_python import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch import LaunchDescription

pkg_path = get_package_share_directory("deter1")
def generate_launch_description():
    gazebo_launch_path = os.path.join(pkg_path, "launch", "gazebo.launch.py")
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch_path])
    )

    teleop_node = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        name="teleop_twist_keyboard",
        prefix='xterm -e',
        output='screen',
        emulate_tty=True,
        arguments=[('__log_level:=debug')]
    )

    return LaunchDescription(
        [
            gazebo_launch,
            teleop_node
        ]
    )