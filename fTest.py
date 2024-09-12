import ftplib
import datetime

SERVER_IP = '192.168.107.128'
FTP_LOGIN = 'msfadmin'

def upload():
    ftp = ftplib.FTP(SERVER_IP)
    ftp.login(FTP_LOGIN,FTP_LOGIN)
    with open(r'text.xlsx','rb') as f:
        ftp.storbinary(f'STOR {datetime.datetime.now().strftime(r'%Y-%m-%d')}_dayily_report.xlsx', f)
        f.close()
    ftp.quit()
    

def connectFtp():
    ftp = ftplib.FTP(SERVER_IP)
    ftp.login(FTP_LOGIN,FTP_LOGIN)

    with open('chache.xlsx','wb') as file:
        ftp.retrbinary(f'RETR {datetime.datetime.now().strftime(r'%Y-%m-%d')}_dayily_report.xlsx', file.write)
        file.close()
    
    # print(l.split())

    ftp.quit()

upload()
connectFtp()