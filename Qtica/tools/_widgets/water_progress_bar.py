class Pop:
    # https://github.com/linuxdeepin/dtkwidget/blob/master/src/widgets/dwaterprogress.cpp#L36

    def __init__(self, size, xs, ys, xo=0, yo=0):
        self.size = size
        self.x_speed = xs
        self.y_speed = ys
        self.x_offset = xo
        self.y_offset = yo
