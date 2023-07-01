# For characters or symbols in the Channel ID
invalid_characters = []
for char in range(ord('a'), ord('z')+1):
    invalid_characters.append(chr(char))
    invalid_characters.append(chr(char).upper())

for char in range(ord('!'), ord('/')+1):
    invalid_characters.append(chr(char))

for char in range(ord(':'), ord('@')+1):
    invalid_characters.append(chr(char))

for char in range(ord('['), ord('`')+1):
    invalid_characters.append(chr(char))

for char in range(ord('{'), ord('~')+1):
    invalid_characters.append(chr(char))


# List of user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; IMO Q2 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G996B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 GNews Android/2022027771',
    'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1816 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; M2007J3SG Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-T815Y Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 GNews Android/2022027771'
    'iTunes/4.7.1 (Linux; N; QLMS 2.X (QNAP TurboStation) [Debian 9 stretch]; aarch64-linux; DA; utf8) SqueezeCenter, Squeezebox Server, Logitech Media Server/8.3.0/1638573231'
    'Mozilla/5.0 (Linux; Android 10; SM-A125M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36'
]