import os, zipfile, datetime, statistics, time, re

day_week = datetime.datetime.today()
path, name_zip = 'Mini_Proyecto_Copia_Seguridad\\', '{:%A}.zip'.format(day_week)
full_path = '{}{}'.format(path, name_zip)
day = 0
while day<1:
    def copysecurity():
        path_copy = 'C:\\Users\\XXX\\Desktop\\'
        count = 0
        weight = []
        if os.path.exists(full_path) is True:
            os.remove(full_path)
        zip_security = zipfile.ZipFile(full_path, 'w')
        for folder, subfolders, files in os.walk(path_copy):
            for file in files:
                if file.endswith(('.py', '.md', '.rst', '.csv')):
                    file_path = '{}\\{}'.format(folder, file)
                    sizefile = os.stat(file_path).st_size
                    weight.append(sizefile)
                    zip_security.write(os.path.join(folder, file), 
                    file, compress_type = zipfile.ZIP_DEFLATED)
                    count += 1
                    print('Archivo incluido en el zip ', file)
        print('Numero de archivos ', count)
        print('Tamaño total de los archivos ', sum(weight), 'bytes')
        print('Tamaño medio de los archivos ', statistics.median(weight), 'bytes')
        zip_security.close
    ini = datetime.datetime.now().second
    copysecurity()
    fin = datetime.datetime.now().second
    print('El programa ha tardado', fin - ini, 'segundos')
    time.sleep(14)
    day+=1
