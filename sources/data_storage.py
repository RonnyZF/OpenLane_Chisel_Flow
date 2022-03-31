import os
import subprocess
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def clean_database(path):
    print("Cleaning database \n")
    os.chdir(path+'/outputs/')
    subprocess.run(
        "mv database.csv database.csv_old", shell=True)
    subprocess.run(
        "rm -rfv database.csv", shell=True)


def database_output(path, apr_num, sum, area, power, NMED_N, NMED_T, NMED_D):
    print("Saving database \n")
    os.chdir(path+'/outputs/')
    with open("database.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for a in range(4):
            apr_num_out = apr_num[a]
            sum_out = sum[a]
            area_out = area[a]
            power_out = power[a]
            NMED_N_out = NMED_N[a]
            NMED_T_out = NMED_T[a]
            NMED_D_out = NMED_D[a]
            writer.writerow([apr_num_out, sum_out, area_out,
                            power_out, NMED_N_out, NMED_T_out, NMED_D_out])
    file.close


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
