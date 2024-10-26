import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QLabel

from table import ERDiagram


class MainWindow(QMainWindow):
    """Main window to display the ER diagram."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ER Diagram Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel("Hello, PyQt5!", self)

        self.view = QGraphicsView(self)
        self.view.setGeometry(0, 0, 800, 600)
        self.scene = ERDiagram()
        self.view.setScene(self.scene)

        self.init_diagram()

    def init_diagram(self):
        """Initialize the ER diagram with sample tables and relationships."""
        # Add tables
        self.scene.add_table("Users", ["user_id", "username", "email"], 100, 100)
        self.scene.add_table("Orders", ["order_id", "order_date", "user_id"], 400, 100)
        self.scene.add_table(
            "Products", ["product_id", "product_name", "price"], 100, 300
        )
        # self.scene.add_table(
        #     "OrderDetails",
        #     ["order_detail_id", "order_id", "product_id", "quantity"],
        #     400,
        #     300,
        # )

        # Add relationships (foreign keys)
        self.scene.add_relationship("Users", "Orders")  # Users -> Orders
        self.scene.add_relationship("Orders", "OrderDetails")  # Orders -> OrderDetails
        self.scene.add_relationship(
            "Products", "OrderDetails"
        )  # Products -> OrderDetails


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
