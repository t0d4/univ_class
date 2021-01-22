"""
Requirements:
 - numpy
 - matplotlib
 - Pillow
"""
import os
import sys
import argparse
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as anm

COLORS = matplotlib.colors.TABLEAU_COLORS.items()
"""
    #=> COLORS == OrderedDict([('tab:blue', '#1f77b4'),
    #=>                  ('tab:orange', '#ff7f0e'),
    #=>                  ('tab:green', '#2ca02c'),
    #=>                  ('tab:red', '#d62728'),
    #=>                  ('tab:purple', '#9467bd'),
    #=>                  ('tab:brown', '#8c564b'),
    #=>                  ('tab:pink', '#e377c2'),
    #=>                  ('tab:gray', '#7f7f7f'),
    #=>                  ('tab:olive', '#bcbd22'),
    #=>                  ('tab:cyan', '#17becf')])
"""


def plot_animation_updater(i: int, datalist: list, color_codes: list):

    plt.xlim(0, 100)
    plt.ylim(0, 10)
    for data, color in zip(datalist, color_codes):
        try:
            moment = data["time_and_coordinates"][i]
        except IndexError:  # When data has no more elements
            pass
        else:
            if i == 0:  # When the first frame is illustrated, label name is set
                plt.scatter(moment[1], moment[2], color=color, label=data["filename"])
                plt.legend()
            else:
                plt.scatter(moment[1], moment[2], color=color)
            plt.title(f"t={moment[0]}")


def main(files: list, config: dict):

    datalist = []
    for file in files:
        data = {"filename": file, "time_and_coordinates": []}

        if not os.path.exists(file):
            print(f"{file} was not found.")
            sys.exit(1)

        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                # Convert each element from str to float
                data["time_and_coordinates"].append([float(num) for num in row])
        datalist.append(data)

    if config["export_png"] is True:
        static_graph = plt.figure()
        axis = static_graph.add_subplot(111, xlabel="x-coordinate", ylabel="y-coordinate")
        for data, (_, color_code) in zip(datalist, COLORS):
            for idx, moment in enumerate(data["time_and_coordinates"]):
                # When the first point is plotted, label name is set
                if idx == 0:
                    axis.scatter(moment[1], moment[2], color=color_code, label=data["filename"])
                else:
                    axis.scatter(moment[1], moment[2], color=color_code)
        _, y_max = axis.get_ylim()
        axis.set_ylim(0, y_max)
        plt.legend()
        plt.savefig("graph.png")

    # Clear the illustration area
    plt.cla()

    animation_figure = plt.figure()
    animation_figure.add_subplot(111, xlabel="x-coordinate", ylabel="y-coordinate")
    color_codes = [color_code for _, color_code in COLORS]
    color_codes = color_codes[0:len(datalist)]
    # Fetch the number of frames of the longest throw
    animation_frames = max([len(data["time_and_coordinates"]) for data in datalist])
    ani = anm.FuncAnimation(animation_figure, plot_animation_updater, fargs=(datalist, color_codes),
                            interval=100, frames=animation_frames)

    if config["export_gif"] is True:
        ani.save("animation.gif")

    #plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="csv file names, separated by spaces")
    parser.add_argument("--export-png", help="Export graph as a png file", action="store_true")
    parser.add_argument("--export-gif", help="Export animation as a gif file", action="store_true")
    args = parser.parse_args()
    config = {"export_png": args.export_png, "export_gif": args.export_gif}

    if len(args.files) > len(COLORS):
        print(f"This program can't handle more than {len(COLORS)} files.")
    else:
        main(args.files, config)
