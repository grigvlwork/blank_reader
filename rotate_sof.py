import math
from PyQt5 import QtCore, QtWidgets

class DraggableGraphicsItemSignaller(QtCore.QObject):

    positionChanged = QtCore.pyqtSignal(QtCore.QPointF)

    def __init__(self):
        super().__init__()

def make_GraphicsItem_draggable(parent):

    class DraggableGraphicsItem(parent):

        def __init__(self, *args, **kwargs):
            """
            By default QGraphicsItems are not movable and also do not emit signals when the position is changed for
            performance reasons. We need to turn this on.
            """
            parent.__init__(self, *args, **kwargs)
            self.parent = parent
            self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable | QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
            self.signaller = DraggableGraphicsItemSignaller()

        def itemChange(self, change, value):
            if change == QtWidgets.QGraphicsItem.ItemPositionChange:
                self.signaller.positionChanged.emit(value)

            return parent.itemChange(self, change, value)

    return DraggableGraphicsItem

def rotate_item(position):
    item_position = item.transformOriginPoint()
    angle = math.atan2(item_position.y() - position.y(), item_position.x() - position.x()) / math.pi * 180 - 45 # -45 because handle item is at upper left border, adjust to your needs
    # print(angle)
    item.setRotation(angle)


DraggableRectItem = make_GraphicsItem_draggable(QtWidgets.QGraphicsRectItem)
DraggableCircleItem = make_GraphicsItem_draggable(QtWidgets.QGraphicsEllipseItem)

app = QtWidgets.QApplication([])

scene = QtWidgets.QGraphicsScene()
item = DraggableRectItem()
item.setRect(0, 0, 100, 100)
item.setTransformOriginPoint(50, 50)
scene.addItem(item)

handle_item = DraggableCircleItem()
handle_item.signaller.positionChanged.connect(rotate_item)
handle_item.setRect(-40, -40, 20, 20)
scene.addItem(handle_item)

view = QtWidgets.QGraphicsView(scene)
view.setFixedSize(500, 500)
view.show()

app.exec_()