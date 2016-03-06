# _*_ coding=utf-8 _*_
import win32serviceutil
import  win32service
import win32event

__author__ = 'patrick'
class MyService(win32serviceutil.ServiceFramework):
    # 服务名
    _svc_name_ = "MyService"
    #服务显示名称
    _svc_display_name_ = "MyServiceDemo"
    #服务描述
    _svc_description_ = "Python service demo."

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isAlive = True

    def SvcStop(self):
        # 先告诉SCM停止这个过程
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False

    def SvcDoRun(self):
        # We do nothing other than wait to be stopped!
        win32event.WaitForSingleObject(self.hWaitStop,win32event.INFINITE)
        # self.ReportServiceStatus(win32service.SERVICE_STOPPED)

if __name__=='__main__':
    win32serviceutil.HandleCommandLine(MyService)
