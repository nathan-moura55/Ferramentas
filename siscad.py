import pyautogui as pa
import time
pa.PAUSE = 1

#abrir chrome
pa.press('win') 
pa.write("chrome")
pa.press('ENTER')

#entrar no siscad
time.sleep(5)
pa.write("https://siscad.uftm.edu.br/")
pa.press('ENTER')   

#informações de login
time.sleep(10)
pa.press('tab')
pa.write(usuario) #modificar usuario (matricula) 
pa.press('tab')
pa.write(senha) # inserir senha
pa.press('tab')
pa.press('ENTER')

#fechar aviso
time.sleep(10)
pa.press('ENTER')

#abrir notas
time.sleep(1)
pa.click(x=217, y=278)
pa.click(x=253, y=298)