import pymel.core


class CamWrapper(object):
    def __init__(self, camtransform):
        self.transform = pymel.core.PyNode(camtransform)
        self.shape = self.transform.getShape()

    def __getattr__(self, attr):
        return self.shape.getAttr(attr)

    def __setattr__(self, attr, value):
        super(CamWrapper, self).__setattr__(attr, value)


class NodeWrapper(object):
    def __init__(self, node):
        self.node = pymel.core.PyNode(node)

    def __getattr__(self, attr):
        return self.node.getAttr(attr)

    def __setattr__(self, attr, value):
        super(NodeWrapper, self).__setattr__(attr, value)


def main():
    cam = CamWrapper('camera1')
    print cam.shape
    print type(cam.shape)
    print cam.transform
    print type(cam.transform)

    print cam.shape.getAttr('focalLength')
    print cam.focalLength

    cam.focalLength = 132

    print cam.shape.getAttr('focalLength')
    print cam.focalLength
    print cam.farClipPlane

    # print cam.shape.focalLength
    # print cam.translateX

    ######

    cam2 = NodeWrapper('cameraShape1')
    print cam2.focalLength
    cam.focalLength = 95
    print cam.focalLength
    print cam2.focalLength
