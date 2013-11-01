'''
Created on Nov 1, 2013
This is a sample which downloads your files to downloads/ and sends new
files to your Kindle

Attention: It requires a valid e-paper abonement of FAZ.net

@author: pete
'''
import faz2kindle

KINDLE_MAIL= "youramazonperonalkindlemail@kindle.com"

# FAZ login data
FAZ_USER = "youruser"
FAZ_PASS = "fazpass"

# Gmail login data
GMAIL_USER = "yourgmail@gmail.com"
GMAIL_PASS = "gmailpass"

fazload = faz2kindle.FazLoader((FAZ_USER, FAZ_PASS), (GMAIL_USER, GMAIL_PASS), KINDLE_MAIL)
fazload.downloadAvailable()