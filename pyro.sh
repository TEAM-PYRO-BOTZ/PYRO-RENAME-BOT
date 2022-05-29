if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TEAM-PYRO-BOTZ/RENAMER_Ultron.git /RENAMER_Ultron                              #1
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RENAMER_Ultron
fi
cd /RENAMER_Ultron
pip3 install -U -r requirements.txt
echo "🚀 𝑷𝒀𝑹𝑶 𝑩𝑶𝑻 𝑰𝑺 𝑺𝑻𝑨𝑹𝑻𝑰𝑵𝑮......."
python3 bot.py
