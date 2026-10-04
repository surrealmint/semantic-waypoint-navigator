import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class TestNode(Node):
    def __init__(self):
        super().__init__('test_node')
        self.get_logger().info('Semantic Waypoint Navigator is running.')


def main(args=None):
    rclpy.init(args=args)
    node = TestNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
