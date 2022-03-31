import os
import subprocess
import numpy as np


def create_triangular_dist(path):
    dist_w = []
    tri_1 = []
    tri_2 = []
    tri_C = []
    test = 0
    print("Creating Triangular Distribution \n ")
    os.chdir(path+'/outputs/')
    #subprocess.run("pwd", shell=True)
    dist_w = list(np.random.triangular(0, 128, 256, 2150))
    for i in range(len(dist_w)):
        test = round(dist_w[i])
        if (test > 255):
            tri_1.append(test-1)
        else:
            tri_1.append(test)
    dist_w.clear
    dist_w = list(np.random.triangular(0, 128, 256, 2150))
    for i in range(len(dist_w)):
        test = round(dist_w[i])
        if (test > 255):
            tri_2.append(test-1)
        else:
            tri_2.append(test)
    for i in range(len(dist_w)):
        text = str(tri_1[i]) + "	" + str(tri_2[i])
        tri_C.append(text)
    ##print (tri_C)
    with open("triangular.txt", "w") as txt_file:
        for line in range(len(tri_C)):
            txt_file.write(tri_C[line] + "\n")
    txt_file.close
    dist_w.clear()
    tri_1.clear()
    tri_2.clear()
    tri_C.clear()


def create_discrete_dist(path):
    dist_w = []
    tri_1 = []
    tri_2 = []
    tri_C = []
    test = 0
    print("Creating Discrete Distribution \n")
    os.chdir(path+'/outputs/')
    dist_w = list(np.random.uniform(0, 256, 2150))
    for i in range(len(dist_w)):
        test = round(dist_w[i])
        if (test > 255):
            tri_1.append(test-1)
        else:
            tri_1.append(test)
    dist_w.clear
    dist_w = list(np.random.uniform(0, 256, 2150))
    for i in range(len(dist_w)):
        test = round(dist_w[i])
        if (test > 255):
            tri_2.append(test-1)
        else:
            tri_2.append(test)
    for i in range(len(dist_w)):
        text = str(tri_1[i]) + "	" + str(tri_2[i])
        tri_C.append(text)
    ##print (tri_C)
    with open("discrete.txt", "w") as txt_file:
        for line in range(len(tri_C)):
            txt_file.write(tri_C[line] + "\n")
    txt_file.close
    
    dist_w.clear()
    tri_1.clear()
    tri_2.clear()
    tri_C.clear()

def copy_dist(path, indx):
    os.chdir(path+'/outputs/')
    subprocess.run(
        "cp discrete.txt "+path+"/target/chisel-test_"+indx+"/distributions/discrete.txt", shell=True)
    subprocess.run(
        "cp triangular.txt "+path+"/target/chisel-test_"+indx+"/distributions/triangular.txt", shell=True)