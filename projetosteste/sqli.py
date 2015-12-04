#!/usr/bin/python

#################################################################
import os, sys, httplib

#################################################################
def principal():
    os.system("reset")
    print """ \033[1m
    ========================================================== \033[0m
                      (`.         ,-,
                        ` `.    ,;' /   \033[91mScanner (SQLi) \033[0m
                         `.  ,'/ .'     Desenvolvido por\033[96m Deivid\033[0m
                          `. X /.'
                .-;--''--.._` ` (
              .'            /   `  
             ,           ` '   Q '  
             ,         ,   `._    \      
          ,.|         '     `-.;_'  
          :  . `  ;    `  ` --,.._;  
           ' `    ,   )   .'  
              `._ ,  '   /_
                 ; ,''-,;' ``-
                  ``-..__``--`
                     \033[0m  \033[1m
    ========================================================== \033[0m
              """
    try:         
         escolha = int(input("    Escolhas: \n    [1] Scanner de SQL Injection \n    [2] Finalizar script \n \033[96m\n    Escolha: \033[0m"))                                                                                                                                  


    except:
        print "\n Escolha invalida.."
        principal()  
       
    if escolha ==1:
           sqli()
    elif escolha ==2:
            print "Finalizando script..."
            os.system("reset")
            sys.exit(1)
    else:
            print "else"   
            
#################################################################
def sqli():
                os.system("reset")
                print "   ================================"
                print "\033[92m       Scanner de SQL Injection \033[0m"
                print "   ================================"
                
                site_sqli = raw_input("\n \033[94m  Site (ex:www.site_alvo.com.br): \033[0m")
                site_sqli = site_sqli.replace("http://", "")
                site_path = raw_input("\033[96m   Diretorio (ex:/noticias.php?id=5565): \033[0m")
                if site_path[0] != "/":
                          site_path = "/" + site_path               
                
                con = httplib.HTTPConnection(site_sqli)
                con.request("GET",  site_path+"'" )
                resp = con.getresponse()
                if resp.status == 200:
                         codigo_resp = resp.read()
                         enc = codigo_resp.find("You have an error in your")
                         if enc == -1:
                              print "   ------------------\n \033[91m  Nenhuma falha detectada.\033[0m\n   ------------------ \n"
                         elif enc != -1:
                              print "   ------------------\n \033[1m  Possivel falha detectada. \033[0m \n   " + site_sqli + site_path + "'"   
                              print "  ------------------"
      
principal()