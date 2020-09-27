from xml.dom import minidom
import random

root = minidom.Document()

base_robot = root.createElement('robot')
root.appendChild(base_robot)

mat1 = root.createElement("material")
mat1.setAttribute("name", "Grey")
color1 = root.createElement("color")
color1.setAttribute('rgba', "0.2 0.2 0.2 1.0")
mat1.appendChild(color1)
base_robot.appendChild(mat1)

mat2 = root.createElement("material")
mat2.setAttribute("name", "Orange")
color2 = root.createElement("color")
color2.setAttribute('rgba', "1.0 0.42 0.039 1.0")
mat2.appendChild(color2)
base_robot.appendChild(mat2)

mat3 = root.createElement("material")
mat3.setAttribute("name", "Blue")
color3 = root.createElement("color")
color3.setAttribute('rgba', "0.5 0.7 1.0 1.0")
mat3.appendChild(color3)
base_robot.appendChild(mat3)

def create_URDF():
    def link_properties():
        material = ["Grey", "Orange", "Blue"]

        print("\n -----Enter Links Details----- \n")
        name = str(input("Enter Link Name = "))
        rpy = input("Enter (Roll Pitch Yaw) values = ")
        xyz = input("Enter Cartesian Coordinate values (X Y Z) = ")
        mass = input("Enter Mass Value = ")
        print("\n -----Enter Inertia values----- \n")
        ixx, ixy, ixz = input("ixx = "), input("ixy = "), input("ixz = ")
        iyy, iyz, izz = input("iyy = "), input("iyz = "), input("izz = ")
        print("\n -----Enter Visual Details----- \n")
        v_rpy = input("Enter (Roll, Pitch, Yaw) values for visual = ")
        v_xyz = input("Enter Cartesian Coordinate values (X, Y, Z) for visual = ")
        v_file = input("Enter path of .obj file = ")
        print("\n -----Enter Collision Details----- \n")
        c_rpy = input("Enter (Roll, Pitch, Yaw) values for collision = ")
        c_xyz = input("Enter Cartesian Coordinate values (X, Y, Z) for collision = ")
        c_file = input("Enter path of .stl file = ")

        links = root.createElement("link")
        links.setAttribute('name', name)
        # Inertial properties of the link
        inertia = root.createElement("inertial")
        links.appendChild(inertia)
        origin, _mass, _inertia = root.createElement("origin"), root.createElement("mass"), root.createElement("inertia")
        origin.setAttribute("rpy", rpy), origin.setAttribute("xyz", xyz)
        _mass.setAttribute("value", mass)
        _inertia.setAttribute("ixx", ixx), _inertia.setAttribute("ixy", ixy), _inertia.setAttribute("ixz", ixz)
        _inertia.setAttribute("iyy", iyy), _inertia.setAttribute("iyz", iyz), _inertia.setAttribute("izz", izz)
        inertia.appendChild(origin), inertia.appendChild(_mass), inertia.appendChild(_inertia)
        # visual properties of link
        visual = root.createElement("visual")
        links.appendChild(visual)
        v_origin, v_geo, v_mesh, v_mat = root.createElement("origin"), root.createElement("geometry"), root.createElement(
            "mesh"), root.createElement("material")
        v_origin.setAttribute("rpy", v_rpy), v_origin.setAttribute("xyz", v_xyz)
        v_mesh.setAttribute("filename", v_file), v_mat.setAttribute("name", material[random.randint(0, 2)])
        visual.appendChild(v_origin), visual.appendChild(v_geo), visual.appendChild(v_mat), v_geo.appendChild(v_mesh)
        # Collision properties of link
        collision = root.createElement("collision")
        links.appendChild(collision)
        c_origin, c_geo, c_mesh = root.createElement("origin"), root.createElement("geometry"), root.createElement(
            "mesh")
        c_origin.setAttribute("rpy", c_rpy), c_origin.setAttribute("xyz", c_xyz)
        c_mesh.setAttribute("filename", c_file)
        collision.appendChild(c_origin), collision.appendChild(c_geo), c_geo.appendChild(c_mesh)
        base_robot.appendChild(links)


    def joint_properties():
        print("\n -----Enter Joint Details----- \n")
        j_name, j_type = str(input("Enter Joint name = ")), str(input("Enter Joint type = "))
        p_link, c_link = str(input("Enter Parent link name = ")), str(input("Enter Child link name = "))
        j_rpy = input("Enter (Roll Pitch Yaw) values = ")
        j_xyz = input("Enter Cartesian Coordinate values (X Y Z) = ")
        j_axis = input("Enter axis of movement (X Y Z) = ")

        joint = root.createElement("joint")
        joint.setAttribute("name", j_name), joint.setAttribute("type", j_type)
        parent, child, origin = root.createElement("parent"), root.createElement("child"), root.createElement("origin")
        axis = root.createElement("axis")
        parent.setAttribute("link", p_link), child.setAttribute("link", c_link)
        origin.setAttribute("rpy", j_rpy), origin.setAttribute("xyz", j_xyz)
        axis.setAttribute("xyz", j_axis)
        joint.appendChild(parent), joint.appendChild(child), joint.appendChild(origin), joint.appendChild(axis)
        base_robot.appendChild(joint)


    no_links = int(input("Enter numbers of Links in Robot = "))
    no_joints = int(input("Enter number of joints in Robot = "))
    filename = str(input("Enter file name with path without extension = "))
    for i in range(no_links):
        link_properties()
    for j in range(no_joints):
        joint_properties()

    xml_str = root.toprettyxml(indent="\t")
    save_path_file = filename+".xml"
    with open(save_path_file, "w") as f:
        f.write(xml_str)


if __name__ == "__main__":
    create_URDF()