import os, shutil
folder = './experiments/base_model/'
for the_file in os.listdir(folder):
    if the_file != "params.json":
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                print("deleting: ", file_path)
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
