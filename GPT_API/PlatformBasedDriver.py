import os
import platform

commandList=['cd /opt/google/chrome && ./chrome --remote-debugging-port=7070']
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
debuggingModeLauncher()