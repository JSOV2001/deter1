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
        PythonLaunchDescriptionSource([rsp_launch_path]),
        launch_arguments= {
            'use_sim_time': 'true'
        }.items()
    )

    gazebo_cmd = ExecuteProcess(
        cmd=["gazebo", "--verbose", "-s", "libgazebo_ros_init.so", "-s", "libgazebo_ros_factory.so"]
    )

    spawn_node = Node(
        package= "gazebo_ros",
        executable= "spawn_entity.py",
        arguments= ["-topic", "robot_description", "-entity", "deter1"]
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
            rsp_launch,
            gazebo_cmd,
            spawn_node,
            teleop_node
        ]
    )