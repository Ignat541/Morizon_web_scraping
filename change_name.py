import os.path
import sys
from psd_tools import PSDImage
import shutil

DIR = "./tests/"
EXT = ".psd"
DEST_masks = 'C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\replaced_files\\masks'
DEST_rgb = 'C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\replaced_files\\rgb'


if __name__ == "__main__":

	if len(sys.argv) > 1:
		if os.path.exists(sys.argv[1]) and os.path.isdir(sys.argv[1]):
			DIR = sys.argv[1] + '/' if sys.argv[1][-1] != '/' else sys.argv[1]
		else:
			print("Invalid path provided")
			exit(1)

	files = []
	for file in os.listdir(DIR):
		if file.endswith(EXT):
			files.append(os.path.splitext(file)[0])

	for file_name in files:
		psd_file = PSDImage.open(DIR + file_name + EXT)

		savepath = os.path.join(DIR, file_name)
		if not os.path.exists(savepath) and len(psd_file) > 0:
			os.makedirs(savepath)

		for layer in psd_file:
			layer_src = layer.composite()
			x = layer_src.save(f"{savepath}/{layer.name}.png")



"""adds folder name to the all files in that folder """
lst = []
pano_number = 0
i = 0
files = os.listdir(DIR)
for items in files:
	if not items.endswith('.psd'):
		old_item_name = os.path.join(DIR, items)
		items = items.split('_' or '-')
		pano_number += 1
		new_item_name = items[0] + '_' + str(pano_number)
		new_item_name = os.path.join(DIR, new_item_name)
		os.rename(old_item_name, new_item_name)
		new_item_name = os.path.abspath(new_item_name)
		end = new_item_name[0:45] + new_item_name[45:]
		inside_folder = os.listdir(end)
		for j, el in enumerate(inside_folder):
			if el == 'Tło.png':
				i += 1
				tlo_path = os.path.abspath(el)
				tlo_path = tlo_path[:45]
				tlo_path = tlo_path + 'tests\\pano_' + str(pano_number) + '\Tło.png'
				DEST_rgb = 'C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\replaced_files\\rgb'
				DEST_rgb = os.path.join(DEST_rgb, f"{i}.png")
				shutil.copy(tlo_path, DEST_rgb)

		if 'punkty.png' in inside_folder:
			inside_folder.remove('punkty.png')
			if 'Tło.png' in inside_folder:
				shutil.copy(new_item_name + '\\' + 'Tło.png', DEST_rgb)
				inside_folder.remove('Tło.png')
		for items in inside_folder:
			inside_files = new_item_name + "_" + items
			inside_files = inside_files[51:]
			inside_files = list(inside_files)
			inside_files.insert(7, inside_files[-5])
			x = ''.join(inside_files)
			x = list(x)
			x.insert(8, inside_files[4])
			x_2 = ''.join(x)
			last_x = x_2.replace(x_2[-5::], '')
			final_files = last_x.strip() + '.png'



			old_file_names = os.path.join(new_item_name, items)
			new_file_names = os.path.join(new_item_name, final_files)
			os.rename(old_file_names, new_file_names)



			src_path = new_item_name + '\\' + final_files
			dest_path = DEST_masks + '\\' + final_files
			shutil.copy(src_path, dest_path)



