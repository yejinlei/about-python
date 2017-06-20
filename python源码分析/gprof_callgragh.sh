#sudo apt-get install gprof2dot
#sudo apt-get install graphviz
gprof ./python gmod.out > gmod.txt
gprof2dot gmon.txt | dot -Tpng -o python.png
