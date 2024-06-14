import os
import platform

commandList=['cd /opt/google/chrome && nohup ./chrome --remote-debugging-port=9222 -incognito www.chatgpt.com &']
def debuggingModeLauncher():
    try:
        currentWorkingEnv=platform.system()
        if currentWorkingEnv=='Windows':
            pass
        elif currentWorkingEnv=='Linux':    
            for cmd in commandList:
                os.system(cmd)
        elif currentWorkingEnv=='Darwin':
            for cmd in commandList:
                os.system(cmd)
    except:
        print("Unknown Operating System")
