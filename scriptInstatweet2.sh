#!/bin/dash
cd $HOME/Proyectos/003-TwitterAppLinux-Python
$HOME/Proyectos/003-TwitterAppLinux-Python/instatweet.py InstaTweet `cat $HOME/Proyectos/003-TwitterAppLinux-Python/.namecache`
$HOME/Proyectos/003-TwitterAppLinux-Python/Tweet.py -n >> $HOME/Proyectos/003-TwitterAppLinux-Python/.namecache
if [ `cat $HOME/Proyectos/003-TwitterAppLinux-Python/.icondirec` !=  `$HOME/Proyectos/003-TwitterAppLinux-Python/Tweet.py -i` ] 
then 
    wget `$HOME/Proyectos/003-TwitterAppLinux-Python/Tweet.py -i` -O $HOME/Proyectos/003-TwitterAppLinux-Python/.iconcache
    $HOME/Proyectos/003-TwitterAppLinux-Python/Tweet.py -i >> $HOME/Proyectos/003-TwitterAppLinux-Python/.icondirec
fi


