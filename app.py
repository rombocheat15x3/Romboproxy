# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, base64, datetime, re, socket, threading, random, telebot
from protobuf_decoder.protobuf_decoder import Parser
from masry import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock, Event
from cfonts import render, say
from telebot import types

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MaSrY_ToKeN = "7564503813:AAFnBj8AtNjT5lBLTvUz_7PXKJEeFhvWOvA"  
AUTHORIZED_USERS = []               
PaSs = "masry" 
MaSrY_Pp = "https://freeimage.host/i/qVCHouf"

# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G

socket_lock = Lock()
data_lock = Lock()
connected_clients = {}
connected_clients_lock = threading.Lock()

CliEnts = False
CliEnts2 = False

class xCLF():

    def __init__(xSeT, id, password):
        xSeT.id = id
        xSeT.password = password
        xSeT.thread_pool = ThreadPoolExecutor(max_workers=20)
        xSeT.active_threads = []
        xSeT.thread_timeout = 30
        xSeT.InPuTMsG = ""
        xSeT.DeCode_CliEnt_Uid = ""
        xSeT.max_retries = 3
        xSeT.retry_count = 0
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
        with connected_clients_lock:
            connected_clients[xSeT.id] = xSeT

        xSeT.GeNToKeNLogin()

    def GeTinFoSqMsG(xSeT, teamcode):
        try:
            if hasattr(xSeT, 'CliEnts2') and xSeT.CliEnts2:

                xSeT.DaTa2 = b""

                print(f"DEBUG: Sending JoinSq for teamcode: {teamcode}")
                xSeT.CliEnts2.send(JoinSq(teamcode, xSeT.key, xSeT.iv))

                start_wait = time.time()
                response_received = False

                while time.time() - start_wait < 5:
                    try:
                        xSeT.CliEnts2.settimeout(0.5)

                        chunk = xSeT.CliEnts2.recv(99999)
                        if chunk:
                            xSeT.DaTa2 += chunk
                            hex_data = xSeT.DaTa2.hex()

                            if len(hex_data) >= 10 and '0500' in hex_data[:10]:
                                print(f"DEBUG: Received 0500 packet, length: {len(hex_data)}")

                                try:
                                    if len(hex_data) > 10:
                                        decoded_data = DeCode_PackEt(hex_data[10:])
                                        print(f"DEBUG: Decoded data length: {len(decoded_data)}")

                                        dT = json.loads(decoded_data)
                                        print(f"DEBUG: Response structure keys: {list(dT.keys())}")

                                        OwNer_UiD, SQuAD_CoDe, ChaT_CoDe = GeTSQDaTa(dT)

                                        print(f"DEBUG EXTRACTED DATA:")
                                        print(f"  Owner UID: {OwNer_UiD}")
                                        print(f"  Squad Code: {SQuAD_CoDe}")
                                        print(f"  Chat Code: {ChaT_CoDe}")

                                        if OwNer_UiD and ChaT_CoDe:
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
                                            print(f"DEBUG: Sending ExitSq")
                                            xSeT.CliEnts2.send(ExitSq('000000', xSeT.key, xSeT.iv))
                                            time.sleep(0.2)

                                            response_received = True
                                            return {
                                                "success": True,
                                                "OwNer_UiD": OwNer_UiD,
                                                "SQuAD_CoDe": SQuAD_CoDe,
                                                "ChaT_CoDe": ChaT_CoDe
                                            }
                                        else:
                                            print("DEBUG: Failed to extract required data from response")
                                            break
                                except Exception as decode_error:
                                    print(f"DEBUG: Decode/parse error: {decode_error}")
                                    break
                                except json.JSONDecodeError as json_error:
                                    print(f"DEBUG: JSON decode error: {json_error}")
                                    break

                    except socket.timeout:
                        continue
                    except Exception as recv_error:
                        print(f"DEBUG: Receive error: {recv_error}")
                        break

                    time.sleep(0.1)

                if not response_received:
                    print(f"DEBUG: No valid response received within timeout period")

            return {"success": False, "reason": "No response or invalid data"}
        except Exception as e:
            print(f"Error => GeT Team DaTa CmD MsG! {str(e)}")
            return {"success": False, "reason": str(e)}

    def SeNd_MsG(xSeT, client, OwNer_UiD, ChaT_CoDe, message, count=100):
        try:
            if hasattr(client, 'CliEnts') and client.CliEnts:
                client.CliEnts.send(OpenCh(OwNer_UiD, ChaT_CoDe, client.key, client.iv))
                time.sleep(1)

                for i in range(count):
                    client.CliEnts.send(MsqSq(f'[b][c]{generate_random_color()}{message}', OwNer_UiD, client.key, client.iv))
                    time.sleep(0.5)

        except Exception as e:
            print(f"Error => SeNd MsG!")
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
    def SeNd_SpaM_MsG(xSeT, OwNer_UiD, ChaT_CoDe, message, count=100):
        try:
            threads = []
            message_clients = list(connected_clients.values())[:3]

            for client in message_clients:
                thread = threading.Thread(target=xSeT.SeNd_MsG, args=(client, OwNer_UiD, ChaT_CoDe, message, count))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join(timeout=30)

            return True
        except Exception as e:
            print(f"Error => SeNd Spam MsG In AccoUnT!")
            return False
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
    def cleanup_threads(xSeT):
        current_time = time.time()
        xSeT.active_threads = [t for t in xSeT.active_threads
                              if t['thread'].is_alive() and
                              current_time - t['start_time'] < xSeT.thread_timeout]

    def ConnEcT_SerVer_OnLiNe(xSeT, Token, tok, host, port, key, iv, host2, port2):
        xSeT.key = key
        xSeT.iv = iv
        while True:
            try:
                xSeT.CliEnts2 = socket.create_connection((host2, int(port2)))
                xSeT.CliEnts2.send(bytes.fromhex(tok))

                while True:
                    try:
                        xSeT.DaTa2 = xSeT.CliEnts2.recv(99999)
                        if not xSeT.DaTa2:
                            break
                        if len(xSeT.DaTa2.hex()) > 4 and '0500' in xSeT.DaTa2.hex()[0:4] and len(xSeT.DaTa2.hex()) > 30:
                            xSeT.packet = json.loads(DeCode_PackEt(f'08{xSeT.DaTa2.hex().split("08", 1)[1]}'))
                            if '5' in xSeT.packet and 'data' in xSeT.packet['5'] and '7' in xSeT.packet['5']['data'] and 'data' in xSeT.packet['5']['data']['7']:
                                xSeT.AutH = xSeT.packet['5']['data']['7']['data']
                    except Exception as e:
                        print(f"Error => SeConDaRy ConnEcTion!")
                        break

            except Exception as e:
                print(f"Error => WTF!")
                time.sleep(2)
                continue

    def ConnEcT_SerVer(xSeT, Token, tok, host, port, key, iv, host2, port2):
        xSeT.key = key
        xSeT.iv = iv
        try:
            xSeT.CliEnts = socket.create_connection((host, int(port)))
            xSeT.CliEnts.send(bytes.fromhex(tok))
            xSeT.DaTa = xSeT.CliEnts.recv(1024)
        except Exception as e:
            print(f"Error => ConnEcTinG To SeRVeR! ")
            time.sleep(2)
            xSeT.ConnEcT_SerVer(Token, tok, host, port, key, iv, host2, port2)
            return
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
        secondary_thread = threading.Thread(target=xSeT.ConnEcT_SerVer_OnLiNe, args=(Token, tok, host, port, key, iv, host2, port2), daemon=True)
        secondary_thread.start()

        xSeT.Exemple = xMsGFixinG('Fu*Ck YoU')
        while True:
            try:
                xSeT.DaTa = xSeT.CliEnts.recv(1024)
                if len(xSeT.DaTa) == 0:
                    try:
                        xSeT.CliEnts.close()
                        if hasattr(xSeT, 'CliEnts2') and xSeT.CliEnts2:
                            xSeT.CliEnts2.close()
                        xSeT.ConnEcT_SerVer(Token, tok, host, port, key, iv, host2, port2)
                    except:
                        ResTarT_zbi()

                xSeT.retry_count = 0

                xSeT.cleanup_threads()

            except Exception as e:
                print(f"Error => {e}")
                xSeT.retry_count += 1

                if xSeT.retry_count >= xSeT.max_retries:
                    print(f"Max retries reached for account {xSeT.id}. Restarting...")
                    return

                try:
                    if xSeT.CliEnts:
                        xSeT.CliEnts.close()
                    if hasattr(xSeT, 'CliEnts2') and xSeT.CliEnts2:
                        xSeT.CliEnts2.close()
                except:
                    pass
                time.sleep(2)
                xSeT.ConnEcT_SerVer(Token, tok, host, port, key, iv, host2, port2)

    def GeT_Key_Iv(xSeT, serialized_data):
        try:
            import Xr
            my_message = Xr.MyMessage()
            my_message.ParseFromString(serialized_data)
            timestamp, key, iv = my_message.field21, my_message.field22, my_message.field23
            timestamp_obj = Timestamp()
            timestamp_obj.FromNanoseconds(timestamp)
            timestamp_seconds = timestamp_obj.seconds
            timestamp_nanos = timestamp_obj.nanos
            combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
            return combined_timestamp, key, iv
        except Exception as e:
            print(f"Error in GeT_Key_Iv! {e}")
            return None, None, None
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
    def GuestLogin(xSeT , uid , password):
        uRL = "https://100067.connect.garena.com/oauth/guest/token/grant"
        Hr = {"Host": "100067.connect.garena.com","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1","Content-Type": "application/x-www-form-urlencoded","Accept-Encoding": "gzip, deflate","Connection": "close",}
        xDaTa = {"uid": f"{uid}","password": f"{password}","response_type": "token","client_type": "2","client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3","client_id": "100067",}
        try:
            xSeT.response = requests.post(uRL, headers=Hr, data=xDaTa).json()
            xSeT.Access_ToKen , xSeT.Access_Uid = xSeT.response['access_token'] , xSeT.response['open_id']

            time.sleep(0.2)
            return xSeT.MajorLogin(xSeT.Access_ToKen , xSeT.Access_Uid)
        except Exception:
            print('Error => GuEsT LoGin!')
            sys.exit()
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
    def DataLogin(xSeT , JwT_ToKen , PayLoad):
        uRL = 'https://clientbp.ggpolarbear.com/GetLoginData'
        Hr = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JwT_ToKen}',
            'X-Unity-Version': '2022.3.47f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB52',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Host': 'clientbp.ggpolarbear.com',
            'Connection': 'close',
            'Accept-Encoding':  'gzip'}
        try:
                xSeT.Res = requests.post(uRL , headers=Hr , data=PayLoad , verify=False)
                xSeT.DaTa_Pb2 = json.loads(DeCode_PackEt(xSeT.Res.content.hex()))
                address , address2 = xSeT.DaTa_Pb2['32']['data'] , xSeT.DaTa_Pb2['14']['data']
                ip , ip2 = address[:len(address) - 6] , address2[:len(address2) - 6]
                port , port2 = address[len(address) - 5:] , address2[len(address2) - 5:]
                return ip , port , ip2 , port2
        except requests.RequestException as e:
                print("Error => DaTa LoGin!")
        return None, None

    def MajorLogin(xSeT , Access_ToKen , Access_Uid):
        uRL = "https://loginbp.ggpolarbear.com/MajorLogin"
        Hr = {
            'X-Unity-Version': '2022.3.47f1',
            'ReleaseVersion': 'OB52',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'Content-Length': '928',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Host': 'loginbp.ggpolarbear.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'}
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
        # Updated payload for OB52
        xSeT.dT = b'\x1a\x132026-01-14 12:19:02"\tfree fire(\x01:\x071.120.1B2Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)J\x08HandheldR\x0cMTN/SpacetelZ\x04WIFI`\x80\nh\xd0\x05r\x03240z-x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4\x80\x01\xe6\x1e\x8a\x01\x0fAdreno (TM) 640\x92\x01\rOpenGL ES 3.2\x9a\x01+Google|625f716f-91a7-495b-9f16-08fe9d3c6533\xa2\x01\r176.28.145.29\xaa\x01\x02ar\xb2\x01 9132c6fb72caccfdc8120d9ec2cc06b8\xba\x01\x014\xc2\x01\x08Handheld\xca\x01\rOnePlus A5010\xd2\x01\x02SG\xea\x01@3dfa9ab9d25270faf432f7b528564be9ec4790bc744a4eba70225207427d0c40\xf0\x01\x01\xca\x02\x0cMTN/Spacetel\xd2\x02\x04WIFI\xca\x03 1ac4b80ecf0478a44203bf8fac6120f5\xe0\x03\xb5\xee\x02\xe8\x03\xc2\x83\x02\xf0\x03\xaf\x13\xf8\x03\x84\x07\x80\x04\xcf\x92\x02\x88\x04\xb5\xee\x02\x90\x04\xcf\x92\x02\x98\x04\xb5\xee\x02\xb0\x04\x04\xc8\x04\x03\xd2\x04=/data/app/com.dts.freefireth-I1hUq4t4vA6_Qo4C-XgaeQ==/lib/arm\xe0\x04\x01\xea\x04_e62ab9354d8fb5fb081db338acb33491|/data/app/com.dts.freefireth-I1hUq4t4vA6_Qo4C-XgaeQ==/base.apk\xf0\x04\x06\xf8\x04\x01\x8a\x05\x0232\x9a\x05\n2019119624\xb2\x05\tOpenGLES2\xb8\x05\xff\x01\xc0\x05\x04\xe0\x05\xed\xb4\x02\xea\x05\t3rd_party\xf2\x05\\KqsHT8Q+ls0+DdIl/OavRrovpyZYcwgnQHQQcmWwjGmXvBQKOMctxpyopTQWTHvS5JqMigGkSLCLB6Q8x9TAavMfljo=\x88\x06\x01\x90\x06\x01\x9a\x06\x014\xa2\x06\x014\xb2\x06"@\x06GOVT\n\x01\x1a]\x0e\x11^\x00\x17\rKn\x08W\tQ\nhZ\x02Xh\x00\to\x00\x01a'
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
        # تحديث البيانات الديناميكية
        xSeT.dT = xSeT.dT.replace(b'2026-01-14 12:19:02', str(datetime.now())[:-7].encode())
        xSeT.dT = xSeT.dT.replace(b'9132c6fb72caccfdc8120d9ec2cc06b8', Access_Uid.encode())
        xSeT.dT = xSeT.dT.replace(b'3dfa9ab9d25270faf432f7b528564be9ec4790bc744a4eba70225207427d0c40', Access_ToKen.encode())

        xSeT.PaYload = bytes.fromhex(EnC_AEs(xSeT.dT.hex()))
        xSeT.ResPonse = requests.post(uRL, headers = Hr ,  data = xSeT.PaYload , verify=False)
        if xSeT.ResPonse.status_code == 200 and len(xSeT.ResPonse.text) > 10:
            xSeT.DaTa_Pb2 = json.loads(DeCode_PackEt(xSeT.ResPonse.content.hex()))
            xSeT.JwT_ToKen = xSeT.DaTa_Pb2['8']['data']
            xSeT.combined_timestamp , xSeT.key , xSeT.iv = xSeT.GeT_Key_Iv(xSeT.ResPonse.content)
            ip , port , ip2 , port2 = xSeT.DataLogin(xSeT.JwT_ToKen , xSeT.PaYload)
            return xSeT.JwT_ToKen , xSeT.key , xSeT.iv, xSeT.combined_timestamp , ip , port , ip2 , port2
        else:
            print(f"Error MajorLogin: Status Code {xSeT.ResPonse.status_code}")
            sys.exit()
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
    def GeNToKeNLogin(xSeT):
        token , key , iv , Timestamp , ip , port , ip2 , port2 = xSeT.GuestLogin(xSeT.id , xSeT.password)
        xSeT.JwT_ToKen = token
        try:
            xSeT.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            xSeT.AccounT_Uid = xSeT.AfTer_DeC_JwT.get('account_id')
            xSeT.EncoDed_AccounT = hex(xSeT.AccounT_Uid)[2:]
            xSeT.HeX_VaLue = DecodE_HeX(Timestamp)
            xSeT.TimE_HEx = xSeT.HeX_VaLue
            xSeT.JwT_ToKen_ = token.encode().hex()
        except Exception as e:
            print(f"Error => GeT ToKeN Login! {e}")
            return
        try:
            xSeT.Header = hex(len(EnC_PacKeT(xSeT.JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(xSeT.EncoDed_AccounT)
            xSeT.__ = '00000000'
            if length == 9: xSeT.__ = '0000000'
            elif length == 8: xSeT.__ = '00000000  '
            elif length == 10: xSeT.__ = '000000'
            elif length == 7: xSeT.__ = '000000000'
            else:
                print('Unexpected length encountered')
            xSeT.Header = f'0115{xSeT.__}{xSeT.EncoDed_AccounT}{xSeT.TimE_HEx}00000{xSeT.Header}'
            xSeT.FiNal_ToKen_0115 = xSeT.Header + EnC_PacKeT(xSeT.JwT_ToKen_ , key , iv)

        except Exception as e:
            print(f"Error => In FiNaL ToKeN! {e}")
        xSeT.AutH_ToKen = xSeT.FiNal_ToKen_0115
        xSeT.ConnEcT_SerVer(xSeT.JwT_ToKen , xSeT.AutH_ToKen , ip , port , key , iv , ip2 , port2)
        return xSeT.AutH_ToKen , key , iv

def GeTSQDaTa(dT):
    try:
        print(f"DEBUG GeTSQDaTa: Keys in dT: {list(dT.keys())}")

        if '5' in dT and 'data' in dT['5']:
            data_field = dT['5']['data']
            print(f"DEBUG GeTSQDaTa: Keys in data_field: {list(data_field.keys())}")

            OwNer_UiD = data_field.get('1', {}).get('data') if '1' in data_field else None
            SQuAD_CoDe = data_field.get('31', {}).get('data') if '31' in data_field else None
            ChaT_CoDe = data_field.get('17', {}).get('data') if '17' in data_field else None

            if not ChaT_CoDe and '14' in data_field:
                ChaT_CoDe = data_field['14'].get('data')

            print(f"DEBUG GeTSQDaTa extracted:")
            print(f"  Owner UID from field 1: {OwNer_UiD}")
            print(f"  Squad Code from field 31: {SQuAD_CoDe}")
            print(f"  Chat Code from field 17: {ChaT_CoDe}")

            return OwNer_UiD, SQuAD_CoDe, ChaT_CoDe

        return None, None, None

    except Exception as e:
        print(f"Error extracting squad data: {e}")
        import traceback
        traceback.print_exc()
        return None, None, None

def ChEck_TeamCode(team_code):
    if team_code and len(team_code) >= 4:
        return True
    return False

def ResTarT_zbi():
    print("DoNe STaRT zbi.!")
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
xA = [
    {'id': '4583276194', 'password': 'CTX_MASRY_EDQFPFAZDxxxx'},
    {'id': '4583276637', 'password': 'CTX_MASRY_OQTGMAPJXxxxx'},
    {'id': '4583278255', 'password': 'CTX_MASRY_BH3UHV9FVxxxx'},
    {'id': '4583278412', 'password': 'CTX_MASRY_HFEMSBENYxxxx'},
    {'id': '4583278530', 'password': 'CTX_MASRY_GTYDFWEOJxxxx'},
    {'id': '4583278663', 'password': 'CTX_MASRY_R7TNERPVExxxx'},
    {'id': '4583278864', 'password': 'CTX_MASRY_2HUVPVRODxxxx'},
    {'id': '4583279006', 'password': 'CTX_MASRY_7EQGTSCSLxxxx'},
    {'id': '4583279124', 'password': 'CTX_MASRY_TVRTYQQONxxxx'},
]

def STaRT_AccoUnT(account):
    try:
        xCLF(account['id'], account['password'])
    except Exception as e:
        print(f"Error => STaRTinG AccOunTe {account['id']}: {e}")
        time.sleep(10)
        STaRT_AccoUnT(account)

def StarT_SerVer():
    time.sleep(1)
    threads = []

    for account in xA:
        thread = threading.Thread(target=STaRT_AccoUnT, args=(account,))
        thread.daemon = True
        threads.append(thread)
        thread.start()
        time.sleep(3)

    for thread in threads:
        thread.join()

def MeMoRy_CmD():
    while True:
        memory_usage = psutil.Process().memory_percent()
        if memory_usage > 80:
            print(f"High memory usage detected ({memory_usage}%). Restarting...")
            ResTarT_zbi()
        time.sleep(60)

memory_thread = threading.Thread(target=MeMoRy_CmD, daemon=True)
memory_thread.start()

zbi = telebot.TeleBot(MaSrY_ToKeN)

authorized_sessions = {}

def is_authorized(message):
    user_id = message.from_user.id

    if AUTHORIZED_USERS:
        return user_id in AUTHORIZED_USERS
    return user_id in authorized_sessions and authorized_sessions[user_id] == True

# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G0
@zbi.message_handler(commands=['start'])
def send_welcome(message):
    if not is_authorized(message):
        if AUTHORIZED_USERS:
            zbi.send_photo(
                message.chat.id,
                MaSrY_Pp,
                caption="<b>NOT AUTHORIZED</b>",
                parse_mode="HTML"
            )
        else:
            zbi.send_photo(
                message.chat.id,
                MaSrY_Pp,
                caption="<b>SEND PASSWORD FIRST</b>\nUse: <code>/password &lt;password&gt;</code>",
                parse_mode="HTML"
            )
        return

    zbi.send_photo(
        message.chat.id,
        MaSrY_Pp,
        caption="<b>WELCOME</b>\nFree Fire Spam zbi\nUse <code>/help</code> to see commands.",
        parse_mode="HTML"
    )

# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
@zbi.message_handler(commands=['password'])
def handle_password(message):
    if AUTHORIZED_USERS:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>PASSWORD METHOD DISABLED</b>",
            parse_mode="HTML"
        )
        return

    try:
        pwd = message.text.split(maxsplit=1)[1]
    except IndexError:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>INVALID FORMAT</b>\nExample: <code>/password 123456</code>",
            parse_mode="HTML"
        )
        return

    if pwd == PaSs:
        authorized_sessions[message.from_user.id] = True
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>LOGIN SUCCESS</b>\nYou can now use commands.",
            parse_mode="HTML"
        )
    else:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>WRONG PASSWORD</b>",
            parse_mode="HTML"
        )

# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
@zbi.message_handler(commands=['help'])
def send_help(message):
    if not is_authorized(message):
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>NOT AUTHORIZED</b>",
            parse_mode="HTML"
        )
        return

    help_text = """
<b>AVAILABLE COMMANDS</b>

<code>/start</code> - Welcome message
<code>/help</code> - Show help
<code>/spam &lt;teamcode&gt; &lt;message&gt;</code> - Send spam to squad

<b>EXAMPLE</b>
<code>/spam 123456 hello</code>

Accounts must be connected first after zbi start.
"""

    zbi.send_photo(
        message.chat.id,
        MaSrY_Pp,
        caption=help_text,
        parse_mode="HTML"
    )

# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G
@zbi.message_handler(commands=['spam'])
def handle_spam(message):
    if not is_authorized(message):
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>NOT AUTHORIZED</b>",
            parse_mode="HTML"
        )
        return

    with connected_clients_lock:
        if not connected_clients:
            zbi.send_photo(
                message.chat.id,
                MaSrY_Pp,
                caption="<b>NO CONNECTED ACCOUNTS</b>\nPlease wait.",
                parse_mode="HTML"
            )
            return
        first_client = list(connected_clients.values())[0]

    try:
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            zbi.send_photo(
                message.chat.id,
                MaSrY_Pp,
                caption="<b>INVALID FORMAT</b>\nUse: <code>/spam &lt;teamcode&gt; &lt;message&gt;</code>",
                parse_mode="HTML"
            )
            return

        teamcode = parts[1]
        msg = parts[2]

    except Exception as e:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption=f"<b>PARSING ERROR</b>\n<code>{e}</code>",
            parse_mode="HTML"
        )
        return

    wait_msg = zbi.send_photo(
        message.chat.id,
        MaSrY_Pp,
        caption=f"<b>LOADING SQUAD INFO</b>\n<code>{teamcode}</code>",
        parse_mode="HTML"
    )

    team_data = first_client.GeTinFoSqMsG(teamcode)

    try:
        zbi.delete_message(wait_msg.chat.id, wait_msg.message_id)
    except:
        pass

    if not team_data["success"]:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption=f"<b>FAILED</b>\nReason: <code>{team_data.get('reason','Unknown')}</code>",
            parse_mode="HTML"
        )
        return

    OwNer_UiD = team_data["OwNer_UiD"]
    ChaT_CoDe = team_data["ChaT_CoDe"]
    SQuAD_CoDe = team_data.get("SQuAD_CoDe", "")

    info_msg = f"""
<b>SQUAD FOUND</b>

<b>OWNER UID</b>
<code>{OwNer_UiD}</code>

<b>CHAT CODE</b>
<code>{ChaT_CoDe}</code>

<b>SQUAD CODE</b>
<code>{SQuAD_CoDe}</code>

<b>SENDING 100 MESSAGES</b>
"""

    zbi.send_photo(
        message.chat.id,
        MaSrY_Pp,
        caption=info_msg,
        parse_mode="HTML"
    )

    success = first_client.SeNd_SpaM_MsG(OwNer_UiD, ChaT_CoDe, msg, count=100)

    if success:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption=f"<b>DONE</b>\n100 messages sent to <code>{teamcode}</code>",
            parse_mode="HTML"
        )
    else:
        zbi.send_photo(
            message.chat.id,
            MaSrY_Pp,
            caption="<b>FAILED TO SEND MESSAGES</b>",
            parse_mode="HTML"
        )
        
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G        

if __name__ == '__main__':

    zbi_thread = threading.Thread(target=StarT_SerVer, daemon=True)
    zbi_thread.start()

    time.sleep(9)

    print("لا تغير حقوقي يا W9")
    zbi.infinity_polling()
# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G    