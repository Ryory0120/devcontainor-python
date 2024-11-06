curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
echo '. "$HOME/.rye/env"' >> ~/.bashrc
echo 'echo "call ~/.bashrc"' >> ~/.bashrc

