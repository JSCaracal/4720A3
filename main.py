# Import necessary libraries
import pygame as pg
from OpenGL.GL import *
import numpy as np

from objLoaderV2 import ObjLoader
import shaderLoader


# Initialize pygame
pg.init()

# Set up OpenGL context version
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)


# Create a window for graphics using OpenGL
width = 640
height = 480
pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF)


glClearColor(0.3, 0.4, 0.5, 1.0)
# Todo: Enable depth testing here using glEnable()
glEnable()


# Todo: Part 3: Write shaders (vertex and fragment shaders) and compile them here




# Todo: Part 1: Read the 3D model
# Lets setup our scene geometry.
obj = ObjLoader("objects/raymanModel.obj")
vertices = np.array(obj.vertices, dtype="float32")
center = obj.center
dia = obj.dia
size_position = 3
size_color = 3
stride = (size_position + size_color) * 4     # stride is the number of bytes between each vertex
offset_position = 0                           # offset of the position data
offset_color = size_position * 4              # offset of the color data. Color data starts after 3 floats (12 bytes) of position data
n_vertices = len(vertices) // (size_position + size_color)   # number of vertices
scale = 2.0/dia
#center = 
ascpet = width/height


# Todo: Part 2: Upload the model data to the GPU. Create a VAO and VBO for the model data.
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)     # Bind the buffer. That is, make it the active one.
glBufferData(GL_ARRAY_BUFFER,
             size=vertices.nbytes,
             data=vertices,
             usage=GL_STATIC_DRAW)


# Todo: Part 4: Configure vertex attributes using the variables defined in Part 1




# Todo: Part 5: Configure uniform variables.




# Todo: Part 6: Do the final rendering. In the rendering loop, do the following:
    # - Clear the color buffer and depth buffer before drawing each frame using glClear()
    # - Use the shader program using glUseProgram()
    # - Bind the VAO using glBindVertexArray()
    # - Draw the triangle using glDrawArrays()


# Run a loop to keep the program running
draw = True
while draw:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            draw = False

    # Clear color buffer and depth buffer before drawing each frame
    glClear(GL_COLOR_BUFFER_BIT)



    # Refresh the display to show what's been drawn
    pg.display.flip()


# Cleanup
glDeleteVertexArrays(1, [vao])
glDeleteBuffers(1, [vbo])
glDeleteProgram(shader)

pg.quit()   # Close the graphics window
quit()      # Exit the program