import tiktok
import proxies
import creator
import account
import time

from tiktok import accounts
from account import email, password, username
from proxies import *

config = {
    "acc": "your_account_name_here"  # Ganti "your_account_name_here" dengan nama akun yang ingin diikuti (jika diperlukan)
}

# Creating accounts

accounts = tiktok.accounts  # Perbaiki untuk mengakses objek accounts dari modul tiktok

creator.init(tiktok.com, accounts)  # Perbaiki argumen pada pemanggilan fungsi init

def __accountCreator__():
    x = creator.newAccount(tiktok, email, password, username)
    x.append()
    x.changeAvatar(RandomPictureNet)
    x.subTo(MostFolloweds)

# Sub to your account

def __subBot__():
    if x.banned:
        print('account is banned')
    elif x.doesNotExist:
        print('skipped account')
    else:
        x.subTo(config["acc"])
        x.pass_and_return
    print('x.followers + 1')  # Tidak jelas apa yang dimaksud dengan baris ini, perlu dilengkapi dengan instruksi yang lebih jelas
