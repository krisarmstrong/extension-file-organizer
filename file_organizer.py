
#/bin/bash

import os


def main():

    if os.system() == 'Darwin':
        os.system('clear')
        print(os.system('clear'))
    elif os.system == 'Linux':
        os.system('clear')
        print(os.system('clear'))
    elif os.system == 'Windows':
        os.system('cls')
        print(os.system('cls'))
    else:
        print('OS not supported')
    
    try:
        inputpath = ('What is the root path to the files you want to move')
        print(inputpath)
        root_path = inputpath
        output_path = ('What is the target path to the files you want to copy to')
        print(output_path)
        target_path = output_path
    except Exception as e:
        print(e)
    finally:
        pass
    
    dir_list = os.listdir(inputpath)
    for file in dir_list:
        print(file)
        file_path = os.path.join(inputpath, file)
        if os.path.isfile(file_path):
            print(file_path)
            file_name = os.path.basename(file_path)
            print(file_name)
 
    
    return 0 






if __name__ == '__main__':
    main()