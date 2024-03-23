import math
import numpy as np


def translate2D(tx, ty, tm=None):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    
    if tm is not None:
        tm = np.eye(3)
        
    tm_new = np.dot(translation_matrix, tm)
    return tm_new

def scale2D(sx, sy, refx, refy, tm=None):
    if tm is None:
        tm = np.eye(3)
        
    tm = np.dot(np.array([
        [1, 0, -refx],
        [0, 1, -refy],
        [0, 0, 1]
    ]), tm)
    
    tm = np.dot(np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]), tm)
    
    tm = np.dot(np.array([
        [1, 0, refx],
        [0, 1, refy],
        [0, 0, 1]
    ]), tm)
    
    return tm

def rotate2D(a, refx, refy, tm=None):
    a_rad = math.radians(a)
    cos_a = math.cos(a_rad)
    sin_a = math.sin(a_rad)
    
    translation_matrix1 = np.array([
        [1, 0, -refx],
        [0, 1, -refy],
        [0, 0, 1]
    ])
    
    translation_matrix2 = np.array([
        [1, 0, refx],
        [0, 1, refy],
        [0, 0, 1]
    ])
    
    rotation_matrix = np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ])
    
    if tm is None:
        tm = np.eye(3)
    
    rotated_matrix = np.dot(translation_matrix2, np.dot(rotation_matrix, np.dot(translation_matrix1, tm)))
    
    if tm is not None:
        tm = np.eye(3)
    
    return np.dot(rotated_matrix, tm)

def shear2D(kx, ky, refx, refy, tm=None):
    if tm is None:
        tm = np.eye(3)
    
    shear_matrix = np.array([
        [1, kx, -refx * kx],
        [ky, 1, -refy * ky],
        [0, 0, 1]
    ])
    return np.dot(shear_matrix, tm)

def mirror2D(axis, refx, refy, tm=None):
    if tm is None:
        tm = np.eye(3)
    
    if axis.lower() == 'x':
        mirror_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis.lower() == 'y':
        mirror_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    else:
        mirror_matrix = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    
    translation_matrix1 = np.array([
        [1, 0, -refx],
        [0, 1, -refy],
        [0, 0, 1]
    ])
    
    translation_matrix2 = np.array([
        [1, 0, refx],
        [0, 1, refy],
        [0, 0, 1]
    ])
        
    tm_new = np.dot(
        np.dot(
            np.dot(translation_matrix2, mirror_matrix),
            tm
        ),
        translation_matrix1
    )
    
    return tm_new

def transformPoints2D(pts, tm=None):
    if tm is None:
        tm = np.eye(3)
        
    i, _ = pts.shape
    
    for j in range(i):
        tmp = tm[0][0] * pts[j][0] + tm[0][1] * pts[j][1] + tm[0][2]
        pts[j][1] = tm[1][0] * pts[j][0] + tm[1][1] * pts[j][1] + tm[1][2]
        pts[j][0] = tmp
        
    return