from ament_index_python import get_package_share_directory
import os
import xacro
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

pkg_path = get_package_share_directory("deter1")

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    xacro_file_path = os.path.join(pkg_path, "urdf","deter1.urdf.xacro")
    robot_description_config = xacro.process_file(xacro_file_path)
    rsp_node = Node(
        package= "robot_state_publisher",
        executable= "robot_state_publisher",
        parameters=[
            {
                "robot_description": robot_description_config.toxml(),
                'use_sim_time': use_sim_time
            }
        ]
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                'use_sim_time', 
                default_value= 'false', 
                description= 'Use sim time if true'
            ),
            rsp_node
        ]
    )