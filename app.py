import random
import math
import io

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
import streamlit as st


# -------------------------------------------------
# Page settings
# -------------------------------------------------
st.set_page_config(
    page_title="Layered Memory Poster",
    page_icon="🎨",
    layout="centered"
)

st.title("Layered Memory Poster")
st.caption("Arts and Advanced Big Data | Interactive Generative Poster")
st.write("Adjust the controls to create your own layered abstract poster.")


# -------------------------------------------------
# Blob shape
# -------------------------------------------------
def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2 * math.pi, points, endpoint=False)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))

    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)

    return x, y


# -------------------------------------------------
# Color palette
# -------------------------------------------------
def make_palette(k=6, mode="soft", base_h=0.60):
    cols = []

    for _ in range(k):
        if mode == "soft":
            h = random.random()
            s = random.uniform(0.15, 0.35)
            v = random.uniform(0.88, 1.0)

        elif mode == "vivid":
            h = random.random()
            s = random.uniform(0.75, 1.0)
            v = random.uniform(0.8, 1.0)

        elif mode == "mono":
            h = base_h
            s = random.uniform(0.2, 0.6)
            v = random.uniform(0.5, 1.0)

        else:
            h = random.random()
            s = random.uniform(0.3, 1.0)
            v = random.uniform(0.5, 1.0)

        cols.append(tuple(hsv_to_rgb([h, s, v])))

    return cols


# -------------------------------------------------
# Draw poster
# -------------------------------------------------
def draw_poster(
    n_layers=10,
    wobble=0.12,
    palette_mode="soft",
    seed=42,
    background="warm"
):
    random.seed(seed)
    np.random.seed(seed)

    fig, ax = plt.subplots(figsize=(7, 9))

    if background == "warm":
        bg = (0.97, 0.95, 0.91)
    elif background == "cool":
        bg = (0.92, 0.95, 0.97)
    else:
        bg = (0.96, 0.96, 0.96)

    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    ax.axis("off")

    palette = make_palette(6, mode=palette_mode)
