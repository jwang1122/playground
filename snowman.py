class Snowman:
    def __init__(self, bottomX, bottomY, head, body, leg):
        self.bottomX = bottomX
        self.bottomY = bottomY
        self.head = head
        self.body = body
        self.leg = leg

    def drawBody(self, pen1):
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY+2*self.leg)
        pen1.down()
        pen1.circle(self.body)

    def drawHead(self, pen1):
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY + 2*self.leg+2*self.body)
        pen1.down()
        pen1.circle(self.head)

    def drawLeg(self, pen1):
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY)
        pen1.down()
        pen1.circle(self.leg)

    def draw(self, pen1):
        self.drawLeg(pen1)
        self.drawBody(pen1)
        self.drawHead(pen1)


def drawCircle(pen1, x, y, r):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.circle(r)


def drawLine(pen1, x, y, angle, length):
    """
    draw a line start at position (x,y) and angle and length
    """
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.left(angle)
    pen1.fd(length)
    pen1.right(angle)


def drawTriangle(pen1, x, y, side):
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.right(60)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(60)


def drawRectangle(pen1, x, y, width, height):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)
