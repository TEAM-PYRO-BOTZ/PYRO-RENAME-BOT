if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrMKN/RENAMER_BOT-5.git /RENAMER_BOT-5       
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RENAMER_BOT-5
fi
cd /RENAMER_BOT-5
pip3 install -U -r requirements.txt
echo "🔥🔥🔥BOT IS STARTING🔥🔥🔥"
python3 bot.py
