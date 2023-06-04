import imageio
from natsort import natsorted
import os
from os import path

workspace_path = os.getcwd()

decreasing_path = path.join(workspace_path, "pngs")

def make_animation(image_path, out_file, looped = False):

    list_of_im_paths = os.listdir(image_path)
    list_of_im_paths = natsorted(list_of_im_paths)

    ims = [imageio.imread(path.join(image_path, f)) for f in list_of_im_paths]

    ims += [ims[-1]] * 20

    if looped:
        ims = ims + list(reversed(ims))

    animation_path = path.join(workspace_path, out_file)

    imageio.mimwrite(animation_path, ims)

make_animation(decreasing_path, path.join("gifs", "decreasing.gif"))
make_animation(decreasing_path, path.join("gifs", "loop.gif"), looped=True)