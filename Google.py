ó
b5ÄZc           @   sî   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z m Z d  d l m	 Z	 d   Z
 e
   d Z e	 e d  GHd   Z e d  Z d	 e k rÈ e j d	 d
  Z n  d Z e d  Z e e e e  d S(   iÿÿÿÿN(   t   urlparset   parse_qs(   t   coloredc           C   s0   t  j d k r t  j d  n t  j d  d  S(   Nt   ntt   clst   clear(   t   ost   namet   system(    (    (    s	   Google.pyt   screen   s    s   
                                                                      
  ,ad8888ba,                                          88              
 d8"'    `"8b                                         88              
d8'                                                   88              
88              ,adPPYba,    ,adPPYba,    ,adPPYb,d8  88   ,adPPYba,  
88      88888  a8"     "8a  a8"     "8a  a8"    `Y88  88  a8P_____88  
Y8,        88  8b       d8  8b       d8  8b       88  88  8PP"""""""  
 Y8a.    .a88  "8a,   ,a8"  "8a,   ,a8"  "8a,   ,d88  88  "8b,   ,aa  
  `"Y88888P"    `"YbbdP"'    `"YbbdP"'    `"YbbdP"Y8  88   `"Ybbd8"'  
                                          aa,    ,88                  
                                           "Y8bbdP" 
 |===============================================================|
 |    Google Dork HTTP/1.1 200 (OK)				 |
 |    Thanks For Member "Obsidian Cyber Team"     		 |
 |    Created : X-G77Z10HACKED        	          		 |
 |===============================================================|
t   greenc         C   s`  g  } t  | d  } d } d |  GHx| d k rBd | d |  d t |  d } t j |  j } t j d	 |  r d
 GHd GHn  t j d |  } xv | D]n }	 |	 j   }	 t |	 d  }
 |	 j	 d  r¡ t
 |
 j  d d } | j |  | j t | d   q¡ q¡ W| d 7} t d t t |   d d  GHq' Wd t t |   d GHd  S(   Nt   ai    s   {+} Sedang Dorking : id   s   http://www.google.s
   /search?q=s   &start=s   &inurl=httpss)   <script src="(.*?)" async defer></script>s=   ==> Terdeteksi Oleh Captcha Detect! Semua Pencarian Terblokirs+   ==> Gunakan ON/OFF Data Untuk Merubah IP Mus   <h3 class="r"><a href="(.*?)"t   https   /url?t   qs   
i
   s   =================>s-   <=================  Sedang Mengumpulkan Situst   yellowt   [s   ] Sukses Scan Dork(   t   opent   strt   requestst   gett   textt   ret   findallt   stripR    t
   startswithR   t   queryt   appendt   writeR   t   len(   t   dorkt   tldt   logt   urlt   resultt   paget   urllt   htmllt   linkt   it   o(    (    s	   Google.pyt   scan$   s,    	$
&s   X-G77Z10HACKED Masukan Dork : t    t   +t   coms   X-G77Z10HACKED Nama File Lu  : (   R   R   R   t   base64t   urllibt   urllib2R    R   t	   termcolorR   R	   t   bannerR(   t	   raw_inputR   t   replacet   domt   out(    (    (    s	   Google.pyt   <module>   s   H		