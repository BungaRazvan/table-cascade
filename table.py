import sys
from PyQt5.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QGraphicsLineItem,
)
from PyQt5.QtGui import QPen, QBrush, QDrag
from PyQt5.QtCore import Qt, QPointF, QMimeData


class ERTableNode(QGraphicsRectItem):
    def __init__(self, table_name: str, fields, x: int = 0, y: int = 1):
        super().__init__(0, 0, 150, 25 + len(fields) * 20)
        self.setPos(x, y)
        self.setBrush(QBrush(Qt.white))

        self.title = QGraphicsTextItem(table_name, self)
        self.title.setDefaultTextColor(Qt.black)
        self.title.setPos(5, 5)
        self.setFlags(
            QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable
        )
        self.connected_lines = []

        for i, field in enumerate(fields):
            field_text = QGraphicsTextItem(field, self)
            field_text.setDefaultTextColor(Qt.black)
            field_text.setPos(10, 30 + i * 20)

    def center(self):
        return QPointF(
            self.x() + self.rect().width() / 2, self.y() + self.rect().height() / 2
        )

    def add_line(self, line):
        """Add a line to update when this item moves."""
        self.connected_lines.append(line)

    def itemChange(self, change, value):
        """Override itemChange to update lines when the table is moved."""

        if change == QGraphicsRectItem.ItemPositionChange:
            for line in self.connected_lines:
                line.update_position()

        return super().itemChange(change, value)


class ERDiagram(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.tables = dict()

    def add_table(self, table_name: str, fields, x: int = 0, y: int = 1):
        table_node = ERTableNode(table_name, fields, x, y)
        self.tables[table_name] = table_node
        self.addItem(table_node)

    def add_relationship(self, table1, table2):

        if table1 in self.tables and table2 in self.tables:
            node1 = self.tables[table1]
            node2 = self.tables[table2]
            line = QGraphicsLineItem(
                node1.center().x(),
                node1.center().y(),
                node2.center().x(),
                node2.center().y(),
            )
            line.setPen(QPen(Qt.red, 2))
            self.addItem(line)
