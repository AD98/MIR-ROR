import inspect
import pathlib

def getSourceFilePath():
    
    fpThis = pathlib.Path(inspect.getfile(getSourceFilePath)).resolve()
    
    # this file is in ./python/utils.py --> root is parent
    fpMirror = fpThis.parent.parent
    print("Found mirror root: " + str(fpMirror))
    if 'img' not in [x.name for x in fpMirror.iterdir()]:
            raise Exception('cannot find expected mirror directory: %s' % fpMirror)
    return fpMirror

