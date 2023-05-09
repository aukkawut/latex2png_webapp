import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image

def crop_image(image_path):
    with Image.open(image_path) as img:
        image_data = img.getdata()
        non_empty_columns = [x for x in range(img.width) if any(image_data[x + img.width * y][3] != 0 for y in range(img.height))]
        non_empty_rows = [y for y in range(img.height) if any(image_data[x + img.width * y][3] != 0 for x in range(img.width))]
        
        if non_empty_columns and non_empty_rows:
            cropped_image = img.crop((min(non_empty_columns),
                                      min(non_empty_rows),
                                      max(non_empty_columns) + 1,
                                      max(non_empty_rows) + 1))
            cropped_image.save(image_path)

def latex_to_png(latex_code, output_filename, text_color='black', font_size=12, dpi=1200):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}\usepackage{amssymb}'
    mpl.rcParams['font.size'] = font_size
    mpl.rcParams['text.color'] = text_color
    fig = plt.figure(figsize=(1, 1), dpi=dpi)
    fig.patch.set_alpha(0)
    ax = plt.gca()
    ax.axis('off')
    latex_code = r'\begin{center}' + latex_code + r'\end{center}'
    plt.text(0, 0, latex_code)
    fig.tight_layout(pad=0)
    plt.savefig(output_filename, transparent=True, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    crop_image(output_filename)
