import tripy
import numpy as np
from stl import mesh

# Load a PLY file
def load_ply(file_path):
    with open(file_path, 'r') as ply_file:
        lines = ply_file.readlines()
    vertex_data = []
    is_vertex_section = False

    for line in lines:
        if 'end_header' in line:
            is_vertex_section = True
            continue

        if is_vertex_section:
            vertex = line.strip().split()
            if len(vertex) == 3:
                vertex_data.append([float(vertex[0]), float(vertex[1]), float(vertex[2])])

    vertices = np.array(vertex_data)
    return vertices

# Convert PLY to STL
def ply_to_stl(ply_file_path, stl_file_path):
    vertices = load_ply(ply_file_path)
    triangles = tripy.earclip(vertices)

    # Create an empty STL mesh
    mesh_stl = mesh.Mesh(np.zeros(len(triangles), dtype=mesh.Mesh.dtype))

    for i, triangle in enumerate(triangles):
        for j in range(3):
            mesh_stl.vectors[i][j] = triangle[j]

    # Write the STL mesh to a file
    mesh_stl.save(stl_file_path)

if __name__ == "__main__":
    ply_file_path = 'input.ply'
    stl_file_path = 'output.stl'
    ply_to_stl(ply_file_path, stl_file_path)