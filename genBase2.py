import maya.cmds as cmds
import random

# Define the file path
file_path = 'D:/Noise/noiseperlin.png'

# Check if the file node exists
file_node_exists = cmds.objExists('file_texture')

    

# If the file node doesn't exist, run the usual code
if not file_node_exists:
    # Create a plane
    plane = cmds.polyPlane(width=10, height=10, subdivisionsX=10, subdivisionsY=10)[0]

    # Create a Lambert material
    lambert_shader = cmds.shadingNode('lambert', asShader=True)

    # Create a file texture node for the Perlin noise texture
    file_texture = cmds.shadingNode('file', asTexture=True, name='file_texture')
    cmds.setAttr(file_texture + '.fileTextureName', file_path, type="string")

    # Create a place2dTexture node
    place2d_texture = cmds.shadingNode('place2dTexture', asUtility=True, name='place2d_texture')

    # Set UV mirror
    cmds.setAttr(place2d_texture + '.mirrorU', True)
    cmds.setAttr(place2d_texture + '.mirrorV', True)

    # Generate random UV offsets
    offsetU = random.uniform(0, 1 - 1024/8640.0)
    offsetV = random.uniform(0, 1 - 1024/8640.0)

    # Generate random UV scaling
    scaleU = random.uniform(0.15, 0.5)
    scaleV = random.uniform(0.15, 0.5)

    # Set the offset and scale values in the place2dTexture node
    cmds.setAttr(place2d_texture + '.offsetU', offsetU)
    cmds.setAttr(place2d_texture + '.offsetV', offsetV)
    cmds.setAttr(place2d_texture + '.repeatU', scaleU)
    cmds.setAttr(place2d_texture + '.repeatV', scaleV)

    # Connect the place2dTexture node to the file texture node
    cmds.connectAttr(place2d_texture + '.outUV', file_texture + '.uvCoord')
    cmds.connectAttr(place2d_texture + '.outUvFilterSize', file_texture + '.uvFilterSize')

    # Connect the file texture node to the Lambert material's color attribute
    cmds.connectAttr(file_texture + '.outColor', lambert_shader + '.color')

    # Create a displacement shader node
    displacement_node = cmds.shadingNode('displacementShader', asShader=True)

    # Connect the Perlin noise texture to the displacement shader node's displacement attribute
    cmds.connectAttr(file_texture + '.outAlpha', displacement_node + '.displacement')

    # Create a shading group for Lambert material
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)

    # Connect the Lambert shader and Displacement shader to the shading group
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')
    cmds.connectAttr(displacement_node + '.displacement', shading_group + '.displacementShader')

    # Assign the shading group to the plane's shape node
    plane_shape = cmds.listRelatives(plane, shapes=True)[0]
    cmds.sets(plane_shape, edit=True, forceElement=shading_group)

    # Apply smoothing to the plane
    cmds.polySmooth(plane, divisions=2, method=0)
    
    

if file_node_exists:

    # Set UV mirror
    cmds.setAttr(place2d_texture + '.mirrorU', True)
    cmds.setAttr(place2d_texture + '.mirrorV', True)
    
    # Generate random UV offsets
    offsetU = random.uniform(0, 1 - 1024/8640.0)
    offsetV = random.uniform(0, 1 - 1024/8640.0)

    # Generate random UV scaling
    scaleU = random.uniform(0.15, 0.3)
    scaleV = random.uniform(0.15, 0.3)
        
    # Set the offset and scale values in the place2dTexture node
    cmds.setAttr(place2d_texture + '.offsetU', offsetU)
    cmds.setAttr(place2d_texture + '.offsetV', offsetV)
    cmds.setAttr(place2d_texture + '.repeatU', scaleU)
    cmds.setAttr(place2d_texture + '.repeatV', scaleV)