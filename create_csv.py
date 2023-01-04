import os
from utils.image_proces import process_img
def create_csv(): # code taken from the internet
    
    mypath = 'abecedario'
    file_name = open('abecedario.csv', 'a')

    for each_folder in os.listdir(mypath):
        if '._' in each_folder:
            pass

        else:
            for each_number in os.listdir(mypath + '/' + each_folder):
                if '._' in each_number:
                    pass
                
                else:
                    label = each_folder

                    file_loc = mypath + '/' + each_folder + '/' + each_number

                    data = process_img(file_loc)
                    try:
                        for id,i in enumerate(data):
                            if id == 0:
                                print(i)
                            
                            file_name.write(str(i))
                            file_name.write(',')

                        file_name.write(label)
                        file_name.write('\n')
                    
                    except:
                        file_name.write('0')
                        file_name.write(',')

                        file_name.write('None')
                        file_name.write('\n')
       
    file_name.close()
    print('CSV Created')

if __name__ == "__main__":
    create_csv()




















