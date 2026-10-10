import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from geometry_msgs.msg import Twist


class CircleDriver(Node):
    def __init__(self):
        super().__init__('circle_driver')

        # Declare parameters with default values
        self.declare_parameter('linear_speed', 1.0)
        self.declare_parameter('angular_speed', 0.9)

        # Create publisher to turtle1/cmd_vel
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Timer callback at 10 Hz
        self.timer = self.create_timer(0.1, self.timer_callback)

        # Register a callback so parameters update live
        self.add_on_set_parameters_callback(self.param_callback)

        self.get_logger().info(
            f'circle_driver started with linear={self.get_parameter("linear_speed").value}, '
            f'angular={self.get_parameter("angular_speed").value}'
        )

    def param_callback(self, params):
        for param in params:
            self.get_logger().info(f'Parameter "{param.name}" changed to {param.value}')
        return SetParametersResult(successful=True)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = float(self.get_parameter('linear_speed').value)
        msg.angular.z = float(self.get_parameter('angular_speed').value)
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CircleDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
