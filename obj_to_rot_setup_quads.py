import matplotlib.pyplot as plt

# Holds the coord values
quad_shape_x = []
quad_shape_y = []
quad_shape_z = []

# Holds the coordinate values in point vector lists.
quad_shape_points = []

# Holds the enumerated vertices, but after decrementing to make them zero-based.
quad_shape_f = []


def importObj(shape_name):
    # Import the OBJ
    file = open(shape_name + '.obj')

    # Fills the list to become 2d matrices (list of lists) of point vectors and coord lists
    list_of_lines = file.readlines()
    vertex_count = 0
    for line in list_of_lines:
        if line[0] == 'v':
            vertex_count += 1
            # print(line)
            line_v = line.strip('v \n')
            # print(line_v)
            pnt_vect = line_v.split(' ')

            for index, str in enumerate(pnt_vect):
                # print(str)
                pnt_vect[index] = float(str)

            # print('pnt_vect', pnt_vect)
            quad_shape_points.append(pnt_vect)
            quad_shape_x.append(pnt_vect[0])
            quad_shape_y.append(pnt_vect[1])
            quad_shape_z.append(pnt_vect[2])

        # Creates the face list
        if line[0] == 'f':

            line_f = line.strip('f \n')
            face = line_f.split(' ')

            print(face)

            for index, vector in enumerate(face):
                pnt_num = vector.split('/')[0]
                face[index] = int(pnt_num) - 1
            print(face)
            quad_shape_f.append(face)

    '''
    print('quad_shape_f')
    print(quad_shape_f)
    print('quad_shape_points')
    print(quad_shape_points)
    '''

    return vertex_count, quad_shape_x, quad_shape_y, quad_shape_z, quad_shape_points, quad_shape_f

    pass


def plot_shape(quad_shape_points, quad_shape_f):
    # GRID SETUP FOR SEQUENTIAL COMBINED ROTATIONS
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.axis([-2, 2, -2, 2])
    plt.axis('on')
    plt.grid(True)

    face_counter = 1
    # odd or even faces, based on 0 pattern

    # Loop to plot all faces for each quad
    mid = 0
    mids = ['y','r','purple','g','orange','b']
    top = 0
    tops = ['y','r','g','b','orange','purple']
    bot = 0
    bots = ['r','y','purple','orange','g','b']
    for face in quad_shape_f:
        # plt.plot([0,1],[0,1], color='k')

        # EXPLANATION AS TO HOW THE PLOT WORKS USING THE f VALUES IN THE OBJ
        # quad_shape_points holds the point vectors
        # quad_shape_f holds the sequence of enumerated points (in 1=1st ordinal)
        # The sequence of point vectors in quad_shape_f is used to draw all edges
        # to make a face.
        # Since quad_shape_points is a list of point vectors (list of lists),
        # it takes two indices to access each point value. The first, for the vector in
        # order in the list, and the second for the either x, y or z values.
        # To get the correct points to draw the face, we must use quad_shape_f because
        # it has the correct order of points for each face.
        # Thus, to get the correct indices for the first point vector to plot, we use
        # face[0], which tells us which point vector to use in the order of quad_shape_f
        # for plotting vertex 0 to 1
        # For example, to plot vertex 0 to 1
        # face[0] has the start ordinal for vertex 0. Then the second index is the [0]
        # to get the x value (eg. [1] is the y value, [2] is the z value).

        # plt.plot needs two values, one for x and one for y in this format [x,y]
        # The first point x val is:
        # quad_shape_points[  face[0] ] [0]
        # The first point y val is:
        # quad_shape_points[ face[1]] [0]
        if face_counter>=16 and face_counter%4==0 and face_counter<=44 :
            if face_counter<=20 or face_counter>=32 :
                plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                         [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                         color='k')
                plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                         [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                         color=mids[mid])
                plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                         [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                         color='k')
                plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                         [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                         color=mids[mid])
                mid += 1
        elif face_counter==18 or face_counter==22 or face_counter==38 or face_counter==46:
            plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                     [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                     [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                     [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                     color=tops[top])
            plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                     [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                     color='k')
            top += 1
        elif face_counter == 52 or face_counter ==54 :
            plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                     [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                     color=tops[top])
            plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                     [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                     [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                     [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                     color='k')
            top += 1
        elif face_counter == 42 or face_counter == 34 :
            plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                     [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                     [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                     [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                     color=bots[bot])
            plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                     [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                     color='k')
            bot += 1
        elif face_counter == 26 or face_counter == 30 or face_counter==48 or face_counter == 50 :
            plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                     [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                     color=bots[bot])
            plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                     [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                     [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                     color='k')
            plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                     [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                     color='k')
            bot += 1
        else :
            # vertex 0 to 1
            plt.plot([quad_shape_points[face[0]][0], quad_shape_points[face[1]][0]],
                     [quad_shape_points[face[0]][1], quad_shape_points[face[1]][1]],
                     color='k')
            # vertex 1 to 2
            plt.plot([quad_shape_points[face[1]][0], quad_shape_points[face[2]][0]],
                     [quad_shape_points[face[1]][1], quad_shape_points[face[2]][1]],
                     color='k')
            # to fill you just need two lists - x and y points. equal numbers.
            # vertex 2 to 3
            plt.plot([quad_shape_points[face[2]][0], quad_shape_points[face[3]][0]],
                     [quad_shape_points[face[2]][1], quad_shape_points[face[3]][1]],
                     color='k')

            # vertex 3 to 0
            plt.plot([quad_shape_points[face[3]][0], quad_shape_points[face[0]][0]],
                     [quad_shape_points[face[3]][1], quad_shape_points[face[0]][1]],
                     color='k')
        face_counter += 1
        pass
    #print(face_counter)
    plt.show()
    pass


def main():
    importObj('cube')
    plot_shape(quad_shape_points, quad_shape_f)
    pass

# main()
