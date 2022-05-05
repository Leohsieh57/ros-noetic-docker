if [[ $1 -gt 0 ]]
then
    echo "[writing ~/.bashrc]"
    echo 'source ~/setup.bash' >> ~/.bashrc
fi