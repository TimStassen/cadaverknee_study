import elastix
import os

elastix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\elastix.exe')

fixed_image = r''
fixed_im_mask = r''
full_path_moving_im = r''
parameter_file = r''
spec_results_path = r''

el = elastix.ElastixInterface(elastix_path=elastix_path)
el.register(
    fixed_image=fixed_image,
    fixed_mask=fixed_im_mask,
    moving_image=full_path_moving_im,
    parameters=parameter_file,
    output_dir=spec_results_path)