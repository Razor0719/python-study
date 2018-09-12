from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('send from python', 'plain', 'utf-8')
# msg = MIMEMultipart('alternative') 支持html加plain
msg['From'] = _format_addr('someone<%s>' % from_addr)
msg['To'] = _format_addr('anotherone<%s>' % to_addr)
msg['Subject'] = Header('to study python', 'utf-8').encode()

import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
