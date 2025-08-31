import random
import time

from win32more.Microsoft.Graphics.Canvas.UI.Xaml import CanvasAnimatedControl
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import Grid
from win32more.Windows.UI import Colors
from win32more.appsdk.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        self._count = 0
        self._fps = 0
        self._time = 0

        self.window = Window()

        grid = Grid()
        self.window.Content = grid

        self.Canvas1 = CanvasAnimatedControl()
        self.Canvas1.Draw += self.Canvas1_Draw
        self.Canvas1.ClearColor = Colors.Gray
        grid.Children.Append(self.Canvas1)

        self.window.Activate()

    def Canvas1_Draw(self, sender, args):
        for x in range(0, int(self.Canvas1.Size.Width), 50):
            args.DrawingSession.DrawLineAtCoordsWithColor(x, 0, x, self.Canvas1.Size.Height, Colors.Blue)
        for y in range(0, int(self.Canvas1.Size.Height), 50):
            args.DrawingSession.DrawLineAtCoordsWithColor(0, y, self.Canvas1.Size.Width, y, Colors.Blue)

        colors = [Colors.Red, Colors.Blue, Colors.Green, Colors.Yellow]
        for i in range(10):
            x = random.randint(0, int(self.Canvas1.Size.Width))
            y = random.randint(0, int(self.Canvas1.Size.Height))
            c = random.choice(colors)
            args.DrawingSession.DrawEllipseAtCoordsWithColorAndStrokeWidth(x, y, 25, 25, c, 2)

        t = int(time.perf_counter())
        if t != self._time:
            self._fps = self._count
            self._count = 0
            self._time = t
        self._count += 1
        args.DrawingSession.DrawTextAtPointCoordsWithColor(f"FPS: {self._fps}", 0, 0, Colors.Black)


XamlApplication.Start(App)
