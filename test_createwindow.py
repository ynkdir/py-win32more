# https://learn.microsoft.com/en-us/windows/win32/learnwin32/your-first-windows-program

import Windows.all as win32

def WinMain():
    hInstance = win32.GetModuleHandleW(None)
    nCmdShow = win32.SW_SHOWNORMAL

    # Register the window class.
    CLASS_NAME  = "Sample Window Class"

    wc = win32.WNDCLASSW()

    wc.lpfnWndProc   = win32.WNDPROC(WindowProc)
    wc.nInstance     = hInstance
    wc.lpszClassName = CLASS_NAME

    win32.RegisterClassW(wc);

    # Create the window.

    hwnd = win32.CreateWindowExW(
        0,                              # Optional window styles.
        CLASS_NAME,                     # Window class
        "Learn to Program Windows",     # Window text
        win32.WS_OVERLAPPEDWINDOW,      # Window style

        # Size and position
        win32.CW_USEDEFAULT, win32.CW_USEDEFAULT, win32.CW_USEDEFAULT, win32.CW_USEDEFAULT,

        0,          # Parent window
        0,          # Menu
        hInstance,  # Instance handle
        0           # Additional application data
        )

    if (hwnd == 0):
        return 0

    win32.ShowWindow(hwnd, nCmdShow);

    # Run the message loop.

    msg = win32.MSG()
    while win32.GetMessageW(msg, 0, 0, 0) > 0:
        win32.TranslateMessage(msg)
        win32.DispatchMessageW(msg)

    return 0

def WindowProc(hwnd: win32.HWND, uMsg: win32.UInt32, wParam: win32.WPARAM, lParam: win32.LPARAM):
    match uMsg:
        case win32.WM_DESTROY:
            win32.PostQuitMessage(0);
            return 0
        case win32.WM_PAINT:
            ps = win32.PAINTSTRUCT()
            hdc = win32.BeginPaint(hwnd, ps)

            # All painting occurs here, between BeginPaint and EndPaint.

            win32.FillRect(hdc, ps.rcPaint, win32.HBRUSH(win32.COLOR_WINDOW+1))

            win32.EndPaint(hwnd, ps)

            return 0
    return win32.DefWindowProcW(hwnd, uMsg, wParam, lParam)

if __name__ == "__main__":
    WinMain()
