import os
import subprocess
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def database_output(apr_num, sum, area, power, NMED_N, NMED_T, NMED_D):
    print(" \n \n Creating database \n \n")
    os.chdir('/home/prj/design-flow/outputs/')
    subprocess.run("pwd", shell=True)

    with open("database.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=',')
        ##print (sum_array)
        ##print (expected_normal)
        ##print (got_triangular)
        ##print (expected_triangular)
        ##print (got_discrete)
        ##print (expected_discrete)
        writer.writerow(
            [apr_num, sum, area, power, NMED_N, NMED_T, NMED_D])
        # file.close


"""
def plot_data(area_array, power_array, sum_array, NMED_array):
    os.chdir('/home/prj/design-flow/')
    l = len(area_array)
    index = np.linspace(0, l, l)
    print(index)

    fig, ax = plt.subplots(1, 1)
    plt.subplots_adjust(bottom=0.2)
    ax.plot(index, power_array, marker="v", lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('Power (W)')
    plt.title('Power consumed')
    ax.grid(True)
    # plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/power.png")
    plt.close()

    fig, ax = plt.subplots(1, 1)
    plt.subplots_adjust(bottom=0.2)
    plt.plot(index, area_array, marker="v", lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('Area (u^2)')
    plt.title('Area')
    ax.grid(True)
    # plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/area.png")
    plt.close()

    fig, ax = plt.subplots(1, 1)
    plt.subplots_adjust(bottom=0.2)
    ax.plot(index, power_array, marker="v", lw=1)
    plt.plot(index, NMED_array, marker="v", lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('NMED)')
    plt.title('NMED')
    ax.grid(True)
    # plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/NMED.png")
    plt.close()

"""
