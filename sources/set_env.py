#!/usr/bin/python3
import os
import subprocess
import re
import sources.replace as replace_lib
from multiprocessing import Process, Queue


def define_dir_path():
    path = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)
    return str(path.stdout)[2:-3]

def cp_chisel(n):
    subprocess.run(
        "cp -R /home/prj/chisel-test chisel-test_"+n+"/", shell=True)


def create_chisel_copy(path):
    print("Creating chisel instances for multiprocesing \n \n")
    os.chdir(path+'/target/')
    subprocesses = []
    subprocess.run(
        "rm -rf chisel-test*", shell=True)
    p1 = Process(target=cp_chisel, args=("1", ))
    p1.start()
    p2 = Process(target=cp_chisel, args=("2", ))
    p2.start()
    p3 = Process(target=cp_chisel, args=("3", ))
    p3.start()
    p4 = Process(target=cp_chisel, args=("4", ))
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()


def cp_openlane(n):
    subprocess.run(
        "cp -R /home/prj/OpenLane OpenLane_"+n+"/", shell=True)


def create_openlane_copy(path):
    print("Creating OpenLane instances for multiprocesing \n \n")
    os.chdir(path+'/target/')
    subprocesses = []
    p1 = Process(target=cp_openlane, args=("1", ))
    p1.start()
    p2 = Process(target=cp_openlane, args=("2", ))
    p2.start()
    p3 = Process(target=cp_openlane, args=("3", ))
    p3.start()
    p4 = Process(target=cp_openlane, args=("4", ))
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

"""
def create_containers(path, indx):

    hay que crer esta funcion
    de debe meter a cada folcer de OpenLane_X y ejecutar "make mount"
    aca uno queda dentro del command line del docker, hay que salirse
    sin matar el contenedor
    luego hay que ejecutar "docker ps" y sacar el nombre de cada contenedor
    para asignarlos en la funcion openlane_flow.run_openlane()
    es importante que los nombre de los contenedores de cada folder
    openlane_X coincida sino se mezclan los resultados

def stop_containers():
    se deberia tambien crear esta funcion para matar los contenedores

"""